from app import app
from database.db import localSession
from sqlalchemy import text

@app.route('/getGridRoom', methods=['GET'])
def get_grid_room():
    session_to_get_grid_room = localSession()
    try:
        query_rooms = text("""select rooms_table.room_id, room_name, bookings.time_end, bookings.time_start, bookings.status
                            from rooms as rooms_table
                            left join bookings on bookings.room_id = rooms_table.room_id 
                            and ( bookings.time_start < date_add(curdate(), interval(4) day)
                            and bookings.time_end > curdate() )
                            ORDER BY rooms_table.room_id, bookings.time_start;
                            """)
        data_Rooms_from_db =session_to_get_grid_room.execute(query_rooms)
        result = []
        for row in data_Rooms_from_db:
            result.append({
                "room_id": row[0],
                "room_name": row[1],
                "time_end": row[2],
                "time_start": row[3],
                "status": row[4]
            })
        return {
            "message": "Get grid room successfully",
            "data": result
        }, 200
    except Exception as e:
        return {"error": str(e)}, 400
    finally:
        session_to_get_grid_room.close()