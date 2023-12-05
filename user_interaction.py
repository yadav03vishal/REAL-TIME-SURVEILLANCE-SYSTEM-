#USER_INTERACTION.PY
import cv2
import json
from datetime import datetime, timedelta
import os
def get_timestamp_from_user():
    # Get timestamp input from the user
    user_timestamp = int(input("Enter timestamp in the format stored in the JSON file: "))
    return user_timestamp

def get_duration_from_user():
    # Get duration input from the user in seconds
    user_duration = int(input("Enter duration in seconds: "))
    return user_duration

def retrieve_camera_footage(timestamp, duration):
    # Read frame information from the JSON file
    with open('frame_info.json', 'r') as json_file:
        frame_info_list = [json.loads(line) for line in json_file]

    # Identify frames within the specified time period
    relevant_frames = [frame for frame in frame_info_list if timestamp <= frame['timestamp'] <= timestamp + duration]

    return relevant_frames

def create_mp4_from_frames(frames, output_filename='output_video.mp4'):
    # Check if frames exist
    if not frames:
        print("No frames found.")
        return

    # Get frame dimensions from the first frame (default and fixed values)
    frame_width, frame_height = 640, 480  # Default and fixed values for laptop camera

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can use other codecs like 'XVID' based on your system
    output_path = 'output_video.mp4'
    
    # Set the frame rate to 1 frame per second
    frame_rate = 1
    out = cv2.VideoWriter(output_path, fourcc, frame_rate, (frame_width, frame_height))

    # Iterate over frames and add them to the video
    for frame in frames:
        image_path = frame['image_path']
        if os.path.exists(image_path):
            img = cv2.imread(image_path)
            out.write(img)
        else:
            print(f"Image not found: {image_path}")

    # Release the VideoWriter and print the output path
    out.release()
    print(f"Video saved at: {output_path}")

# Example usage
def main():
    # Get user input for timestamp and duration
    user_timestamp = get_timestamp_from_user()
    user_duration = get_duration_from_user()

    # Retrieve camera footage based on user input
    result_frames = retrieve_camera_footage(user_timestamp, user_duration)

    # Create MP4 file from frames
    create_mp4_from_frames(result_frames)

if __name__ == "__main__":
    main()
