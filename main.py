"""Main file for a python qr code generator."""
import os.path

from qrcodegenerator import create_qr_code_img
from config import Config

def main():
    """Main funtion for a python qr code generator"""
    full_path = os.getcwd()

    directory_path_and_filename = os.path.join(full_path,
                                               Config.QR_CODE_IMAGE_DIRECTORY,
                                               Config.QR_CODE_DEFAULT_FILENAME)

    qr_image = create_qr_code_img(Config.QR_CODE_DEFAULT_URL)

    for _ in range(0,1):
        while True:
            try:
                qr_image.save(directory_path_and_filename)
            except FileNotFoundError:
                current_working_directory = os.getcwd()
                qr_image_directory = Config.QR_CODE_IMAGE_DIRECTORY
                new_directory_path = os.path.join(
					current_working_directory,
     				qr_image_directory
				)
                os.mkdir(new_directory_path)
            break

if __name__ == "__main__":
    main()
