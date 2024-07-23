import cv2
import torch
import io
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
import numpy as np
import os
from datetime import timedelta

# YOLOv5 모델 불러오기
model = torch.hub.load('ultralytics/yolov5', 'yolov5m')  # 모델을 'yolov5m'으로 변경

app = FastAPI()

# 감지 결과를 저장할 리스트
detection_results = []

# 업로드된 파일을 저장할 디렉토리 생성
UPLOAD_DIR = "./uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Jinja2 템플릿 설정
templates = Jinja2Templates(directory="templates")

@app.post("/upload_video/")
async def upload_video(request: Request, file: UploadFile = File(...)):
    # 업로드된 파일 저장
    file_location = f"{UPLOAD_DIR}/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    
    # 동영상 처리
    cap = cv2.VideoCapture(file_location)
    frame_count = 0
    fps = cap.get(cv2.CAP_PROP_FPS)  # 영상의 FPS를 얻어옴
    detection_results.clear()  # 이전 감지 결과 초기화
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1
        # YOLOv5 모델을 사용해 프레임 처리
        results = model(frame)
        detections = results.xyxy[0].cpu().numpy()  # 감지 결과를 numpy 배열로 변환
        
        # 감지 결과 저장
        for detection in detections:
            x1, y1, x2, y2, conf, cls = detection
            if conf > 0.5:  # confidence 임계값 설정
                detection_results.append({
                    "frame": frame_count,
                    "time": str(timedelta(seconds=frame_count / fps)),
                    "detection": detection.tolist()
                })
    
    cap.release()
    
    # 업로드된 동영상 경로와 감지 결과를 JSON 형태로 반환
    return JSONResponse(content={"video_path": file_location, "detection_results": detection_results})

@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# FastAPI 서버 실행
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
