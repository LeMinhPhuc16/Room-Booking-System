from database.db import Base, engine
from models.user import User
from models.booking import Booking

def init_db():
    Base.metadata.create_all(engine)


init_db()