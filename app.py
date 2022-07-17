from flask import Flask, render_template
from game_of_life import *

app = Flask(__name__)

@app.route('/')
def hello():
    GameOfLife(10, 10)
    return render_template('index.html')

@app.route('/life')
def create_life():
    UNIVERSE = GameOfLife()
    if UNIVERSE.counter >= 0:
        UNIVERSE.form_new_generation()

    return render_template('life.html', universe=UNIVERSE)

if __name__ == "__main__":
    app.run(debug=True)