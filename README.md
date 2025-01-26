# share bits wirelessly


![ss](/asset/Screenshot_2024-05-28_21-33-01.jpg)
## Try this💡
### Here is my simple solution for sharing really small files. 

Share small files from an offline source using only a QR code!

## Why?

Imagine: You want to share a file with a friend nearby. You want to share from a source that does not have internet access - you just want to beam the file directly to your friend. This system lets you _embed_ your file into a QR code that loads as an actual file download on your friend's device. Try it out here if you're feeling brave! The image that is downloaded by scanning this QR code **is not hosted on any server, it only lives _inside_ the QR code**.

![QR code with file embedded](/asset/thumb14.jpg)

## How it works

1. **Generate a QR Code**
  - Embed a small file into a QR code.
  - use the [web app](https://amanraox.github.io/share-bits-wirelessly/) or the provided Python script.

2. **Share and Scan**
  - Show the generated QR code to the recipient.
  - They scan it using any standard QR code scanner capable of handling embedded data (e.g., a smartphone camera or QR reader app).
  - The file downloads directly to their device.

## Usage

### Option 1 : Web App
1. Visit the [web app](https://amanraox.github.io/share-bits-wirelessly/).
2. Upload a file and download the QR code.
3. Share the QR code with others.

### Option 2 : Python Script
1. Clone the repository.
2. Install dependencies: 
```bash
  pip install -r requirements.txt
```
3. Generate a QR Code:
```bash
  python3 generate_pr.py input_file.txt
```
- The QR code is saved as `input_file.txt.png` (or provide an alternate output name as the second argument).

## Clarification: QR System

The process for generating a QR code is clear. However, for retrieving files, note the following:

1. Use any QR code scanner or a smartphone camera to scan the code.
2. Ensure the QR reader supports **embedded data decoding**, as the file resides entirely within the QR code.
3. Once scanned, the QR reader will automatically prompt the download of the embedded file.

If additional steps are needed, or you face issues, feel free to raise a question or open an issue in the repository!

## CONTRIBUTING 

We welcome contributions to SHare Bits Wirelessly! To contribute:

1. Fork and Star the repository 🍴⭐
2. Create a new branch 🌱
```bash
  git checkout -b feature/your-feature
```
3. Make your changes ✨
```bash
  git commit -m "Add your message"
```
4. Push your changes 🚀
5. Create a pull request 🔄

## Contributors

A heartfelt thank you to the following individuals for their valuable contributions to this project. Your support and dedication are greatly appreciated:

<a href="https://github.com/amanraox/share-bits-wirelessly/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=amanraox/share-bits-wirelessly" />
</a>

<br>
