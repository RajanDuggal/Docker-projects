from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """Hello, Kim Duggal
            My babu!
            You are the best!
            My wifey
            Love you so much! <3
            welcome to my docker container"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
