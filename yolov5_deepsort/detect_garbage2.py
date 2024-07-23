import cv2
import os
import glob
import torch

# YOLOv5 모델 불러오기
model = torch.hub.load('ultralytics/yolov5', 'yolov5m')  # 모델을 'yolov5m'으로 변경

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

# IoU 계산 함수
def calculate_iou(box1, box2):
    x1, y1, x2, y2 = box1
    x1_p, y1_p, x2_p, y2_p = box2
    inter_x1 = max(x1, x1_p)
    inter_y1 = max(y1, y1_p)
    inter_x2 = min(x2, x2_p)
    inter_y2 = min(y2, y2_p)
    inter_area = max(0, inter_x2 - inter_x1) * max(0, inter_y2 - inter_y1)
    box1_area = (x2 - x1) * (y2 - y1)
    box2_area = (x2_p - x2_p) * (y2_p - y1_p)
    union_area = box1_area + box2_area - inter_area
    return inter_area / union_area if union_area > 0 else 0

# 이전 프레임과 현재 프레임 간 쓰레기 변화 감지
for i in range(1, len(detection_results)):
    previous_detections = detection_results[i-1]
    current_detections = detection_results[i]
    for current_detection in current_detections:
        x1, y1, x2, y2, conf, cls = current_detection
        if conf < 0.5:  # confidence 임계값 설정
            continue
        new_object = True
        for previous_detection in previous_detections:
            px1, py1, px2, py2, pconf, pcls = previous_detection
            iou = calculate_iou((x1, y1, x2, y2), (px1, py1, px2, py2))
            if iou > 0.5:  # IoU 임계값 설정
                new_object = False
                break
        if new_object:
            print(f"새 쓰레기 감지됨 at {image_files[i]}: {current_detection}")

print("변화 감지 완료!")
