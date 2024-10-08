from pdf2image import convert_from_path
from pytesseract import image_to_string
from PIL import Image
import os


def convert_pdf_to_img(pdf_file):
    """Converts PDF into images."""
    return convert_from_path(pdf_file)


def convert_image_to_text(file):
    """Extracts text from a single image."""
    text = image_to_string(file)
    return text


def is_image(file_path):
    """Checks if the file is an image based on its extension."""
    image_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.tiff']
    return os.path.splitext(file_path)[1].lower() in image_extensions


def get_text_from_any_file(file_path):
    """Extracts text from either a PDF or an image file."""
    final_text = ""

    if file_path.lower().endswith('.pdf'):
        # Process PDF
        images = convert_pdf_to_img(file_path)
        for pg, img in enumerate(images):
            final_text += convert_image_to_text(img)
    elif is_image(file_path):
        # Process image
        img = Image.open(file_path)
        final_text = convert_image_to_text(img)
    else:
        raise ValueError("Unsupported file type. Please provide a PDF or an image.")

    return final_text


def print_lines_with_keyword(text, keyword, position):
    """Prints only lines containing the keyword (case-insensitive)."""
    lines = text.splitlines()
    for line in lines:
        if (position == "begin") and (line.strip().lower().startswith(keyword.lower())):
            print(line)
        elif (position == "end") and (line.strip().lower().endswith(keyword.lower())):
            print(line)
        elif (position == "middle") and (keyword.lower() in line.lower()):
            print(line)


# Example usage for PDF and image
path_to_pdf = 'AAOS4461592-100824_2662 (3).pdf'
path_to_image = 'Screenshot 2024-10-07 at 16.56.46.png'

# Get text from PDF or image
extracted_text = get_text_from_any_file(path_to_pdf)  # You can replace with path_to_image

# Print lines containing the word 'What'
print_lines_with_keyword(extracted_text, 'LDL CHOLESTEROL','middle')
