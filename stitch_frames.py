import cv2
import numpy as np
import os
import sys
import time

def get_abs_listdir(DIR):
    '''
    Returns the absolute or relative addresses.
    '''
    return sorted([os.path.join(DIR, frame) for frame in os.listdir(DIR)])

if __name__ == '__main__':
    f = open('log.time', 'a')
    start_time = time.time()

    OP_FRAMES_DIR = sys.argv[1]
    OP_VIDEO_NAME = sys.argv[2]

    print(f'ffmpeg -i {OP_FRAMES_DIR}/%05d_pss2_k0.0.png -c:v libx264 -vf fps=25 -pix_fmt yuv420p -b:v 10M {OP_VIDEO_NAME}')
    os.system(f'ffmpeg -i {OP_FRAMES_DIR}/%05d_pss2_k0.0.png -c:v libx264 -vf fps=25 -pix_fmt yuv420p -b:v 10M {OP_VIDEO_NAME}')
    time_taken_encode = time.time() - start_time
    f.write(f'time taken to encode o/p video = {time_taken_encode}\n')
