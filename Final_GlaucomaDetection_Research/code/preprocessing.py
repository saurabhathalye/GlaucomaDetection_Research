
import cv2

def preprocess_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    equalized = cv2.equalizeHist(blurred)
    return equalized

if __name__ == "__main__":
    processed_image = preprocess_image("data/sample_image.jpg")
    cv2.imwrite("results/processed_image.jpg", processed_image)
