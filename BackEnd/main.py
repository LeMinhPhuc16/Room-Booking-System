from app import app
from database.init_db import init_db
from routes.health.health import health #Kiểm tra sức API
from routes.getGridRoom.getGridRoom import get_grid_room  #import API lấy dữ liệu phòng từ database
from routes.createBooking.createBooking import create_booking #import API tạo booking mới vào database


def main():
    init_db()

if __name__ == "__main__":
    main()
    print(app.url_map)
    app.run(debug=True)