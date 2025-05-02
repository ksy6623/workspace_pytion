import cv2
import numpy as np
import re

def auto_detect_card(image):
    # 이미지 복사 및 축소
    orig = image.copy()
    ratio = image.shape[0] / 500.0
    image = cv2.resize(image, (int(image.shape[1] / ratio), 500))

    # 그레이 변환, 블러, 에지
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 75, 200)

    # 윤곽선 탐지
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5]

    screenCnt = None
    for c in contours:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if len(approx) == 4:
            screenCnt = approx
            break

    if screenCnt is None:
        return None, False

    # 점 정렬
    pts = screenCnt.reshape(4, 2)
    rect = np.zeros((4, 2), dtype="float32")

    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    rect *= ratio

    # 투시 변환
    (tl, tr, br, bl) = rect
    widthA = np.linalg.norm(br - bl)
    widthB = np.linalg.norm(tr - tl)
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.linalg.norm(tr - br)
    heightB = np.linalg.norm(tl - bl)
    maxHeight = max(int(heightA), int(heightB))

    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")

    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(orig, M, (maxWidth, maxHeight))

    return warped, True


def extract_contact_info(text_lines):
    """
    OCR 결과에서 이메일, 전화번호, 이름 후보 추출
    """
    email_pattern = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
    phone_pattern = re.compile(r"(01[016789]|02|0[3-9][0-9])[-.\s]?[0-9]{3,4}[-.\s]?[0-9]{4}")
    name_candidates = []

    emails = []
    phones = []

    for line in text_lines:
        if email_pattern.search(line):
            emails.append(email_pattern.search(line).group())

        if phone_pattern.search(line):
            phones.append(phone_pattern.search(line).group())

        # 이름 후보: 한글 2~4자, 공백 없는 단어
        if re.fullmatch(r"[가-힣]{2,4}", line.strip()):
            name_candidates.append(line.strip())

    return {
        "emails": emails,
        "phones": phones,
        "names": name_candidates
    }

if __name__ == '__main__':
    import easyocr
    img_path = 'test_name.jpg'
    image = cv2.imread(img_path)
    warped_img, success = auto_detect_card(image)
    if success:
        print("명함 감지 및 보정")
        cv2.imwrite('re_business_card.jpg', warped_img)
    else: # 명함 감지 못함
        print("원본사용")
        warped_img = image

    reader = easyocr.Reader(['ko','en'])
    results = reader.readtext(warped_img)

    text_lines = [text for _, text, _ in results]
    print("추출된 텍스트 ")
    for line in text_lines:
        print("-", line)

    info = extract_contact_info(text_lines)
    print(info)

