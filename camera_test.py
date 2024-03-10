import cv2


def take_picture():
    # Open the camera
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Capture a frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not capture frame.")
        cap.release()
        return

    # Display the frame
    cv2.imshow("Camera", frame)

    # Save the frame as an image
    cv2.imwrite("captured_image.jpg", frame)

    # Release the camera
    cap.release()

    # Close OpenCV windows
    cv2.destroyAllWindows()


def display_picture(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Display the image
    cv2.imshow("Captured Image", image)
    cv2.waitKey(0)  # Wait for any key to be pressed
    cv2.destroyAllWindows()


if __name__ == "__main__":
    take_picture()
    display_picture("captured_image.jpg")
