from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room
import random
import base64
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = 'rouge_secret_key_2024'
socketio = SocketIO(app, cors_allowed_origins="*")

# Store active rooms and their participants
rooms = {}
MAX_FILE_SIZE = 8 * 1024 * 1024  # 8MB

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create')
def create_room():
    return render_template('create.html')

@app.route('/join')
def join_room_page():
    return render_template('join.html')

@app.route('/chat/<room_code>')
def chat(room_code):
    return render_template('chat.html', room_code=room_code)

@socketio.on('create_room')
def on_create_room():
    """Generate a unique room code"""
    room_code = str(random.randint(100000, 999999))
    rooms[room_code] = {'users': []}
    emit('room_created', {'room_code': room_code})

@socketio.on('join_room')
def on_join_room(data):
    """Join a room with the given code"""
    room_code = data.get('room_code')
    if room_code in rooms:
        join_room(room_code)
        if 'users' not in rooms[room_code]:
            rooms[room_code]['users'] = []
        rooms[room_code]['users'].append(request.sid)
        emit('room_joined', {'status': 'success', 'room_code': room_code})
    else:
        emit('room_joined', {'status': 'error', 'message': 'Invalid room code'})

@socketio.on('connect')
def on_connect():
    emit('connected', {'data': 'Connected to ROUGE'})

@socketio.on('disconnect')
def on_disconnect():
    """Remove user from all rooms on disconnect"""
    for room_code, room_data in rooms.items():
        if 'users' in room_data and request.sid in room_data['users']:
            room_data['users'].remove(request.sid)
            if len(room_data['users']) == 0:
                del rooms[room_code]
            else:
                leave_room(room_code)
            break

@socketio.on('send_message')
def on_send_message(data):
    """Handle text messages"""
    room_code = data.get('room_code')
    message = data.get('message')
    if room_code in rooms:
        socketio.emit('receive_message', {
            'message': message,
            'sender': request.sid
        }, room=room_code)

@socketio.on('send_image')
def on_send_image(data):
    """Handle image messages"""
    room_code = data.get('room_code')
    image_data = data.get('image_data')
    if room_code in rooms:
        socketio.emit('receive_image', {
            'image_data': image_data,
            'sender': request.sid
        }, room=room_code)

@app.route('/upload_image', methods=['POST'])
def upload_image():
    """Handle image uploads"""
    if 'image' not in request.files:
        return jsonify({'error': 'No image file'}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    # Check file size
    file.seek(0, os.SEEK_END)
    file_size = file.tell()
    file.seek(0)
    
    if file_size > MAX_FILE_SIZE:
        return jsonify({'error': 'File too large (max 8MB)'}), 400
    
    # Convert to base64
    image_data = base64.b64encode(file.read()).decode('utf-8')
    return jsonify({'image_data': image_data})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True, allow_unsafe_werkzeug=True)

