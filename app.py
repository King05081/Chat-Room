from flask import Flask,render_template,request
from flask_socketio import SocketIO, emit
import random



app = Flask(__name__)
socketio = SocketIO(app)

# python dictionary. Store connected users. Key is socketid. Value is username and avatarUrl
users = {}

@app.route('/')
def index():
    return render_template('index.html')

# .on means we are listening for the connect event
@socketio.on("connect")
# when a user connects they get assigned username and icon
def handle_connect():
    username = f"User_{random.randint(100,9999)}"
    gender = random.choice(["girl","boy"])
    # https://avatar.iran.liara.run/public/boy?username=User_123
    avatar_url = f" https://api.dicebear.com/9.x/bottts-neutral/svg?seed={username}"
    # when a user joins the group give a username and picture
    users[request.sid] = { "username":username,"avatar":avatar_url}

    emit("user_joined", {"username":username,"avatar":avatar_url},broadcast=True)

    emit("set_username", {"username":username})
# when user disconnects tells everyone they left
@socketio.on("disconnect")
def handle_disconnect():
    user = users.pop(request.sid, None)
    if user:
      emit("user_left", {"username":user["username"]},broadcast=True)
# when user sends a message have everyone see it
@socketio.on("send_message")
def handle_message(data):
    user = users.get(request.sid)
    if user:
        emit("new_message", {
            "username":user["username"],
            "avatar":user["avatar"],
            "message":data["message"]
        }, broadcast=True)
# when user changes usernames switch old for new
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