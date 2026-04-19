from fastapi import FastAPI
from database import Base, engine
from routers import auth, category, asset
from routers import tag


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Design Asset Manager API")

app.include_router(auth.router, prefix="/auth")
app.include_router(category.router, prefix="/categories")
app.include_router(asset.router, prefix="/assets")
app.include_router(tag.router, prefix="/tags", tags=["Tags"])