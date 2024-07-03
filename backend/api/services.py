import cv2
import os
import numpy as np
from fastapi import HTTPException
from landmark import Landmark

def generate_avatar(words):
    # Initialize the Landmark class
    landmark = Landmark()

    all_landmarks_data = []
    
    for word in words:
        video_path = f"assets/sign_lang_videos/{word}.mp4"
        
        if not os.path.exists(video_path):
            raise HTTPException(status_code=404, detail=f"Video file for word '{word}' not found")
        
        cap = cv2.VideoCapture(video_path)
        landmarks_data = []

        # Process each frame of the input video
        frame_index = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Process the frame for holistic landmarks
            frame_landmarks = landmark.process_frame(frame)
            frame_landmarks['frame'] = frame_index

            landmarks_data.append(frame_landmarks)
            frame_index += 1

        all_landmarks_data.append({
            'name': word,
            'landmarks': landmarks_data
        })

        cap.release()

    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    out = cv2.VideoWriter('output_video_c.mp4', fourcc, 30, (1280, 720))  # Adjust resolution as needed

    # Define a simple avatar
    avatar = np.zeros((720, 1280, 3), dtype=np.uint8)
    avatar[:] = (255, 255, 255)  # Set the avatar color (white)

    # Process each word's landmarks data
    for word_data in all_landmarks_data:
        word = word_data['name']
        landmarks_data = word_data['landmarks']
        
        for frame_landmarks in landmarks_data:
            # Clear the avatar frame
            avatar[:] = (255, 255, 255)

            # Draw the pose, face, and hand landmarks on the avatar
            landmark.draw_landmarks(avatar, frame_landmarks)

            # Write the avatar frame to the output video
            out.write(avatar)

    # Release resources
    out.release()
    cv2.destroyAllWindows()

    out_path = 'output_video_c.mp4'
    return out_path

def iterfile(file_path: str):
    with open(file_path, mode="rb") as file_like:
        yield from file_like
