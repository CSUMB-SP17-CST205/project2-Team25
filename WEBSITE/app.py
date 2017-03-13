import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap



app = Flask(__name__)

bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('user.html')




if __name__ == '__main__':
    app.run(
        debug = True,
        port = int(os.getenv('PORT', 8080)),
        host = os.getenv('IP', '0.0.0.0')
    )