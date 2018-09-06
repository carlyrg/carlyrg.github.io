import os
from flask import Flask, request, render_template, send_from_directory, url_for

app = Flask(__name__, static_url_path='/static')

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return "hi  "
    return render_template("photoGallery.html")

@app.route('/gallery')
def get_gallery():
    image_names = os.listdir('static')
    return render_template("photoGallery.html", image_names=image_names)

if __name__ == "__main__":
    app.run(port=5000, debug=True)