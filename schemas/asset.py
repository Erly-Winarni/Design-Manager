from pydantic import BaseModel

class AssetCreate(BaseModel):
    title: str
    file_url: str
    category_id: int

class AssetResponse(BaseModel):
    id: int
    title: str
    file_url: str

    class Config:
        orm_mode = True