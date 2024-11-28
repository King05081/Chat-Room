from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import random
from datetime import datetime

app = Flask(__name__)
socketio = SocketIO(app)

users = {}  # Store connected users: key is socket ID, value is user data
messages = {}  # Store messages with their reactions


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on("connect")
def handle_connect():
    username = f"User_{random.randint(1000, 9999)}"
    avatar_url = f"https://api.dicebear.com/9.x/bottts-neutral/svg?seed={username}"
    users[request.sid] = {"username": username, "avatar": avatar_url}
    emit("user_joined", {"username": username, "avatar": avatar_url}, broadcast=True)
    emit("set_username", {"username": username})


@socketio.on("disconnect")
def handle_disconnect():
    user = users.pop(request.sid, None)
    if user:
        emit("user_left", {"username": user["username"]}, broadcast=True)


@socketio.on("send_message")
def handle_message(data):
    user = users.get(request.sid)
    if user:
        message_id = len(messages) + 1
        timestamp = datetime.now().strftime("%I:%M %p")
        message_data = {
            "id": message_id,
            "username": user["username"],
            "avatar": user["avatar"],
            "message": data["message"],
            "timestamp": timestamp,
            "reactions": {},  # Store reactions as {emoji: [usernames]}
        }
        messages[message_id] = message_data
        emit("new_message", message_data, broadcast=True)


@socketio.on("add_reaction")
def handle_reaction(data):
    message_id = data.get("message_id")
    emoji = data.get("emoji")
    user = users.get(request.sid)

    if message_id in messages and user:
        message = messages[message_id]
        username = user["username"]

        if emoji not in message["reactions"]:
            message["reactions"][emoji] = []
        if username not in message["reactions"][emoji]:
            message["reactions"][emoji].append(username)

        emit("update_message", message, broadcast=True)


if __name__ == "__main__":
    socketio.run(app)
