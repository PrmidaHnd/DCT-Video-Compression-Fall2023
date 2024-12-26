# DCT Video Compression (Fall 2023)

This project implements a video compression algorithm based on the Discrete Cosine Transform (DCT) technique. The project demonstrates the ability of DCT in reducing the size of a video while maintaining reasonable quality.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [License](#license)

## Introduction
This project uses the Discrete Cosine Transform (DCT) to compress video files. The DCT algorithm transforms the video frames into frequency components, allowing for the removal of less significant data, thus reducing the size of the video file. The result is a compressed video that can be stored or transmitted more efficiently.

## Features
- **DCT-based Compression**: Uses DCT to transform the video frames for compression.
- **Optimized Storage**: Compresses videos to a fraction of their original size.

## Installation
To run this project, you need to have Python 3.x installed on your machine. It is recommended to create a virtual environment for the project.

1. Clone the repository:
    ```bash
    git clone https://github.com/PrmidaHnd/DCT-Video-Compression-Fall2023.git
    ```

2. Navigate to the project directory:
    ```bash
    cd DCT-Video-Compression-Fall2023
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. **Prepare your own input video**: Since this repository does not include any video files, you will need to provide your own video file. Place your video file (e.g., `input_video.mp4`) in the same directory as the script.

2. **Compress the video**: After placing your video file, run the compression script to compress it. Replace `input_video.mp4` with the name of your video file and `output_video_compressed.mp4` with the desired name for the compressed output:
    ```bash
    python compress_video.py input_video.mp4 output_video_compressed.mp4
    ```

3. **Adjust Compression Quality**: You can modify the compression quality by adjusting the parameters in the code (e.g., the quantization table). Refer to the script's code for more details on how to change these settings.

## Dependencies
- Python 3.x
- NumPy
- OpenCV
- ffmpeg (for video processing)

You can install the necessary dependencies using:
```bash
pip install numpy opencv-python ffmpeg-python
