from PIL import Image
import os
source_dir = r"D:\аип\lab 11\11.2\jpgs and others"
target_dir = r"D:\аип\lab 11\11.2\processed"
if not os.path.exists(target_dir):
    os.makedirs(target_dir)
for filename in os.listdir(source_dir):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        full_path = os.path.join(source_dir, filename)
        with Image.open(full_path) as img:
            processed_img = img.transpose(Image.FLIP_TOP_BOTTOM)
            output_path = os.path.join(target_dir, filename)
            processed_img.save(output_path)

print("Обработка завершена!")
