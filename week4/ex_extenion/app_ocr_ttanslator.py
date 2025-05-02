import io

from flask import Flask, request, jsonify
from PIL import  Image
from io import BytesIO
import base64
import easyocr
import numpy as np
from flask_cors import CORS
from python_flask.flask_youtube import grok_tranlator
app = Flask(__name__)
CORS(app)
reader = easyocr.Reader(['ko','en'])
@app.route('/upload',methods=['POST'])
def upload_ocr():
    if 'image' not in request.files:
        return jsonify({"error":"no image file provided"}),400
    image_file = request.files['image'].read()
    image = Image.open(io.BytesIO(image_file))
    image_np = np.array(image)
    result = reader.readtext(image_np, detail=0)
    if result :
        text = ' '.join(result)
        trans = grok_tranlator_en_to_ko(text)
        # 번역
        trans = text
    else:
        trans = "번역 가능 텍스트 없음"
    return jsonify({'translation':trans})
    # return jsonify({'result':' '.join(result)})

if __name__ == '__main__':
    app.run(debug=True)