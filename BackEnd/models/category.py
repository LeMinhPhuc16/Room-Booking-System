from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from database.db import Base

class Category(Base):
    __tablename__ = "categories"
    category_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    description: Mapped[str] = mapped_column(String(255))