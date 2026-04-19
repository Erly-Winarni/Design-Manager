from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from models.tag import asset_tags

class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    file_url = Column(String)

    category_id = Column(Integer, ForeignKey("categories.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    tags = relationship("Tag", secondary=asset_tags, back_populates="assets")

    category = relationship("Category", back_populates="assets")