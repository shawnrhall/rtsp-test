import cv2

def save_rtsp_stream(rtsp_url, output_file):
    # Create a VideoCapture object to connect to the RTSP stream
    cap = cv2.VideoCapture(rtsp_url)

    # Check if the connection was successful
    if not cap.isOpened():
        print("Failed to open RTSP stream:", rtsp_url)
        return

    # Get the video's frame width, height, and frames per second
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Create a VideoWriter object to save the stream to a file
    fourcc = cv2.VideoWriter_fourcc(*"XVID")  # Codec used for the output file
    out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

    while True:
        # Read the next frame from the RTSP stream
        ret, frame = cap.read()

        if not ret:
            # End of the stream
            break

        # Write the frame to the output file
        out.write(frame)

        # Display the frame (optional)
        cv2.imshow("RTSP Stream", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            # Quit if 'q' is pressed
            break

    # Release the VideoCapture and VideoWriter objects
    cap.release()
    out.release()

    # Close any open windows
    cv2.destroyAllWindows()

# Example usage
#rtsp_url = "rtsp://admin:aria1104@192.168.1.174:554/cam/realmonitor?channel=1&subtype=0"  # Replace with your RTSP stream URL
rtsp_url = "rtsp://admin:M&WCamera3@10.0.2.24:554/media/video2"
#

output_file = "output.avi"  # Replace with your desired output file path
save_rtsp_stream(rtsp_url, output_file)

