from flask import Flask, render_template, request, redirect, session, url_for
from flask_socketio import join_room, leave_room, SocketIO, send
import random
from string import ascii_uppercase

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

rooms = {}

def generate_room_code(length=6):
    code = ''.join(random.choices(ascii_uppercase, k=length))
    while code in rooms:
        code = ''.join(random.choices(ascii_uppercase, k=length))
    return code

@app.route('/', methods=['GET', 'POST'])
def index():
    session.clear()
    errors = []
    if request.method == 'POST':
        name = request.form.get('name')
        code = request.form.get('code')
        join = request.form.get('join', False)
        create = request.form.get('create', False)
        if not name:
            errors.append('Name is required.')
        if join != False and code.strip() == '':
            errors.append('Room code is required to join a room.')
    
        if errors:
            return render_template('index.html', errors=errors)
        room = code
        if create != False:
            room = generate_room_code()
            rooms[room] = {'members': 0, 'messages': []}
            session['name'] = name
            session['room'] = room
            return redirect(url_for('room'))
        if code not in rooms:
            errors.append('Room code does not exist.')
            return render_template('index.html', errors=errors, code=code, name=name)
        session['name'] = name
        session['room'] = room
        return redirect(url_for('room'))
        

    return render_template('index.html')

@app.route('/room')
def room():
    name = session.get('name')
    room = session.get('room')
    if not name or not room or room not in rooms:
        return redirect(url_for('index'))
    return render_template('room.html', name=name, room=room)

@socketio.on('connect')
def handle_connect(auth):
    room = session.get('room')
    name = session.get('name')
    if not room and not name:
        return
    if room in rooms:
        join_room(room)
        send({"name": name, "message": f'{name} has joined the room.'}, to=room)
        rooms[room]['members'] += 1
        print(f'{name} has joined room {room}. Total members: {rooms[room]["members"]}')
    else:
        leave_room(room)
    
@socketio.on('disconnect')
def handle_disconnect():
    room = session.get('room')
    name = session.get('name')
    if room in rooms:
        leave_room(room)
        rooms[room]['members'] -= 1
        send({"name": name, "message": f'{name} has left the room.'}, to=room)
        print(f'{name} has left room {room}. Total members: {rooms[room]["members"]}')
        if rooms[room]['members'] <= 0:
            del rooms[room]
            print(f'Room {room} has been deleted due to no members.')

@socketio.on('message')
def handle_message(data):
    room = session.get('room')
    name = session.get('name')
    if room in rooms:
        message = f'{name}: {data["data"]}'
        rooms[room]['messages'].append(message)
        send({"name": name, "message": data["data"]}, to=room)
        print(f'Message in room {room}: {message}')

if __name__ == '__main__':
    socketio.run(app, debug=True)

