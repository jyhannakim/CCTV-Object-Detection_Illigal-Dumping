import cv2
import torch
import io
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
import numpy as np
import os

# # YOLOv5 모델 불러오기
# MODEL_PATH = "yolov5s_results/weights/best.pt"  # 사용자 모델 파일 경로
#model = torch.hub.load('ultralytics/yolov5', 'yolov5m')  # 모델을 'yolov5m'으로 변경# YOLOv5 모델 불러오기
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# model = torch.hub.load("ultralytics/yolov5", "custom", path=MODEL_PATH, force_reload=True)  # local model

app = FastAPI()

# 감지 결과를 저장할 리스트
detection_results = []

# 업로드된 파일을 저장할 디렉토리 생성
UPLOAD_DIR = "./uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload_video/")
async def upload_video(file: UploadFile = File(...)):
    # 업로드된 파일 저장
    file_location = f"{UPLOAD_DIR}/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    
    # 동영상 처리
    cap = cv2.VideoCapture(file_location)
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1
        # YOLOv5 모델을 사용해 프레임 처리
        results = model(frame)
        detections = results.xyxy[0].cpu().numpy()  # 감지 결과를 numpy 배열로 변환
        
        # 감지 결과 저장
        detection_results.append({
            "frame": frame_count,
            "detections": detections.tolist()
        })
    
    cap.release()
    
    # 감지 결과를 HTML로 반환
    results_html = "<h2>Detection Results</h2><pre>{}</pre>".format(detection_results)
    content = f"""
    <html>
        <head>
            <title>Video Upload</title>
        </head>
        <body>
            <h1>Upload Video for Garbage Detection</h1>
            <form action="/upload_video/" enctype="multipart/form-data" method="post">
                <input name="file" type="file">
                <input type="submit">
            </form>
            {results_html}
        </body>
    </html>
    """
    return HTMLResponse(content=content)

@app.get("/")
async def main():
    content = """
    <html>
        <head>
            <title>Video Upload</title>
        </head>
        <body>
            <h1>Upload Video for Garbage Detection</h1>
            <form action="/upload_video/" enctype="multipart/form-data" method="post">
                <input name="file" type="file">
                <input type="submit">
            </form>
        </body>
    </html>
    """
    return HTMLResponse(content=content)

# FastAPI 서버 실행
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
