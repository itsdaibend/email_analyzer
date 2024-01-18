# Extract Emails from Image

This script utilizes the OpenCV and Tesseract OCR libraries to extract email addresses from an image. It provides two different methods for text extraction and selects the one with the highest response.

## Prerequisites
- Python 3.10
- `python3 -m venv env`
- `source env/bin/activate`
- `pip install -r requirements.txt`
- Tesseract OCR installed on your machine. You can download it [here](https://github.com/tesseract-ocr/tesseract).

## Usage

1. Ensure you have the required libraries installed.
2. Ensure you have a photo to extract emails.
3. Download and install Tesseract OCR.
4. Run the script with the following command:

```bash
python script.py --input <path/to/image.jpg> --output <output_file_name.txt>
```

- --input or -i: Path to the input image.
- --output or -o: Path to the output text file (default is "output.txt").

## Note

- The script uses two methods for text extraction: threshold cut and resized image. It selects the one with the highest response to maximize email address extraction.
- Extracted email addresses are written to the output file in a simple text format, with each email on a new line.
- All the code is covered by unittests.
