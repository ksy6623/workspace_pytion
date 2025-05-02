# app.py
import os
from flask import Flask, render_template, request, send_from_directory
from photo_transfer import run_style_transfer
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['RESULT_FOLDER'] = 'static/results'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULT_FOLDER'], exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        content_file = request.files["content"]
        style_file = request.files["style"]
        alpha = float(request.form.get("alpha", 1.0))

        if content_file and style_file:
            content_filename = secure_filename(content_file.filename)
            style_filename = secure_filename(style_file.filename)

            content_path = os.path.join(app.config['UPLOAD_FOLDER'], content_filename)
            style_path = os.path.join(app.config['UPLOAD_FOLDER'], style_filename)
            result_filename = f"result_{content_filename}"
            result_path = os.path.join(app.config['RESULT_FOLDER'], result_filename)

            content_file.save(content_path)
            style_file.save(style_path)

            run_style_transfer(
                content_path, style_path, result_path,
                preserve=False, alpha=alpha
            )

            return render_template("index.html", result_image=result_filename)

    return render_template("index.html", result_image=None)

@app.route('/static/results/<filename>')
def result_file(filename):
    return send_from_directory(app.config['RESULT_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)
