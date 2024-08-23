# 🔥무단투기, 멈춰! : CCTV Object Detection_Illigal Dumping
### | Project
Due to the problem of illegal dumping of garbage, illegal dumping has been detected nationwide through the installation of CCTV. However, cctv's (such as smart warning boards) for preventing illegal dumping are surveillance cameras that can shoot video and guide audio and try to prevent them through audiovisual stimulation, and some are settings to catch illegal dumping through direct manpower input. If motion recognition cctv is used, the following expected effects can be obtained.

1. Reduce unnecessary surveillance personnel
2. Speed up response to unauthorized speculators through real-time detection


### | Stacks
<img src="https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white"><img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"> <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi"><img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"><img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white">

### | Dataset
[AI hub_공원 주요시설 및 불법행위 감시 CCTV 영상 데이터](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=477)<br>
We use video that has various situations such as (one person / two people), (a tied garbage bag / an untethered garbage bag), (no trash can/ when there is a trash can but throwing it away somewhere else).

### | Model
**Yolov5**<br>
Among Yolo's many versions, it was selected as a model with a fast calculation speed (up to 140 frames per second), so it was considered suitable for real-time motion tracking.


### | Training
We use [Roboflow](https://roboflow.com/) for data labeling. Labeling was conducted by classifying it into three classes :<br> `Garbage` , `Bin`, `Person`<br>

<img width = "400px" src="assets/readme//labeling.png">


### | Result
**F1-Confidence Curve : 0.92**
<br><img width = "300px" src="assets/readme/f1-confidence curve.jpg" > 

**Precision-recall curve : 0.940**
<br><img width = "300px" src="assets/readme//precision-recall curve.jpg" >

### | Function
<img width = "300px" src = "assets/readme/detect.png"><br>
Run the yolov5 model to extract coordinates txt for each frame.<br>
-> After merging this into a csv file, only the garbage is identified and extracted based on the class ID. <br>
-> Through this process, the last change frame is extracted.

EX. last dump frame:<br>
1st garbage dump : 00 frame<br>
2nd garbage dump: 00 frame
...

### | Web
**Home Page** <br>This is the page you see when you try to enter the website. Here, the start button will take you to the video menu page on the left. 
<br><img width= "500px" src="assets/readme//home.png"><br>
There is a sidebar on the left, so you can click on the page you want. Click on the prometheus logo to go to the [club's main site](https://prometheus-ai.net/). Also, if you click Members, you can find out the members' GitHub addresses, and if you click Github, you can go to the project address.

**Video Page**
<br><img width= "500px" src="assets/readme//video.png">

### | Members
|      김예지       |          김재영         |     장민주         |      장나래       |                                                                                                               
| :------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------: |  
|   <img width="130px" src="./assets/yaeji.png" />    |                      <img width="300px" src="./assets/jaeyoung.png" />    |                   <img width="250px" src="./assets/minju.png"/>   |   <img width="180px" src="./assets/narae.png" />    |
|   [@jyhannakim](https://github.com/jyhannakim)   |    [@sevenrich03](https://github.com/sevenrich03)  | [@alswn-03](https://github.com/alswn-03)  | [@brandnewwwnarae](https://github.com/brandnewwwnarae)  |


### | Directory Structure
```
CCTV-Object-Detection_Illigal-Dumping
│
├── README.md         
├── Extract_illegal_garbage_detection_from_raw_vid_version1.ipynb 
├── index.html          
├── script.js     
│
├── assets/           
│   ├── readme/    
│   ├── detect-icon.png      
│   └── github-icon.png
|   └── ...
│
├── styles/           
│   ├── styles.css
│
  ```
