from flask import Flask
from controller.controllers import main

app = Flask(__name__)
app.register_blueprint(main)
app.secret_key = "abcd1234"

if __name__ == "__main__":
    #debug=False
    app.run(debug=True)
