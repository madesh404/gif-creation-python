import imageio.v3 as iio
import os

folder1 = "GIF Python"
folder2 = "Nyan_Cat_Frames"   # <-- put your folder name here

filenames = [os.path.join(folder1, folder2, f"nyan-cat{i}.png") 
             for i in range(1,4)]     # Adjust range as per number of frames

images = [iio.imread(filename) for filename in filenames]

iio.imwrite("nyan_cat.gif", images, duration=1, loop=0)
print("GIF created successfully.")
