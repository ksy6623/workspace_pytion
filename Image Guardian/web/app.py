from flask import Flask, request, render_template, send_from_directory, redirect, url_for
import os
from werkzeug.utils import secure_filename
from protect_images import protect_single_image

UPLOAD_FOLDER = 'uploads'
PROTECTED_FOLDER = 'uploads/protected'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROTECTED_FOLDER'] = PROTECTED_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROTECTED_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    protect_success = False
    results = []

    if request.method == 'POST':
        uploaded_files = request.files.getlist('images')

        for file in uploaded_files:
            if file and file.filename != '':
                filename = secure_filename(file.filename)
                original_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                protected_path = os.path.join(app.config['PROTECTED_FOLDER'], filename)

                file.save(original_path)
                protect_single_image(original_path, protected_path)

                results.append({
                    'original': url_for('uploaded_file', filename=filename),
                    'protected': url_for('protected_file', filename=filename)
                })

        protect_success = True

    return render_template('index.html', results=results, protect_success=protect_success)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/uploads/protected/<filename>')
def protected_file(filename):
    return send_from_directory(app.config['PROTECTED_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
