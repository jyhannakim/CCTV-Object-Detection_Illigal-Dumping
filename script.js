window.addEventListener('DOMContentLoaded', (event) => {
    openNav();
  });
  
  function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
  }
  
  function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
  }

  function showHome() {
    document.getElementById('main').innerHTML = `
        <img src="./assets/cctv.png" alt="CCTV" class="center-image"> <!-- CCTV 이미지 추가 -->

        <div class="white-box">
          <img src="./assets/box.png" alt="white-box" class="center-image"> 
          <button onclick="showVideo1()" class="start-button">Start</button>
        </div>
    `;
  }
  function showVideo1() {
    document.getElementById('main').innerHTML = `

        <input type="file" id="videoUpload" accept="video/*" class="upload-button">
        
        <div class="video-and-frames-container">
            <div class="video-container">
                <div class="video-section">
                    <p>Original Video</p>
                    <video id="uploadedVideo" controls style="display: none; width: 100%; max-width: 300px; margin-top: 10px;">
                        Your browser does not support the video tag.
                    </video>
                </div>
                <div class="video-section">
                    <p>Result Video</p>
                    <video id="resultVideo" controls style="display: none; width: 100%; max-width: 300px; margin-top: 10px;">
                        Your browser does not support the video tag.
                    </video>
                </div>
            </div>

            <div id="garbageFramesContainer" class="frames-container"></div>
        </div>
    `;

    document.getElementById('videoUpload').addEventListener('change', function(event) {
        const file = event.target.files[0];
        if (file) {
            const videoElement = document.getElementById('uploadedVideo');
            const videoURL = URL.createObjectURL(file);

            videoElement.src = videoURL;
            videoElement.style.display = 'block';
            videoElement.load();

            setTimeout(() => {
                const resultVideoElement = document.getElementById('resultVideo');
                const resultVideoURL = 'cctv_video/result/garbagedump_result.mp4';

                resultVideoElement.src = resultVideoURL;
                resultVideoElement.style.display = 'block';
                resultVideoElement.load();
                displayGarbageFrames([45, 139, 225]);
            }, 10000); 
        }
    });
}

function displayGarbageFrames(frames) {
  const container = document.getElementById('garbageFramesContainer');
  frames.forEach(frameNum => {
      const frameBox = document.createElement('div');
      frameBox.classList.add('frame-box');
      
      const img = document.createElement('img');
      img.src = `frame/detected_frames/frame_${frameNum}.jpg`; 
      img.alt = `Frame ${frameNum}`;

      const frameInfo = document.createElement('div');
      const frameNumText = document.createElement('p');
      frameNumText.classList.add('frame-num');
      frameNumText.textContent = `${frameNum} frame`;
      
      const garbageText = document.createElement('p');
      garbageText.textContent = 'Garbage Detected!!';
      
      frameInfo.appendChild(frameNumText);
      frameInfo.appendChild(garbageText);
      
      frameBox.appendChild(img);
      frameBox.appendChild(frameInfo);
      container.appendChild(frameBox);
  });
}

function showVideo2() {
  document.getElementById('main').innerHTML = `   
      <div class="video-and-frames-container">
          <div class="video-container">
              <div class="video-section">
                  <div style="display: flex; align-items: center;">
                      <p style="margin-right: 10px;">Original Video</p>
                      <button id="detectButton" class="detect-button" style="background-color: #32CD32; color: white; border: none; padding: 5px 10px; cursor: pointer; font-size: 14px;">
                          Detect
                      </button>
                  </div>
                  <video id="uploadedVideo" controls style="width: 100%; max-width: 300px; margin-top: 10px;">
                      <source src="cctv_video/video2.mp4" type="video/mp4">
                      Your browser does not support the video tag.
                  </video>
              </div>
              
              <div class="video-section">
                  <p>Result Video</p>
                  <video id="resultVideo" controls style="display: none; width: 100%; max-width: 300px; margin-top: 10px;">
                      Your browser does not support the video tag.
                  </video>
              </div>
          </div>

          <div id="garbageFramesContainer" class="frames-container"></div>
      </div>
  `;

  document.getElementById('detectButton').addEventListener('click', function() {
      const resultVideoElement = document.getElementById('resultVideo');
      const resultVideoURL = 'cctv_video/result/garbagedump_result2.mp4'; // 결과 비디오 경로

      resultVideoElement.src = resultVideoURL;
      resultVideoElement.style.display = 'block';
      resultVideoElement.load();

      displayGarbageFrames2([38, 106, 181, 240, 301]);
  });
}

function displayGarbageFrames2(frames) {
  const container = document.getElementById('garbageFramesContainer');
  frames.forEach(frameNum => {
      const frameBox = document.createElement('div');
      frameBox.classList.add('frame-box');
      
      const img = document.createElement('img');
      img.src = `frame/detected_frames2/frame_${frameNum}.png`; 
      img.alt = `Frame ${frameNum}`;

      const frameInfo = document.createElement('div');
      const frameNumText = document.createElement('p');
      frameNumText.classList.add('frame-num');
      frameNumText.textContent = `${frameNum} frame`;
      
      const garbageText = document.createElement('p');
      garbageText.textContent = 'Garbage Detected!!';
      
      frameInfo.appendChild(frameNumText);
      frameInfo.appendChild(garbageText);
      
      frameBox.appendChild(img);
      frameBox.appendChild(frameInfo);
      container.appendChild(frameBox);
  });
}



  function showMembers() {
    document.getElementById('main').innerHTML = `
        <h1>Our Team</h1>
        <div class="members-grid">
            <div class="member-card" style="background-color: #EBE9FB;">
                <img src="./assets/yaeji.png" alt="Yaeji Kim" class="member-photo">
                <h3>Yaeji Kim</h3>
                <a href="https://github.com/jyhannakim" target="_blank">Github_jyhannakim</a>
            </div>
            <div class="member-card" style="background-color: #facfd6;">
                <img src="./assets/jaeyoung.png" alt="Jaeyoung Kim" class="member-photo">
                <h3>Jaeyoung Kim</h3>
                <a href="https://github.com/sevenrich03" target="_blank">Github_sevenrich03</a>
            </div>
            <div class="member-card" style="background-color: #DFF7FF;">
                <img src="./assets/narae.png" alt="Narae Jang" class="member-photo">
                <h3>Narae Jang</h3>
                <a href="https://github.com/brandnewwwwnarae" target="_blank">Github_brandnewwwwnarae</a>
            </div>
            <div class="member-card" style="background-color: #EEFFD3;">
                <img src="./assets/minju.png" alt="Minju Jang" class="member-photo">
                <h3>Minju Jang</h3>
                <a href="https://github.com/alswn-03" target="_blank">Github_alswn-03</a>
            </div>
        </div>
    `;
  }
