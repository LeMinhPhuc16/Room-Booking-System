from app  import app
from database.db import localSession
from models import User

@app.route('/users')
def getUsers():
    session = localSession()
    users = session.query(User).all()
    session.close()
    return users