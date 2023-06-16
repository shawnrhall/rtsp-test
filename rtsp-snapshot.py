import cv2

def take_snapshot(rtsp_url, output_path):
    # Open the RTSP stream
    cap = cv2.VideoCapture(rtsp_url)

    # Check if the stream is opened successfully
    if not cap.isOpened():
        print("Failed to open RTSP stream")
        return

    # Read the next frame from the stream
    ret, frame = cap.read()

    # Check if a frame was successfully read
    if not ret:
        print("Failed to read frame from the RTSP stream")
        return

    # Save the frame as an image
    cv2.imwrite(output_path, frame)

    # Release the stream and close any open windows
    cap.release()
    cv2.destroyAllWindows()

# Example usage
rtsp_url = rtsp_url = "rtsp://admin:aria1104@192.168.1.174:554/cam/realmonitor?channel=1&subtype=0"   # Replace with your RTSP stream URL
output_path = "snapshot.jpg"  # Replace with your desired output path

take_snapshot(rtsp_url, output_path)
print("Snapshot saved successfully.")