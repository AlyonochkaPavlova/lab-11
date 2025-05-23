from PIL import Image
import os
source_dir = r"D:\аип\lab 11\11.1\jpgs"
target_dir = r"D:\аип\lab 11\11.2\processed"
if not os.path.exists(target_dir):
    os.makedirs(target_dir)
for filename in os.listdir(source_dir):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        path_to_image = os.path.join(source_dir, filename)
        with Image.open(path_to_image) as img:
            flipped_img = img.transpose(Image.FLIP_TOP_BOTTOM)
            target_path = os.path.join(target_dir, filename)
            flipped_img.save(target_path)

print("Обработка завершена!")
