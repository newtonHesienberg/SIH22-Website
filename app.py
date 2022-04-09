from flask import Flask, render_template, request
import os

from Katna.video import Video
from Katna.writer import KeyFrameDiskWriter

app = Flask(__name__)

no_of_frames_to_return = 10
diskwriter = KeyFrameDiskWriter(location="KeyFrames")


@app.route('/', methods=["GET", "POST"])
def Hello():
    if request.method == 'POST':
        file = request.files["file"]
        file.save(os.path.join("Video_Uploads", file.filename))
        vd.extract_video_keyframes(
            no_of_frames=no_of_frames_to_return, file_path= "Video_Uploads/" + file.filename,
            writer=diskwriter
        )
        
        return render_template("base.html", message="Success")
    return render_template("base.html", message="Upload")


if __name__ == "__main__":
    vd = Video()
    app.run("localhost", 1000, debug=True)
