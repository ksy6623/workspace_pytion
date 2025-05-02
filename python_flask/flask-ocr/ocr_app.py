import os
import cv2
import easyocr
from flask import Flask, render_template, request
from ocr_util import auto_detect_card, extract_contact_info

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
reader = easyocr.Reader(['ko','en'])
from werkzeug.utils import secure_filename
@app.route("/",methods=["GET","POST"])
def index():
    info = {}
    result_text = ""
    upload_path = ""
    re_image_path = ""
    if request.method == "POST":
        file = request.files['image']
        filename = secure_filename(file.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'],filename)
        file.save(path) # static 경로에 이미지 저장
        img = cv2.imread(path)

        warped_img, success = auto_detect_card(img)
        if success:
            print("명함 감지 및 보정")
            re_name = "re_" + filename
            re_image_path = os.path.join(app.config['UPLOAD_FOLDER'], re_name)
            cv2.imwrite('re_business_card.jpg', warped_img)
        else:  # 명함 감지 못함
            print("원본사용")
            warped_img = img

        results = reader.readtext(warped_img)
        text_lines = [text for _, text in results]
        result_text = "\n".join(text_lines)
        print("추출된 텍스트")
        for line in text_lines:
            print("-", line)
        info = extract_contact_info(text_lines)
        upload_path = path

    return render_template("index.html" ,image_path=upload_path
                                        ,re_image_path=re_image_path
                                        ,result_text=result_text
                                        , info = info)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")