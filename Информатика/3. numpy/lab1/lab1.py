from PIL import Image
import numpy as np

file_path = 'lunar_images/lunar03_raw.jpg'
# считаем картинку в numpy array
img = Image.open(file_path)
data = np.array(img)
min, max = data.min(), data.max()
print(min, max)
# ... логика обработки
'''
updated_data = data
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        delta = data[i][j] - min
        d = delta * 255 / (int(max) - int(min))
        updated_data[i][j] = d
'''
#(data - int(min)) * 255 / (int(max) - int(min))
c = 255 / (max - min)
data = (data - min) * 255.0 / (max - min)
#print(updated_data.astype(np.uint8).max(), updated_data.astype(np.uint8).min())
# запись картинки после обработки
res_img = Image.fromarray(data.astype(np.uint8))
new_file_path = 'lunar_images/lunar03_new.jpg'
res_img.save(new_file_path)
