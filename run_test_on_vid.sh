VIDEO_NAME=../frames/EROS_Original_1.mov
EXTRACT_FRAMES_DIR=frames/input
OP_FRAMES_DIR=frames/output
OP_VIDEO_NAME=frames/AWGN_EROS_Original_1.mp4

python extract_frames.py $VIDEO_NAME $EXTRACT_FRAMES_DIR

python/test_fastdvdnet.py \
		--test_path $EXTRACT_FRAMES_DIR \
			--noise_sigma 30 \
				--save_path $OP_FRAMES_DIR

python stitch_frames.py $OP_FRAMES_DIR $OP_VIDEO_NAME
