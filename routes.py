from btracker import app

@app.route("/")
def main_():
    return "<h1>Hello World!<h1>"
    