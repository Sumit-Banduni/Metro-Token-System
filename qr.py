import qrcode

# Read the file content
file_path = "metro.csv"

try:
    with open(file_path, "r") as file:
        data = file.read()  # Read the entire file content
except FileNotFoundError:
    print("File not found. Make sure the 'metro.csv' file exists.")
    exit()

# Generate QR Code
qr = qrcode.QRCode(
    version=5,  # Adjust the version based on data size
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Create and save the QR Code image
img = qr.make_image(fill="black", back_color="white")
img.save("metro_qr.png")

print("QR Code for the file has been generated and saved as 'metro_qr.png'.")
