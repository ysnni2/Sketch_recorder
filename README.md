# Sketch Recorder😊
OpenCV를 이용해 구현한 웹캠 비디오 녹화 프로그램입니다.  
실시간 카메라 화면을 표시할 수 있으며, Preview 모드와 Record 모드를 전환할 수 있습니다.  
추가 기능으로 윤곽선 검출 필터를 구현하여 스케치 스타일의 화면 효과를 적용할 수 있습니다.

---

## 🤖 주요 기능 🤖

- 실시간 웹캠 화면 출력
- Preview 모드 / Record 모드 전환
- Record 모드에서 빨간 원과 `REC` 표시 
- `record.avi` 파일로 영상 저장
- 윤곽선 검출(Edge Filter) 기능
- 프로그램 종료

---

## 조작 방법

- `SPACE` : Preview 모드와 Record 모드 전환
- `E` : Edge Filter 켜기 / 끄기
- `ESC` : 프로그램 종료

---

## 기능 설명

### 1. Preview 모드
프로그램 실행 시 처음에는 Preview 모드로 시작합니다.  
이 상태에서는 카메라 화면만 표시되고 영상은 저장되지 않습니다.  
화면 왼쪽 상단에 `PREVIEW` 문구가 표시됩니다.

### 2. Record 모드
`SPACE` 키를 누르면 Record 모드로 전환됩니다.  
이 상태에서는 웹캠 영상이 `record.avi` 파일로 저장됩니다.
화면 왼쪽 상단에 빨간 원과 `REC` 문구가 표시되어 녹화 중임을 알 수 있습니다.

### 3. 윤곽선 필터 기능
`E` 키를 누르면 윤곽선 필터가 적용됩니다.  
이 기능은 OpenCV의 Canny 알고리즘을 사용하여 카메라 영상의 윤곽선을 검출합니다.  
화면에서는 흰 배경 위에 검은 선이 보이는 스케치 스타일로 표시했습니다.

---

## 저장 파일

- `record.avi` : 녹화된 비디오 파일

---

## 스크린샷 😎

### Preview 모드
#### `preview_mode.png` 파일에서 확인가능 

### Record 모드
#### `record_mode.png` 파일에서 확인 가능 

### Edge Filter 모드
#### 'edge_detection.png' 파일에서 확인 가능 
