from app import app
from database.init_db import init_db
from routes import test

def main():
    init_db()

if __name__ == "__main__":
    main()
    app.run(debug=True)
