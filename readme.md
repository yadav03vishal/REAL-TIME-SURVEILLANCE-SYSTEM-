# Real-Time Surveillance System

## Overview

The Real-Time Surveillance System is an accessible and efficient application tailored for users seeking live camera stream analytics. This guide will walk you through every aspect of the system, providing detailed instructions and insights to ensure a smooth and informed user experience.

## Introduction

### What is the Real-Time Surveillance System?

The Real-Time Surveillance System stands as a pivotal component in a broader surveillance infrastructure. Its primary function is to facilitate real-time analytics on live camera streams. It offers a simplified approach to video stream processing, enabling users to specify a time period and retrieve relevant footage effortlessly.

### Why is it Useful?

The user-centric design ensures that even individuals with limited computer knowledge can navigate the system with ease. The real-time interaction feature empowers users to request specific video footage based on timestamps and durations, promoting a dynamic and tailored user experience. The system employs intelligent storage mechanisms to optimize resource usage, ensuring critical information is stored effectively without overwhelming the user.

## Getting Started

### System Requirements

To embark on your Real-Time Surveillance journey, make sure your computer meets the following requirements:

- Operating System: Windows, macOS, or Linux
- RAM: Minimum 2GB
- Python: Version 3.7 or higher installed

### Installation Instructions

Follow these steps to install and launch the application:

1. **Download:** Access the application from the [GitHub repository](https://github.com/your-username/real-time-surveillance).
2. **Extraction:** Unzip the downloaded file to a location of your preference.
3. **Terminal/Command Prompt:** Open the terminal or command prompt and navigate to the extracted folder.
4. **Run Application:** Type `python image_process.py` and press Enter to launch the application.

### Launching the Application

Upon launching, the application presents a straightforward interface displaying a live camera stream. It will record your live feed info and store the information into the JSON file.

## Using the Application

### Interacting with the Real-Time Surveillance System

The application interface provides a live camera stream. To retrieve video footage for a specific time period:

1. **Timestamp Input:** Enter the timestamp following the on-screen format.
2. **Duration Input:** Specify the duration in seconds.
3. **Press Enter:** Initiate the retrieval process by pressing Enter.

### Retrieving Video Footage

The system processes frames, generates a video file, and presents it to you. It will create an `output.mp4` for the given timestamp and duration.

### Viewing the Output

The output video file is conveniently located in the application folder. Any standard video player on your computer can be used to view the footage.

## File Structure

Explore the contents of the application folder:

- `image_process.py`: Main application file.
- `user_interaction.py`: User-driven interaction file.
- `database_operations.py`: Database-related operations file.
- `frame_info.json`: JSON file storing frame information.
- `output_images/`: Folder containing output frames.
- `output_video.mp4`: Output video file.
- `batch_info.db`: SQLite database file.

## Troubleshooting

### Common Issues

If you encounter any issues, consider the following:

- **Check Inputs:** Verify the correctness of timestamp and duration inputs.




## Additional Information

### Tasks Not Completed

Certain tasks remain uncompleted due to time constraints:

- **Concurrency and Performance:** Concurrent processing of frames from multiple camera streams.
- **Detailed Word Document:** A more comprehensive document explaining the application.

### Acknowledgments

We appreciate your understanding as we continue to improve and enhance the Real-Time Surveillance System.

---

**Note:** This project is not entirely error-proof but can run for a simple use case of the mentioned requirement in the PDF file.

We appreciate your understanding as we continue to improve and enhance the Real-Time Surveillance System. I would like to express my gratitude to HappyMonk for providing me with an assignment to test my capabilities for a data science intern. I have done my best work in the given time frame, and I hope to hear soon from you. This code was entirely created by me, and help was taken from the internet to build this. I hope this meets the requirements mentioned in the PDF file, and I hope to hear from you.


