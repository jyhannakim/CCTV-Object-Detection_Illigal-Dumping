import cv2
import torch
import time

# YOLOv5 모델 불러오기
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # yolov5s 모델 사용

# 웹캠 비디오 캡처 객체 생성 (디폴트 웹캠: 0)
video_capture = cv2.VideoCapture(0)

# 이전 프레임의 감지 결과를 저장할 변수
previous_detections = []

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

while True:
    # 프레임 읽기
    ret, frame = video_capture.read()
    if not ret:
        break

    # 객체 감지 수행
    results = model(frame)
    current_detections = results.xyxy[0].cpu().numpy()  # 감지 결과를 numpy 배열로 변환

    # 이전 프레임과 현재 프레임 간 쓰레기 변화 감지
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
            print(f"새 쓰레기 감지됨: {current_detection}")

    # 이전 프레임 감지 결과 업데이트
    previous_detections = current_detections

    # 프레임 디스플레이
    cv2.imshow('Video', frame)

    # 'q' 키를 누르면 루프 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 비디오 캡처 객체 및 모든 창 닫기
video_capture.release()
cv2.destroyAllWindows()
