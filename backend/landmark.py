import cv2
import mediapipe as mp
from mediapipe.framework.formats import landmark_pb2
from mediapipe.python.solutions.drawing_utils import draw_landmarks
from mediapipe.python.solutions.drawing_styles import get_default_pose_landmarks_style, get_default_face_mesh_tesselation_style
from mediapipe.python.solutions.pose_connections import POSE_CONNECTIONS
from mediapipe.python.solutions.face_mesh import FACEMESH_TESSELATION
from mediapipe.python.solutions.hands_connections import HAND_CONNECTIONS
from util import create_normalized_landmark_proto


class Landmark:
    def __init__(self, static_image_mode=False, model_complexity=1, smooth_landmarks=True, refine_face_landmarks=True, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.mp_holistic = mp.solutions.holistic
        self.holistic = self.mp_holistic.Holistic(
            static_image_mode=static_image_mode,
            model_complexity=model_complexity,
            smooth_landmarks=smooth_landmarks,
            refine_face_landmarks=refine_face_landmarks,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence
        )

    def process_frame(self, frame):
        results = self.holistic.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        frame_landmarks = {
            'pose_landmarks': [],
            'face_landmarks': [],
            'left_hand_landmarks': [],
            'right_hand_landmarks': []
        }

        if results.pose_landmarks:
            for landmark in results.pose_landmarks.landmark:
                frame_landmarks['pose_landmarks'].append({
                    'x': landmark.x,
                    'y': landmark.y,
                    'z': landmark.z,
                    'visibility': landmark.visibility
                })

        if results.face_landmarks:
            for landmark in results.face_landmarks.landmark:
                frame_landmarks['face_landmarks'].append({
                    'x': landmark.x,
                    'y': landmark.y,
                    'z': landmark.z
                })

        if results.left_hand_landmarks:
            for landmark in results.left_hand_landmarks.landmark:
                frame_landmarks['left_hand_landmarks'].append({
                    'x': landmark.x,
                    'y': landmark.y,
                    'z': landmark.z
                })

        if results.right_hand_landmarks:
            for landmark in results.right_hand_landmarks.landmark:
                frame_landmarks['right_hand_landmarks'].append({
                    'x': landmark.x,
                    'y': landmark.y,
                    'z': landmark.z
                })

        return frame_landmarks

    def draw_landmarks(self, avatar, frame_landmarks):
        if frame_landmarks['pose_landmarks']:
            pose_landmarks = create_normalized_landmark_proto(frame_landmarks['pose_landmarks'])
            draw_landmarks(
                avatar, landmark_pb2.NormalizedLandmarkList(landmark=pose_landmarks), POSE_CONNECTIONS,
                landmark_drawing_spec=get_default_pose_landmarks_style())

        if frame_landmarks['face_landmarks']:
            face_landmarks = create_normalized_landmark_proto(frame_landmarks['face_landmarks'])
            draw_landmarks(
                avatar, landmark_pb2.NormalizedLandmarkList(landmark=face_landmarks), FACEMESH_TESSELATION,
                landmark_drawing_spec=None,
                connection_drawing_spec=get_default_face_mesh_tesselation_style())

        if frame_landmarks['left_hand_landmarks']:
            left_hand_landmarks = create_normalized_landmark_proto(frame_landmarks['left_hand_landmarks'])
            draw_landmarks(
                avatar, landmark_pb2.NormalizedLandmarkList(landmark=left_hand_landmarks), HAND_CONNECTIONS)

        if frame_landmarks['right_hand_landmarks']:
            right_hand_landmarks = create_normalized_landmark_proto(frame_landmarks['right_hand_landmarks'])
            draw_landmarks(
                avatar, landmark_pb2.NormalizedLandmarkList(landmark=right_hand_landmarks), HAND_CONNECTIONS)
