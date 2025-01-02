import sys
import base64
import qrcode
import urllib.parse
import os

# Change this if you want to use decoding file hosted elsewhere
WEB_URL_PREFIX = "https://amanraox.github.io/share-bits-wirelessly/dl.html"

def validate_file(input_filename):
    """Check if the input file exists and is a valid file."""
    if not os.path.isfile(input_filename):
        raise FileNotFoundError(f"The file {input_filename} does not exist.")
    
def encode_file(input_filename):
    """Encode the file to base64."""
    with open(input_filename, "rb") as f:
        file_data = f.read()
    return base64.b64encode(file_data).decode('ascii')

def generate_qr_code(url, output_filename):
    """Generate QR code and save it."""
    qr_img = qrcode.make(url)
    qr_img.save(f"{output_filename}_qr.png")
    print(f"QR code saved as {output_filename}_qr.png")

def main():
    if len(sys.argv) > 1:
        input_filename = sys.argv[1]
        output_filename = input_filename if len(sys.argv) == 2 else sys.argv[2]
    else:
        print("Usage: python generate_qr.py inputfile [optional output filename]")
        exit(-1)

    try:
        # Validate input file existence
        validate_file(input_filename)

        # Encode file content to base64
        b64_file_data = encode_file(input_filename)
        
        # URL encode the base64 file data
        url_file_data = urllib.parse.quote_plus(b64_file_data)
        
        # Generate the full URL
        full_url = f"{WEB_URL_PREFIX}?f={output_filename}#{url_file_data}"
        print("Encoded URL:", full_url)
        
        # Generate QR code and save it
        generate_qr_code(full_url, output_filename)
        
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
