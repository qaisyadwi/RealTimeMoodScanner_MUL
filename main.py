import cvzone
import pickle
from cvzone.FaceMeshModule import FaceMeshDetector
import cv2
import numpy as np
import mediapipe as mp

# Initialize webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Unable to access the webcam.")
    exit(1)

# Load face mesh detector
FMD = FaceMeshDetector()

# Load the behavior prediction model
try:
    with open('model.pkl', 'rb') as f:
        Behaviour_model = pickle.load(f)
except FileNotFoundError:
    print("Error: Behavior prediction model file 'model.pkl' not found.")
    exit(1)

# Initialize mediapipe segmentation
mp_selfie_segmentation = mp.solutions.selfie_segmentation
segment = mp_selfie_segmentation.SelfieSegmentation(model_selection=1)

# Background video paths
background_video_paths = {
    "sad": "marah.mp4",
    "happy": "senang.mp4",
    "shock": "kaget.mp4",
}

# Mapping of mood labels for display
mood_labels = {
    "sad": "sedih",
    "happy": "senang",
    "shock": "kaget",
}

# Function to initialize a video
def initialize_video(video_path):
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print(f"Error: Unable to open video '{video_path}'.")
        return None
    return video

# Load background videos
background_videos = {mood: initialize_video(path) for mood, path in background_video_paths.items()}
if None in background_videos.values():
    exit(1)

# Default background video
current_mood = "happy"
background_video = background_videos[current_mood]

# Processing video frames
while cap.isOpened():
    rt, frame = cap.read()
    if not rt:
        print("Error: Unable to read frame from webcam.")
        break

    frame = cv2.resize(frame, (720, 480))
    real_frame = frame.copy()

    # Read the next frame from the background video
    ret_bg, bg_frame = background_video.read()
    if not ret_bg:
        print(f"End of video for mood '{current_mood}', resetting...")
        background_video.release()  # Release the video
        background_video = initialize_video(background_video_paths[current_mood])  # Reinitialize the video
        ret_bg, bg_frame = background_video.read()
        if not ret_bg:
            print(f"Error: Unable to reset and read video for mood '{current_mood}'.")
            bg_frame = np.zeros_like(frame)  # Fallback to a black background

    bg_frame = cv2.resize(bg_frame, (720, 480))

    # Use mediapipe for segmentation
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = segment.process(frame_rgb)

    # Create a mask for the background
    mask = results.segmentation_mask
    condition = mask > 0.5  # Threshold to distinguish background and foreground

    # Replace the background
    output_frame = np.where(condition[..., None], frame, bg_frame)

    # Face Mesh Processing
    img, faces = FMD.findFaceMesh(output_frame)
    cvzone.putTextRect(output_frame, 'Mood', (10, 80))
    if faces:
        face = faces[0]
        face_data = list(np.array(face).flatten())

        try:
            # Predict behavior
            result = Behaviour_model.predict([face_data])
            mood = result[0]

            # Map mood to translated label for display
            display_mood = mood_labels.get(mood, mood)  # Fallback to raw mood if not in mapping
            cvzone.putTextRect(output_frame, display_mood, (250, 80))
            print(f"Detected Mood: {display_mood}")

            # Change background video if mood changes
            if mood != current_mood:
                if mood in background_video_paths:
                    print(f"Detected mood change: {current_mood} -> {mood}")
                    current_mood = mood
                    background_video.release()  # Release the current video
                    background_video = initialize_video(background_video_paths[current_mood])  # Reinitialize
                    print(f"Background video changed to '{current_mood}'.")

        except Exception as e:
            print("Error during behavior prediction:", e)

    # Display the output
    all_frames = cvzone.stackImages([real_frame, output_frame], 2, 0.70)
    cv2.imshow('frame', all_frames)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
for video in background_videos.values():
    if video:
        video.release()
cv2.destroyAllWindows()
