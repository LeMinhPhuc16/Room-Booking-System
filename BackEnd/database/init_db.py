from database.db import Base, engine
import models
def init_db():
    print(Base.metadata.tables.keys())
    Base.metadata.create_all(engine)