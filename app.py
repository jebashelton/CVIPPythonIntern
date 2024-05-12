from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    return render_template('index.html', current_time=now)

if __name__ == '__main__':
    app.run(debug=True)
