from database.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Enum, ForeignKey, DateTime
from datetime import datetime

class Payment(Base):
    __tablename__ = "payments"
    payment_id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id_order"), nullable=False, index=True)
    amount: Mapped[int] = mapped_column(nullable=False)
    status = mapped_column(Enum("Da thanh toan", "Chua thanh toan", "Thanh toan that bai"))
    method: Mapped[str] = mapped_column(String(255), nullable=False)
    transaction_id : Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    create_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow, index=True)


# Table payment{
#   idPayment int [primary key]
#   idOrder int [ref: > orders.idOrder]
#   amount int [not null]

#   status varchar [not null]  //cho biết trạng thái thanh toán hiện tại
#   method varchar 
#   transactionId varchar [not null, unique]
#   createAt datetime [not null]

#   indexes {
#     idOrder
#     status
#   }
# }