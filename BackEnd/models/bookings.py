from sqlalchemy import ForeignKey, DateTime, Enum, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from database.db import Base

class Booking(Base):
    __tablename__ = "bookings"
    booking_id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.room_id"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"), nullable=False)
    time_start: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    time_end: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now)
    status: Mapped[str] = mapped_column(Enum("Dang xu li", "Da thanh cong", "Da huy"), default="Dang xu li", nullable=False)

    __table_args__ = (
        CheckConstraint("time_end > time_start", name = "time_end_after_time_start"),
    )

