import sys
import os
import time

if __name__ == '__main__':
    f = open('log.time', 'w')
    start_time = time.time()

    if os.path.exists(sys.argv[2]):
        os.system(f'rm {sys.argv[2]} -rf')
    os.makedirs(sys.argv[2])
    os.system(f'ffmpeg -i {sys.argv[1]} {sys.argv[2]}/%05d.png')
    
    time_taken = time.time() - start_time
    print('----------------------------------------------')
    print(f'time taken for extracting the frames = {time_taken}')
    f.write(f'time taken for extracting the frames = {time_taken}\n')
