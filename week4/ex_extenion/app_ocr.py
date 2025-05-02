from flask import Flask, request, jsonify
from PIL import  Image
from io import BytesIO
import base64
import easyocr
import numpy as np


app = Flask(__name__)
reader = easyocr.Reader(['ko','en'])

@app.route('/upload',methods=['POST'])
def upload_ocr():
    data = request.json['image']
    image_date = base64.b64encode(data.splist(',')[1])
    image = Image.open(BytesIO(image_date)).convert('RGB')
    image_np = np.array(image)
    result = reader.readtext(image_np, detail=0) # 텍스트만
    return jsonify({'result':' '.join(result)})

if __name__ == '__main__':
    app.run(debug=True)