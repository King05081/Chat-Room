from flask import Flask,render_template,request
from flask_socketio import SocketIO, emit
from datetime import datetime
import random

app = Flask(__name__)
socketio = SocketIO(app)

# python dict. Store connected users. Key is socket id, value is username and avatarUrl 
users = {}

@app.route('/')
def index():
    return render_template('index.html')

# we're listening for the connect event
@socketio.on("connect")
def handle_connect():
    username = f"User_{random.randint(1000,9999)}"
    gender = random.choice(["girl","boy"])
    # https://avatar.iran.liara.run/public/boy?username=User_123
    avatar_url = f"https://api.dicebear.com/9.x/bottts-neutral/svg?seed={username}"

    users[request.sid] = { "username":username,"avatar":avatar_url}

    emit("user_joined", {"username":username,"avatar":avatar_url},broadcast=True)

    emit("set_username", {"username":username})

@socketio.on("disconnect")
def handle_disconnect():
    user = users.pop(request.sid, None)
    if user:
      emit("user_left", {"username":user["username"]},broadcast=True)


@socketio.on("send_message")
def handle_message(data):
    user = users.get(request.sid)
    if user:
        timestamp = datetime.now().strftime("%I:%M %p")  # Format time as HH:MM AM/PM
        emit("new_message", {
            "username": user["username"],
            "avatar": user["avatar"],
            "message": data["message"],
            "timestamp": timestamp
        }, broadcast=True)

@socketio.on("update_username")
def handle_update_username(data):
    old_username = users[request.sid]["username"]
    new_username = data["username"]
    users[request.sid]["username"] = new_username

    emit("username_updated", {
        "old_username":old_username,
        "new_username":new_username
    }, broadcast=True)

if __name__ == "__main__":
    socketio.run(app) 
