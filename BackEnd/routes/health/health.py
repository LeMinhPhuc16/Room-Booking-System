from app import app
from database.db import localSession
from sqlalchemy import text
@app.route('/health')
def health():
    session = localSession()
    try:
        session.execute(text("SELECT 1"))
        return {"status": "ok"}, 200
    except Exception as error:
        return {"status": "error"}, 500
    finally:
        session.close()