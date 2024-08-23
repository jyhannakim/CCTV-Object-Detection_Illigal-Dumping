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
          <button onclick="showVideo()" class="start-button">Start</button>
        </div>
    `;
  }
  function showVideo() {
    // 비디오 페이지를 로드
    document.getElementById('main').innerHTML = `
        <!-- 파일 업로드 버튼 -->
        <input type="file" id="videoUpload" accept="video/*" class="upload-button">
        
        <!-- 비디오를 표시할 영역 -->
        <div class="video-container">
            <video id="uploadedVideo" controls style="display: none; width: 100%; max-width: 600px; margin-top: 20px;">
                Your browser does not support the video tag.
            </video>
            <p>Original Video</p>

            <!-- 결과 비디오를 표시할 영역 -->
            <video id="resultVideo" controls style="display: none; width: 100%; max-width: 600px; margin-top: 20px;">
                Your browser does not support the video tag.
            </video>
            <p>Result Video</p>
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
          }, 10000); 
      }
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