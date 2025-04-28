from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

rooms = {"P1111": None, "P1158": None, "P1159": None, "P1160": None}

@app.route('/')
def home():
    return render_template("index.html", rooms=rooms)

@app.route('/show_book_form', methods=['POST','GET'])
def show_book_form():
    room_number = request.form.get("room_number")
    guest_name = request.form.get("guest_name")
    return render_template("show_booking.html", room_number=room_number, guest_name=guest_name)

@app.route('/book', methods=['POST','GET'])
def do_book_room():
    room_number = request.form.get("room_number").strip()
    guest_name = request.form.get("guest_name").strip()
    msg = request.form.get("msg")
    rooms[room_number] = guest_name
    if room_number in rooms:
        if rooms[room_number] is None:
               rooms[room_number] = guest_name         
        else:
            msg = f"Room {room_number} is already booked by {guest_name}."
            rooms[room_number] = guest_name 

    else:
        msg = "Invalid room number {{ room_number}} for guest {{ guest_name}}."

    return render_template("index.html", rooms=rooms, msg=msg)

@app.route('/cancel', methods=['POST', 'GET'])
def cancel_booking():
    if request.method == "GET":
        room_number = request.args.get('room_number').strip()
    if room_number in rooms:
        if rooms[room_number] is not None:
            rooms[room_number] = None
            message = f"Booking for Room {room_number} has been canceled."
        else:
            message = f"Room {room_number} is not booked."
    else:
        message = "Invalid room number {{room_number}} ."
    return render_template("index.html", rooms=rooms, msg="Room Booking cancelled")
   # return jsonify({"message": message})

@app.route('/available', methods=['GET'])
def show_available_rooms():
    available_rooms = [room for room, guest in rooms.items() if guest is None]
    return jsonify({"available_rooms": available_rooms})




if __name__ == '__main__':
    # Load rooms from file
    app.run(debug=True)