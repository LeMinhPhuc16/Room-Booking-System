from database.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Enum, ForeignKey

class OrderItem(Base):
    __tablename__ = "order_items"
    item_id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.order_id"), nullable=False)
    booking_id: Mapped[int] = mapped_column(ForeignKey("bookings.booking_id"), nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)



# Table orderItem{
#   idItem int [primary key]
#   idOrder int [ref: > orders.idOrder]
#   idBooking int [ref: > bookings.idBooking] 
#   price int [not null]   //giá lúc đặt (có thể ảnh hưởng voucher, ...)
# }