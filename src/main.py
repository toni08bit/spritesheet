import os
import math
import logging
import re
import PIL.Image

# === LOGGING CONFIG ===
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler()]
)

# === CONFIG ===
INPUT_FOLDER = "input"
OUTPUT_FILE = "spritesheet.png"
PADDING = 2


def natural_sort_key(s):
    # Natural sorting (e.g., img2.png before img10.png)
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def get_image_files(folder):
    logging.info(f'Scanning for images in "{folder}"...')
    supported_exts = (".png", ".jpg", ".jpeg", ".bmp", ".gif")
    files = [f for f in os.listdir(folder) if f.lower().endswith(supported_exts)]
    files.sort(key=natural_sort_key)
    logging.debug(f"Found files (natural sorted): {files}")
    return [os.path.join(folder, f) for f in files]

def load_images(filepaths):
    images = []
    for path in filepaths:
        try:
            img = PIL.Image.open(path).convert("RGBA")
            images.append(img)
            logging.info(f"Loaded image: {path} ({img.size[0]}x{img.size[1]})")
        except Exception as e:
            logging.error(f"Failed to load image {path}: {e}")
    return images

def create_spritesheet(images, padding):
    if not images:
        logging.error("No images to pack into spritesheet.")
        return None

    # Prepare grid
    num_images = len(images)
    grid_cols = math.ceil(math.sqrt(num_images))
    grid_rows = math.ceil(num_images / grid_cols)
    logging.info(f"Arranging {num_images} images in a grid: {grid_cols} columns x {grid_rows} rows")

    # Find max width and height for each cell
    cell_width = max(img.width for img in images)
    cell_height = max(img.height for img in images)
    logging.debug(f"Cell size: {cell_width}x{cell_height}")

    sheet_width = grid_cols * cell_width + padding * (grid_cols - 1)
    sheet_height = grid_rows * cell_height + padding * (grid_rows - 1)
    logging.info(f"Creating spritesheet of size {sheet_width}x{sheet_height}...")

    spritesheet = PIL.Image.new('RGBA', (sheet_width, sheet_height), (0, 0, 0, 0))

    for idx, img in enumerate(images):
        row = idx // grid_cols
        col = idx % grid_cols
        x = col * (cell_width + padding)
        y = row * (cell_height + padding)
        logging.debug(f"Pasting image {idx} at ({x}, {y})")
        spritesheet.paste(img, (x, y))

    return spritesheet

def main():
    if not os.path.exists(INPUT_FOLDER):
        logging.error(f'Input folder "{INPUT_FOLDER}" does not exist.')
        return

    image_files = get_image_files(INPUT_FOLDER)
    if not image_files:
        logging.error("No image files found in the input folder.")
        return

    images = load_images(image_files)
    spritesheet = create_spritesheet(images, PADDING)
    if spritesheet:
        spritesheet.save(OUTPUT_FILE)
        logging.info(f"Spritesheet saved as '{OUTPUT_FILE}'.")

if __name__ == "__main__":
    main()
