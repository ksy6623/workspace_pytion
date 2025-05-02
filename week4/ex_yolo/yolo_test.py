from ultralytics import YOLO
import matplotlib.pyplot as plt

model = YOLO('best.pt')
results = model('./b7(P).jpg',save=True)
detected_image = results[0].plot()
print(results[0].boxes)
plt.imshow(detected_image)
plt.show()