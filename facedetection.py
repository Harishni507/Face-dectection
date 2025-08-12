import cv2
import pyttsx3

# Initialize the webcam
cap = cv2.VideoCapture(0)  # 0 corresponds to the default camera

# Initialize text-to-speech engine
engine = pyttsx3.init()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    print("ret:", ret)  # Debugging print statement
    print("frame shape:", frame.shape)  # Debugging print statement

    if not ret:
        print("Error: Frame not captured")
        break

    # Convert the frame to grayscale for better performance
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Dummy distance estimation (replace with your real calculation)
    # Example: Let's assume distance is 1.2 meters
    distance_m = 1.2  

    # Convert distance to speech
    speech_text = f"The human is approximately {distance_m} meters away"
    print(speech_text)  # Also print for debugging
    engine.say(speech_text)
    engine.runAndWait()

    # Display the video
    cv2.imshow("Webcam", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
