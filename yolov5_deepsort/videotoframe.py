import cv2
import os

# 'frame' 폴더가 없다면 생성
if not os.path.exists('frame'):
    os.makedirs('frame')

video = cv2.VideoCapture('쓰레기 무단투기 인식 demo1.mp4')

count = 0
fps = video.get(cv2.CAP_PROP_FPS)
frame_interval = int(fps / 5)  # 초당 5프레임 저장

while video.isOpened():
    try:
        ret, image = video.read()
        if not ret:
            break

        if int(video.get(cv2.CAP_PROP_POS_FRAMES)) % frame_interval == 0:
            cv2.imwrite(f"frame/frame{count}.jpeg", image)
            print(f'Download {count}')
            count += 1
    except cv2.error as e:
        print(f"Error: {e}")
        continue

print("Done!")
video.release()