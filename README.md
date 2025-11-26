# Create a GIF with Python

This project follows the Codedex tutorial for creating an animated GIF using Python. The goal of the project is to extract individual frames from a GIF and then reassemble them using Python.

## 📦 Requirements

To run this project, you need the following installed:

* **Python 3.10+** (Python 3.13 recommended)
* **pip** (comes with Python)
* **imageio** library
* **Pillow** library (only needed if converting formats)

You can install the dependencies with:

```bash
pip install imageio pillow
```

## 📂 Project Structure

```
GIF Python/
├── frames/           # Folder containing extracted PNG frames
├── create_gif.py     # Python script that generates the GIF
└── README.md          # This file
```

## 📝 How to Extract Frames from a GIF

If you want to manually get still images from a GIF (e.g., from Tenor):

1. Download the GIF from Tenor.
2. Use an online GIF frame extractor such as:

   * ezgif.com/split
   * gif-extract.com
3. Download all extracted frames as PNG files.
4. Place all frames into the `frames/` directory.

Make sure the frames are named sequentially, such as:

```
frame_0.png
frame_1.png
frame_2.png
...
```

## ▶️ Running the Script

Run the script using:

```bash
python create_gif.py
```

This will produce an `output.gif` file in the project folder.

## ❗ Common Errors

### **TypeError: Cannot handle this data type**

This error appears when your frames are **still GIF frames**, not PNG/JPG.
Convert all frames to PNG before running the script.

## 📜 License

MIT License. Free to use for learning or projects.

---
