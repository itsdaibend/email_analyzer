import cv2
import pytesseract
import argparse
import re


class InputPathNotFoundError(ValueError):
    def __init__(self):
        super().__init__(
            f"CV2 returned a None object. Please, enter a valid path. "
            f"Use argument --input <path/to/file.txt>",
        )


def get_threshold_cut_text(img):
    """
    Returns a text, initially extracted by thershold cut.
    """
    try:
        if img is None:
            raise InputPathNotFoundError()
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    except cv2.error as e:
        raise InputPathNotFoundError() from e
    _, threshold_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(threshold_img)

    return text


def get_resized_text(img):
    """
    Returns text from the resized image.
    """
    img = cv2.resize(img, None, fx=2, fy=2)
    data = pytesseract.image_to_string(img)

    return data


def extract_emails_from_image(input_path, output_path):
    """
    Returns a file containing selected emails with the algorithm
    that returned the biggest amount of response data.
    """
    img = cv2.imread(input_path)

    threshold_cut_text, resized_text = get_threshold_cut_text(img), get_resized_text(
        img
    )

    # Select a text with the biggest response.
    selected_text = (
        threshold_cut_text
        if len(threshold_cut_text) > len(resized_text)
        else resized_text
    )

    emails = re.findall(
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", selected_text
    )

    with open(output_path, "w") as output_file:
        for email in emails:
            output_file.write(email + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract email addresses from an image."
    )
    parser.add_argument("--input", "-i", required=True, help="Path to the input image.")
    parser.add_argument(
        "--output", "-o", default="output.txt", help="Path to the output text file."
    )

    args = parser.parse_args()

    exit(extract_emails_from_image(args.input, args.output))
