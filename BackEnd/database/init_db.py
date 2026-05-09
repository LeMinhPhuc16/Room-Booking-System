from database.db import Base, engine
import models
def init_db():
    Base.metadata.create_all(engine)