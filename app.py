from flask import Flask, render_template, request, jsonify
from werkzeug.utils import redirect
import os

from Katna.video import Video
from Katna.writer import KeyFrameDiskWriter

app = Flask(__name__)

no_of_frames_to_return = 10
global fileName
fileName = ''


@app.route('/', methods=["GET", "POST"])
def Hello():
    if request.method == 'POST':
        global fileName
        file = request.files["file"]
        fileName = file.filename
        file.save(os.path.join("Video_Uploads", file.filename))
        redirect('/')
        return render_template("base.html", message="Video Successfully Uploaded...")
    return render_template("base.html", message="Upload a Video...")


def extractKeyFrame():
    global fileName
    vd = Video()
    vd.extract_video_keyframes(
        no_of_frames=no_of_frames_to_return, file_path="Video_Uploads/" + fileName,
        writer=KeyFrameDiskWriter(location="KeyFrames")
    )
    print("KeyFrames Extracted Successfully...")


@app.route('/keyframe')
def keyframe():
    extractKeyFrame()
    results = {'processed': 'True'}
    return jsonify(results)
    # Show KeyFrames Extracted Successfully... message


if __name__ == "__main__":
    app.run("localhost", 1000, debug=True)
