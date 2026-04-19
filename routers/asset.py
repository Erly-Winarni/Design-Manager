from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.asset import Asset
from schemas.asset import AssetCreate
from auth.auth_bearer import JWTBearer
from auth.utils import get_current_user

router = APIRouter()
security = JWTBearer()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", dependencies=[Depends(security)])
def create_asset(
    asset: AssetCreate,
    token: str = Depends(security),
    db: Session = Depends(get_db)
):
    user = get_current_user(token)

    new_asset = Asset(
        title=asset.title,
        file_url=asset.file_url,
        category_id=asset.category_id,
        user_id=user.id
    )

    db.add(new_asset)
    db.commit()
    db.refresh(new_asset)

    return new_asset

@router.get("/")
def get_assets(db: Session = Depends(get_db)):
    return db.query(Asset).all()


@router.get("/{asset_id}")
def get_asset(asset_id: int, db: Session = Depends(get_db)):
    asset = db.query(Asset).filter(Asset.id == asset_id).first()

    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")

    return asset

@router.put("/{asset_id}", dependencies=[Depends(security)])
def update_asset(
    asset_id: int,
    updated: AssetCreate,
    token: str = Depends(security),
    db: Session = Depends(get_db)
):
    asset = db.query(Asset).filter(Asset.id == asset_id).first()

    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")

    user = get_current_user(token)
    if asset.user_id != user.id:
        raise HTTPException(status_code=403, detail="Not allowed")

    asset.title = updated.title
    asset.file_url = updated.file_url
    asset.category_id = updated.category_id

    db.commit()
    db.refresh(asset)

    return asset

@router.delete("/{asset_id}", dependencies=[Depends(security)])
def delete_asset(
    asset_id: int,
    token: str = Depends(security),
    db: Session = Depends(get_db)
):
    asset = db.query(Asset).filter(Asset.id == asset_id).first()

    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")

    user = get_current_user(token)
    if asset.user_id != user.id:
        raise HTTPException(status_code=403, detail="Not allowed")

    db.delete(asset)
    db.commit()

    return {"message": "Asset deleted successfully"}