"""Module that creates a qr code from some sort of data."""
import qrcode

def create_qr_code_img(data: str):
    """Generate QR Code

	Args:
		data (str): data which is being put into a QR code
	"""

    qr = qrcode.QRCode(
		version=1,
		box_size=10,
		border=5
	)
    qr.add_data(data)
    qr.make(fit=True)
    return qr.make_image(fill="black", back_color="white")
