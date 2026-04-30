from database.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum, ForeignKey, DateTime
from datetime import datetime

class Order(Base):
    __tablename__ = "orders"
    order_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"), nullable=False)
    total_price: Mapped[int] = mapped_column(nullable=False)
    status =  mapped_column(Enum("Da thanh cong", "Chua thanh cong", "Da huy"))
    create_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)


# Table orders{
#   idOrder int [pk]
#   idUser int [ref: > users.idUser]
#   totalPrice int [not null]  //tổng tiền của các booking
#   status varchar [not null]   //cho biết trạng thái của đơn đặt
#   createAt datetime [not null]
# }