# photo_transfer.py
import os
import argparse
import torch
from PIL import Image
from torchvision import transforms
from photo_wct import PhotoWCT
from function import preserve_color, coral
import cv2

def load_image(img_path):
    image = Image.open(img_path).convert("RGB")
    transform = transforms.ToTensor()
    image = transform(image).unsqueeze(0)
    return image

def save_image(tensor, path):
    image = tensor.squeeze(0).clamp(0, 1).numpy().transpose(1, 2, 0) * 255
    image = image.astype("uint8")
    cv2.imwrite(path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

def run_style_transfer(content_path, style_path, output_path, preserve=False, alpha=1.0):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = PhotoWCT()
    model.load_state_dict(torch.load('./PhotoWCTModels/photo_wct.pth'))
    model = model.to(device)
    model.eval()

    content_img = load_image(content_path).to(device)
    style_img = load_image(style_path).to(device)

    if preserve:
        style_img = preserve_color(style_img, content_img)

    with torch.no_grad():
        stylized_img = model.transform(content_img, style_img, None, None)
        if alpha < 1.0:
            stylized_img = alpha * stylized_img + (1 - alpha) * content_img

    save_image(stylized_img.cpu(), output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--content', type=str, required=True, help='콘텐츠 이미지 경로')
    parser.add_argument('--style', type=str, required=True, help='스타일 이미지 경로')
    parser.add_argument('--output', type=str, required=True, help='결과 저장 경로')
    parser.add_argument('--preserve_color', action='store_true', help='색상 보존 여부')
    parser.add_argument('--alpha', type=float, default=1.0, help='스타일 강도 (0~1)')
    args = parser.parse_args()

    run_style_transfer(
        args.content,
        args.style,
        args.output,
        preserve=args.preserve_color
    )
