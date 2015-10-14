from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Index File \n"

@app.route("/hello")
def hello():
    return "Hello world \n"

@app.route("/user/<username>")
def user_profile(username):
    return "User %s \n" % username

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return "Post %d \n" % post_id

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
