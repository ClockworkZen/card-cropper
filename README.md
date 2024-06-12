# Magic the Gathering Card Image Cropper

This utility trims white space from around Magic the Gathering card images and processes an entire folder of images at a time.

## Prerequisites

- Python 3.x
- OpenCV library

To install OpenCV, run:

`pip install opencv-python`

### Folder Structure
Place the script in a directory with the following structure:
```
your_directory/
│
├── Input/
│   ├── image1.jpg
│   ├── image2.png
│   └── ...
│
├── Output/
│   └── (cropped images will be saved here)
│
└── card_cropper.py

Input/: Directory containing the images you want to process.
Output/: Directory where the cropped images will be saved.
card_cropper.py: The script file.
```

### Usage
Place your images in the Input folder.
Run the script:

`python card_cropper.py`

Check the Output folder for the processed images.

### Contribution
Feel free to contribute to this project by creating pull requests or submitting issues.

### License
This project is licensed under the MIT License.
