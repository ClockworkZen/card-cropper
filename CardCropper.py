import os
import cv2
import numpy as np

def trim_whitespace(image_path):
    try:
        # Load the image
        image = cv2.imread(image_path)
        if image is None:
            print(f"Error loading image {image_path}")
            return None
        
        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Apply adaptive thresholding to create a binary image
        binary_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
        
        # Use morphology operations to remove small noise
        kernel = np.ones((5, 5), np.uint8)
        cleaned_binary_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)
        
        # Find contours in the binary image
        contours, _ = cv2.findContours(cleaned_binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        if contours:
            # Debugging: Print the number of contours found
            print(f"{len(contours)} contours found in {image_path}")
            
            # Get the bounding box of the largest contour
            largest_contour = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(largest_contour)
            
            # Debugging: Print the bounding box coordinates
            print(f"Bounding box for {image_path}: x={x}, y={y}, w={w}, h={h}")
            
            # Crop the image to the bounding box
            trimmed_image = image[y:y+h, x:x+w]
            return trimmed_image
        else:
            print(f"No contours found in {image_path}")
            return image
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return None

def process_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".jpg") or filename.lower().endswith(".png"):
            image_path = os.path.join(input_folder, filename)
            trimmed_image = trim_whitespace(image_path)

            if trimmed_image is not None:
                output_path = os.path.join(output_folder, filename)
                # Save the trimmed image to the output folder
                cv2.imwrite(output_path, trimmed_image)
                print(f"{filename}: processed")
            else:
                print(f"{filename}: error")

# Define the folder paths
script_directory = os.path.dirname(os.path.abspath(__file__))
input_folder = os.path.join(script_directory, "Input")
output_folder = os.path.join(script_directory, "Output")

process_folder(input_folder, output_folder)
