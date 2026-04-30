from sqlalchemy import String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from database.db import Base

class Booking(Base):
    __tablename__ = "bookings"
    booking_id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.room_id"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"), nullable=False)
    check_in: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    check_out:  Mapped[datetime] = mapped_column(DateTime, nullable=False)
    create_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)
    status = mapped_column(Enum("Dang xu li", "Da thanh cong", "Da huy"), default="Dang xu li", nullable=False)
