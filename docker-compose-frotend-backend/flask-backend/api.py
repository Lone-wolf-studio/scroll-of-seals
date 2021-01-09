import time
from flask import Flask

app = Flask(__name__)

@app.route('/api')
def get_current_time():
    return "Hello from backend"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
