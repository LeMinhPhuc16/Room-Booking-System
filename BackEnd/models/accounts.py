from sqlalchemy import String, ForeignKey, DateTime
from database.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class Account(Base):
    __tablename__ = "accounts"
    id_account: Mapped[int] = mapped_column(primary_key=True)
    id_user: Mapped[int] = mapped_column(ForeignKey("users.user_id"), nullable=False)
    user_name: Mapped[str] =  mapped_column(String(15), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    create_at: Mapped[datetime] = mapped_column(DateTime,nullable=False, default=datetime.utcnow) 

    