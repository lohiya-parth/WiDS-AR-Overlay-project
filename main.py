import cv2
import numpy as np
from PIL import Image

# -------------------------------
# Function: Load image using Pillow
# -------------------------------
def load_image_pillow(image_path):
    image = Image.open(image_path)
    print("Image loaded using Pillow")
    return image

# -----------------------------------------
# Function: Convert Pillow image to OpenCV
# -----------------------------------------
def pillow_to_opencv(pil_image):
    numpy_image = np.array(pil_image)
    print("Converted to NumPy array")
    return numpy_image

# -----------------------------------------
# Image Operations
# -----------------------------------------
def rgb_to_bgr(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

def resize_image(image, width, height):
    return cv2.resize(image, (width, height))

def sharpen_image(image):
    kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])
    return cv2.filter2D(image, -1, kernel)

# -----------------------------------------
# Main Program
# -----------------------------------------
def main():
    image_path = input("Enter image path: ")
    pil_image = load_image_pillow(image_path)

    # Convert to OpenCV format
    cv_image = pillow_to_opencv(pil_image)

    print("\nChoose an operation:")
    print("1. Convert RGB to BGR")
    print("2. Resize Image")
    print("3. Sharpen Image")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        output_image = rgb_to_bgr(cv_image)

    elif choice == 2:
        width = int(input("Enter new width: "))
        height = int(input("Enter new height: "))
        output_image = resize_image(cv_image, width, height)

    elif choice == 3:
        output_image = sharpen_image(cv_image)

    else:
        print("Invalid choice")
        return

    # Display image
    cv2.imshow("Final Output", output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save result
    cv2.imwrite("output_image.jpg", output_image)
    print("Final image saved as output_image.jpg")

if __name__ == "__main__":
    main()
