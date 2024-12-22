import cv2
import mediapipe as mp
import numpy as np
import os

def detect_mood(landmarks, width, height):
    left_mouth = landmarks[57]
    right_mouth = landmarks[287]
    top_mouth = landmarks[13]
    bottom_mouth = landmarks[14]

    left_mouth_pos = (int(left_mouth.x * width), int(left_mouth.y * height))
    right_mouth_pos = (int(right_mouth.x * width), int(right_mouth.y * height))
    top_mouth_pos = (int(top_mouth.x * width), int(top_mouth.y * height))
    bottom_mouth_pos = (int(bottom_mouth.x * width), int(bottom_mouth.y * height))

    mouth_width = np.linalg.norm(np.array(left_mouth_pos) - np.array(right_mouth_pos))
    mouth_height = np.linalg.norm(np.array(top_mouth_pos) - np.array(bottom_mouth_pos))

    if mouth_height / mouth_width > 0.6:  # Mulut terbuka lebar
        return "kaget"
    elif mouth_width / height < 0.05:  # Mulut menyempit
        return "marah"
    else:
        return "senang"

def main():
    data_folder = "data"

    # Load video untuk setiap mood
    videos = {
        "marah": cv2.VideoCapture(os.path.join(data_folder, "marah.mp4")),
        "senang": cv2.VideoCapture(os.path.join(data_folder, "senang.mp4")),
        "kaget": cv2.VideoCapture(os.path.join(data_folder, "kaget.mp4")),
    }

    for mood, video in videos.items():
        if not video.isOpened():
            print(f"Video untuk mood '{mood}' tidak ditemukan atau gagal dibuka!")
            videos[mood] = None

    # Inisialisasi Mediapipe Face Mesh
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)

    # Inisialisasi background subtractor
    bg_subtractor = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=50, detectShadows=True)

    # Buka kamera
    cap = cv2.VideoCapture(0)
    current_mood = "senang"

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Kamera gagal menangkap frame.")
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = face_mesh.process(rgb_frame)
        mood = "senang"

        if result.multi_face_landmarks:
            for face_landmarks in result.multi_face_landmarks:
                height, width, _ = frame.shape
                mood = detect_mood(face_landmarks.landmark, width, height)

        # Terapkan background subtraction
        fg_mask = bg_subtractor.apply(frame)

        # Gunakan morfologi untuk membersihkan noise
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, kernel)

        # Buat area wajah tetap transparan
        fg_mask_inv = cv2.bitwise_not(fg_mask)
        face_region = cv2.bitwise_and(frame, frame, mask=fg_mask)
        
        # Tampilkan hasil background subtraction untuk debugging
        cv2.imshow("Foreground Mask", fg_mask)

        # Fallback jika mood tidak valid
        if mood not in videos or videos[mood] is None:
            print(f"Video untuk mood '{mood}' tidak tersedia. Defaulting to camera view.")
            cv2.putText(frame, f"Mood: {mood} (No Video)", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow("Mood Scanner", frame)
            continue

        if current_mood != mood:
            if current_mood in videos and videos[current_mood]:
                videos[current_mood].set(cv2.CAP_PROP_POS_FRAMES, 0)  # Reset video
            current_mood = mood

        ret_video, mood_frame = videos[current_mood].read()
        if ret_video:
            mood_frame = cv2.resize(mood_frame, (frame.shape[1], frame.shape[0]))

            # Gabungkan area transparan dengan latar belakang video
            background_region = cv2.bitwise_and(mood_frame, mood_frame, mask=fg_mask_inv)
            combined_frame = cv2.add(face_region, background_region)

            cv2.putText(combined_frame, f"Mood: {mood}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow("Mood Scanner", combined_frame)
        else:
            print(f"Video untuk mood '{current_mood}' tidak dapat dibaca.")
            cv2.putText(frame, f"Mood: {mood} (No Video)", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow("Mood Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    for video in videos.values():
        if video:
            video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()