from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def Hello():
    if request.method == 'POST':
        file = request.files["file"]
        file.save(os.path.join("Video_Uploads", file.filename))
        return render_template("base.html", message = "Success")
    return render_template("base.html", message = "Upload") 

if __name__ == "__main__":
    app.run("localhost", 1000, debug=True)    