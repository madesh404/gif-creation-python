import imageio.v3 as iio
import os

folder1 = "GIF Python"
folder2 = "cat_png_frames"   # <-- put your folder name here

filenames = [os.path.join(folder1, folder2, f"frame_{i:02d}.png") 
             for i in range(54)]     # Adjust range as per number of frames

images = [iio.imread(filename) for filename in filenames]

iio.imwrite("cat.gif", images, duration=1, loop=0)
print("GIF created successfully.")
