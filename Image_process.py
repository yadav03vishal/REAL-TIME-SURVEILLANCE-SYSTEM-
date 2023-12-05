# IMAGE_PROCESS.PY
import cv2
import json
import os
from datetime import datetime
# import geocoder  # Uncomment this line if you want to use real-time geo-location
import database_operations
from user_interaction import retrieve_camera_footage  # Import the function


def get_current_location():
    # Uncomment the following line if you want to use real-time geo-location
    # location = geocoder.ip('me')
    # return {'latitude': location.latlng[0], 'longitude': location.latlng[1]}
    
    # Use initialized geo-location due to CPU usage concerns
    return {'latitude': 0.0, 'longitude': 0.0}

def process_frame(frame, camera_id, frame_id, geo_location, image_path):
    # Create a JSON object for each frame
    frame_info = {
        'camera_id': camera_id,
        'frame_id': frame_id,
        'geo_location': geo_location,
        'image_path': image_path,
        'timestamp': int(datetime.timestamp(datetime.now()))  # Add timestamp to frame_info
    }

    # Write frame information to a JSON file
    json_file_path = 'frame_info.json'
    with open(json_file_path, 'a') as json_file:
        json.dump(frame_info, json_file)
        json_file.write('\n')

    # Display geo-location on every 5th frame and this commented because again due to extra CPU usage and lower frame detection
    # if frame_id % 5 == 0:
    #     geo_text = f"Latitude: {geo_location['latitude']}, Longitude: {geo_location['longitude']}"
    #     cv2.putText(frame, geo_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Consider that the streaming is 25 FPS
    # Write one frame per second as an image file and reuse that file for the rest 24 frames
    if frame_id % 25 == 0:
        cv2.imwrite(image_path, frame)

# Example usage within the video capture loop
def main():
    camera_id = 1
    frame_id = 0
    output_folder = 'output_images'

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    cap = cv2.VideoCapture(0)  # 0 corresponds to the default camera (laptop camera)

    # Initialize the database (run this only once)
    database_operations.create_database()

    last_batch_time = int(datetime.timestamp(datetime.now()))

    result_batches = []  # Move the definition outside the if block

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_id += 1
        image_path = os.path.join(output_folder, f'frame_{frame_id}.jpg')

        geo_location = get_current_location()

        process_frame(frame, camera_id, frame_id, geo_location, image_path)

        cv2.imshow('Live Feed', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Batch information for every 1 second
        current_time = int(datetime.timestamp(datetime.now()))
        if current_time - last_batch_time >= 1:
            # Retrieve batches for the last 1 second
            timestamp = current_time - 1
            user_duration = 1
            result_batches = retrieve_camera_footage(timestamp, user_duration)

            # Insert batch information into the database
            database_operations.insert_batch_info(result_batches)

            last_batch_time = current_time

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

