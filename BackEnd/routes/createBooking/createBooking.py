from app import app
from database.db import localSession
from sqlalchemy import text
from flask import request
from models.bookings import Booking
from datetime import datetime

@app.route('/createBooking', methods = ['POST'])
def create_booking():
    session = localSession()
    try:
        data = request.get_json()
        new_booking = Booking(
            room_id = data['room_id'],
            user_id = data['user_id'],
            time_start = datetime.strptime(data['time_start'], "%Y-%m-%d %H:%M:%S"),
            time_end = datetime.strptime(data['time_end'], "%Y-%m-%d %H:%M:%S")
        )
        session.add(new_booking)
        session.commit()
        return {
            "message": "Booking created successfully",
            "booking_id": new_booking.booking_id
        }, 201
    except Exception as e:
        session.rollback()
        return {"error": str(e)}, 400
    finally:
        session.close()