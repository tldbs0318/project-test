# 1. Getting Started
```
test_electric_scooter.py와 test.mp4 혹은 electric scooter model test.zip 저장

1) test_electric_scooter.py, test.pm4 다운로드
  PM-tracker.pt, test.mp4와 같은 폴더에 저장 후 VS CODE로 실행

2) electric scooter model test.zip 다운로드
  압축해제 후 VS CODE로 실행
```

# 2. Execution
```
python test_electric_scooter.py
```

# 3. Caution
```
*프레임 계산을 통한 정확도 산출이기 때문에 test.mp4 영상은 전동킥보드가 촬영된 부분만 잘라서 실행*
```

# Test result
```
1) 화질 개선 전 영상 테스트: result_test.mp4 참고

=== 전동 킥보드(PM-Tracker) 객체 탐지 정확도 결과 ===
- 사용된 모델: PM-Tracker.pt
- 총 분석한 영상 프레임: 116장
- AI가 찾아낸 프레임: 65장
*** 최종 탐지율 (Dectection Rate): 56.03%

*카카오톡 영상 전송 시 화질 저하*

2) 화질 개선 후 영상 테스트(원본 촬영 영상): result_test2.mp4 참고

=== 전동 킥보드(PM-Tracker) 객체 탐지 정확도 결과 ===
- 사용된 모델: PM-Tracker.pt
- 총 분석한 영상 프레임: 143장
- AI가 찾아낸 프레임: 99장
*** 최종 탐지율 (Dectection Rate): 69.23%

=> 화질에 따른 정확도 차이 존재
```
