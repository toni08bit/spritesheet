# 🖼️ spritesheet

A simple Python tool to generate a spritesheet from a folder of images!  
Supports `.png`, `.jpg`, `.jpeg`, `.bmp`, and `.gif` files.  
Perfect for game developers, animators, and anyone who needs to pack multiple images into a single file.

## 🚀 Features

- 📂 **Batch process**: Drop your images into the `src/input/` folder and run!
- 🧩 **Automatic grid**: Arranges images in a compact grid.
- 🏷️ **Natural sorting**: Keeps your frames in the right order (e.g., `img2.png` before `img10.png`).
- 🖼️ **Mixed formats**: Handles different image sizes and formats.
- 🛡️ **Transparent background**: Output is a PNG with transparency.

## 🛠️ Usage

1. **Install dependencies**  
   ```
   pip install -r requirements.txt
   ```

2. **Add your images**  
   Place your images in the `src/input/` directory.

3. **Run the script**  
   ```
   python src/main.py
   ```

4. **Get your spritesheet**  
   The output file `spritesheet.png` will be created in the project root.

## 📁 Directory Structure

```
spritesheet/
├── src/
│   ├── main.py
│   └── input/
│       └── (your images here)
├── requirements.txt
└── README.md
```

---
Made with ❤️ for pixel pushers!