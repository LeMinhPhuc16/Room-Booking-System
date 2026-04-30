from sqlalchemy import String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from database.db import Base


class User(Base):
    __tablename__ = "users"
    user_id: Mapped[int] = mapped_column(primary_key=True)
    publicId: Mapped[str] = mapped_column(String(10), unique=True)
    name: Mapped[str]  = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    numberPhone: Mapped[str] = mapped_column( String(10), unique=True, nullable=False)

class Account(Base):
    __tablename__ = "accounts"
    id_account: Mapped[int] = mapped_column(primary_key=True)
    id_user: Mapped[int] = mapped_column(ForeignKey("users.user_id"), nullable=False)
    user_name: Mapped[str] =  mapped_column(String(15), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    create_at: Mapped[datetime] = mapped_column(DateTime,nullable=False, default=datetime.utcnow) 

class Category(Base):
    __tablename__ = "categories"
    category_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    description: Mapped[str] = mapped_column(String(255))

class Room(Base):
    __tablename__ = "rooms"
    room_id: Mapped[int] = mapped_column(primary_key=True)
    room_name: Mapped[str] = mapped_column(String(50), nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.category_id"), nullable=False, index=True)
    capacity: Mapped[int] = mapped_column(nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)    

class Booking(Base):
    __tablename__ = "bookings"
    booking_id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.room_id"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"), nullable=False)
    check_in: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    check_out:  Mapped[datetime] = mapped_column(DateTime, nullable=False)
    create_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)
    status = mapped_column(Enum("Dang xu li", "Da thanh cong", "Da huy"), default="Dang xu li", nullable=False)

class Order(Base):
    __tablename__ = "orders"
    order_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"), nullable=False)
    total_price: Mapped[int] = mapped_column(nullable=False)
    status =  mapped_column(Enum("Da thanh cong", "Chua thanh cong", "Da huy"))
    create_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)

class OrderItem(Base):
    __tablename__ = "order_items"
    item_id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.order_id"), nullable=False)
    booking_id: Mapped[int] = mapped_column(ForeignKey("bookings.booking_id"), nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)


class Payment(Base):
    __tablename__ = "payments"
    payment_id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.order_id"), nullable=False, index=True)
    amount: Mapped[int] = mapped_column(nullable=False)
    status = mapped_column(Enum("Da thanh toan", "Chua thanh toan", "Thanh toan that bai"))
    method: Mapped[str] = mapped_column(String(255), nullable=False)
    transaction_id : Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    create_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow, index=True)