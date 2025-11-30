from PIL import Image
import os

folder1 = "GIF Python"
folder2 = "Cat_GIF_Frames"
output_folder = "cat_png_frames"
os.makedirs(output_folder, exist_ok=True)

for i in range(54):
    gif_path = os.path.join(folder1, folder2, f"frame_{i:02d}_delay-0.06s.gif")
    img = Image.open(gif_path)

    # Extract only the first frame
    img.seek(0)

    png_path = os.path.join(output_folder, f"frame_{i:02d}.png")
    img.save(png_path)

print("All frames converted to PNG!")
