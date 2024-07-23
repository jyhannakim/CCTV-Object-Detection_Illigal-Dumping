import cv2
import os
import glob
import torch

# YOLOv5 모델 불러오기
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # yolov5s 모델 사용

# 폴더 내 모든 이미지 파일 목록
image_files = glob.glob('./frame/*.jpeg')

# 이미지 파일 정렬 (frame0.jpeg, frame1.jpeg, ...)
image_files.sort()

# 각 이미지에 대한 객체 감지 결과를 저장할 리스트
detection_results = []

# 객체 감지 모델 초기화 및 실행
for image_file in image_files:
    image = cv2.imread(image_file)
    results = model(image)  # 객체 감지 수행
    detections = results.xyxy[0].cpu().numpy()  # 감지 결과를 numpy 배열로 변환
    detection_results.append(detections)

# 이전 프레임과 현재 프레임 간 쓰레기 변화 감지
for i in range(1, len(detection_results)):
    previous_detections = detection_results[i-1]
    current_detections = detection_results[i]
    for current_detection in current_detections:
        x1, y1, x2, y2, conf, cls = current_detection
        new_object = True
        for previous_detection in previous_detections:
            px1, py1, px2, py2, pconf, pcls = previous_detection
            if abs(x1 - px1) < 10 and abs(y1 - py1) < 10:
                new_object = False
                break
        if new_object:
            print(f"새 쓰레기 감지됨 at {image_files[i]}: {current_detection}")

print("변화 감지 완료!")
