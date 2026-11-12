# 🖼️ Image Text Steganography with Python

<p align="center">
  <strong>Hide a text message inside an image using Python and Pillow.</strong>
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white">
  <img alt="Pillow" src="https://img.shields.io/badge/Library-Pillow-purple">
  <img alt="Project" src="https://img.shields.io/badge/Project-Learning%20Project-orange">
</p>

## 📌 Overview

**Image Text Steganography** is a small Python project that demonstrates how a text message can be hidden inside an image by modifying selected pixel color values. The project includes two scripts:

- `encode.py` — asks for a message and embeds its character values into an image.
- `decode.py` — reads the generated image and reconstructs the hidden message.

The project uses [Pillow](https://python-pillow.org/), Python's image-processing library, to open images, read pixel values, update pixels, and save the encoded result.

> **Important:** This project demonstrates basic *steganography* (hiding information), not secure encryption. The message is not protected by a cryptographic key, and someone who knows the encoding method may be able to recover it.

## ✨ Features

- Embed a text message into an image by modifying pixel data.
- Extract the hidden message with a separate decoding script.
- Use Python's built-in `ord()` and `chr()` functions to convert between characters and numeric character codes.
- Preserve the green and blue channels of the pixels currently used to store message characters; the red channel carries the message data.
- Save the encoded image as a PNG file.
- Keep encoding and decoding in separate, easy-to-understand scripts.

## 🧰 Technologies

- **Python 3**
- **Pillow** (`PIL`) for image processing

## 📁 Project Structure

```text
image_encryption/
├── encode.py             # Writes a message into the image
├── decode.py             # Reads the hidden message from the encoded image
├── ramz_aks.jpg          # Original image used for encoding
└── ramz_aks_encode.png   # Generated image containing the message
```

`ramz_aks_encode.png` is created when you run `encode.py`. Depending on your workflow, you may choose to commit the generated file to the repository or generate it locally when needed.

## ⚙️ Installation

### 1. Install Python

Install Python 3 from [python.org](https://www.python.org/downloads/) if it is not already installed.

### 2. Get the project

Clone the repository, or download it and extract the project folder. Then open a terminal in the `image_encryption` directory.

```bash
git clone <your-repository-url>
cd image_encryption
```

Replace `<your-repository-url>` with the URL of your GitHub repository. If you downloaded the project as a ZIP file, just navigate to the extracted folder instead.

### 3. Install the dependency

```bash
python -m pip install Pillow
```

If your system uses `python3` to run Python, use:

```bash
python3 -m pip install Pillow
```

## 🚀 Usage

### Encode a message

1. Make sure `ramz_aks.jpg` is present in the project directory.
2. Run the encoder:

   ```bash
   python encode.py
   ```

3. When prompted, enter the text you want to hide:

   ```text
   enter the text:
   ```

4. After the script finishes, it saves the result as `ramz_aks_encode.png`.

**Keep the generated PNG file.** The decoder reads this file, not the original JPG.

### Decode the message

Run:

```bash
python decode.py
```

The decoder opens `ramz_aks_encode.png`, reads the selected pixels in the same order used by the encoder, and prints the recovered text to the terminal.

### Typical workflow

```text
Original image + input text
            │
            ▼
       encode.py
            │
            ▼
  ramz_aks_encode.png
            │
            ▼
       decode.py
            │
            ▼
     Recovered message
```

## 🔍 How It Works

The current implementation uses a simple, custom pixel-based method:

1. **Open the source image.** Pillow loads `ramz_aks.jpg`.
2. **Visit selected pixels.** Both scripts step through the image in increments of five pixels along each dimension. They therefore use only pixels at those sampled coordinates, rather than every pixel in the image.
3. **Convert characters to numbers.** `ord(character)` returns the numeric code for a character.
4. **Store the code.** The encoder puts that value into the red channel of a selected pixel while leaving the pixel's green and blue channel values unchanged.
5. **Mark the end.** After the message has been written, the encoder sets the red channel of the next selected pixel to `0`. The decoder treats a red-channel value of `0` as the end-of-message marker.
6. **Recover the text.** The decoder reads the red-channel values in the same sampling order and converts them back into characters with `chr()`.
7. **Save as PNG.** The encoded image is saved as `ramz_aks_encode.png`. PNG is a lossless format, which is important because the decoder depends on exact pixel values.

### Why PNG matters

The encoder writes message data directly into pixel values. A lossy format such as JPEG can alter those values when an image is saved, potentially corrupting the message. For that reason, the generated image is saved as PNG and should not be converted to JPEG or passed through a service that recompresses or edits it before decoding.

## ⚠️ Current Limitations

This is an educational project, so the current implementation has some important limitations:

- **Not cryptographically secure:** The message is hidden, not encrypted. There is no password or encryption key.
- **Character-range limitation:** RGB channel values must be in the range `0`–`255`. Because the code stores `ord(character)` directly in one channel, it does not reliably support all Unicode text, including many Persian characters and emoji.
- **Limited capacity:** Only the sampled pixels can carry data. The code does not currently check whether the message fits in the image, so an overlong message may not be stored completely.
- **End marker:** A red-channel value of `0` is used as the end marker. The decoder stops at the first sampled pixel with that value.
- **Fixed file names:** The scripts expect the image files to have the names used in the code. Renaming or moving them requires updating the file paths.
- **No validation or error handling:** The scripts do not yet provide friendly messages for missing files, unsupported input, or insufficient image capacity.
- **No visual integrity guarantee:** Although the project changes only selected red-channel values, those edits may be visible in some cases. The method is not designed to guarantee imperceptibility.

## 🛣️ Possible Improvements

Potential next steps for the project include:

- Add support for Persian and other Unicode text by encoding messages as UTF-8 bytes.
- Store the message length or use a more robust terminator scheme.
- Check the image's available capacity and reject messages that are too long.
- Allow users to select the source image and output path.
- Add input validation and clear error messages.
- Add automated tests for encoding and decoding.
- Add optional real encryption (for example, a well-established authenticated encryption library) before hiding the message.
- Explore least-significant-bit (LSB) steganography to make pixel changes less noticeable.

## 🔐 Security Note

Do not use the current implementation to store passwords, confidential personal information, or other sensitive data. Anyone who discovers the method may be able to read the message, and the method does not authenticate the message or prevent tampering. For genuine confidentiality, use established encryption in addition to any steganography technique.

## 🎓 What I Practiced

This project is a hands-on exercise in:

- Reading and writing image files with Pillow.
- Accessing and modifying RGB pixel values.
- Nested loops and controlling iteration with `break`.
- Converting characters to numeric codes with `ord()` and back with `chr()`.
- Separating functionality into encoder and decoder scripts.
- Understanding the difference between steganography and cryptographic encryption.

## 🤝 Contributing

Suggestions and improvements are welcome. You can fork the repository, make changes on a separate branch, and open a pull request describing your improvements.

## 📄 License

No license has been specified yet. Unless a license is added to the repository, others should not assume they have permission to reuse, modify, or redistribute the project. Consider adding an open-source license if you want to allow reuse.

---

<p align="center">
  Made with Python 🐍 and curiosity.
</p>
