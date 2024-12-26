import cv2
import numpy as np
from scipy.fftpack import dct, idct

def apply_dct_block(block):
    # Apply DCT
    dct_block = dct(dct(block.T, norm='ortho').T, norm='ortho')
    return dct_block


def quantize(block, q=400):
    return np.round(block / q) * q


def apply_idct_block(block):
    idct_block = idct(idct(block.T, norm='ortho').T, norm='ortho')
    return idct_block


def process_block(block):
    # DCT
    dct_block = apply_dct_block(block)

    # Quantization
    quantized_block = quantize(dct_block, q=400)

    # Inverse DCT
    idct_block = apply_idct_block(quantized_block)

    return idct_block

def process_frame(frame):
    # Split the frame into RGB channels
    B, G, R = cv2.split(frame)
    
    # Initialize output channels
    B_processed, G_processed, R_processed = (np.zeros_like(B) for _ in range(3))

    # Process each channel
    for channel, processed_channel in zip([B, G, R], [B_processed, G_processed, R_processed]):
        # Divide the channel into 8x8 blocks and process each block
        for i in range(0, channel.shape[0], 8):
            for j in range(0, channel.shape[1], 8):
                block = channel[i:i+8, j:j+8]
                processed_block = process_block(block)
                processed_channel[i:i+8, j:j+8] = processed_block

    # Merge the processed channels back into a frame
    processed_frame = cv2.merge([B_processed, G_processed, R_processed])
    print("ok")
    return processed_frame

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()
    return frames

def write_video(frames, output_path):
    height, width, layers = frames[0].shape
    video = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))

    for frame in frames:
        compressed_image = np.uint8(np.clip(frame, 0, 255))
        video.write(compressed_image)

    video.release()

# Main
video_path = 'input.mp4'
frames = read_video(video_path)

processed_frames = [process_frame(frame) for frame in frames]
output_video_path = 'compressed_video.mp4'
write_video(processed_frames, output_video_path)
