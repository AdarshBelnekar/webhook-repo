from app import create_app
from flask_cors import CORS
from flask import render_template

app = create_app()
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
