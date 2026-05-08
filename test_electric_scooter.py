import cv2
from ultralytics import YOLO

def measure_custom_accuracy(video_path, model_path, target_classes, test_name):
    
    model = YOLO(model_path)
    cap = cv2.VideoCapture(video_path)
    
    # 원본 영상의 크기와 FPS(초당 프레임 수) 정보 가져오기
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    # 테스트 영상 저장 설정
    output_filename = f"result_{video_path}"
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # mp4 코덱
    out = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))
   
    detected_frames = 0
    total_processed_frames = 0

    print(f"\n[{test_name}] 영상을 분석하며 '{output_filename}' 파일로 저장 중입니다...")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        total_processed_frames += 1
        results = model(frame, verbose=False)

        # Bounding Box 생성
        annotated_frame = results[0].plot()
        
        # 테스트 영상 저장
        out.write(annotated_frame)
        
        cv2.imshow("YOLO Detection Test", annotated_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("사용자에 의해 영상 재생이 중단되었습니다.")
            break

        object_detected = False
        for box in results[0].boxes:
            detected_class = int(box.cls[0])
            if detected_class in target_classes:
                object_detected = True
                break

        if object_detected:
            detected_frames += 1

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    actual_target_frames = total_processed_frames

    if actual_target_frames > 0:
        accuracy = (detected_frames / actual_target_frames) * 100
        print(f"\n=== {test_name} 객체 탐지 정확도 결과 ===")
        print(f"- 사용된 모델: {model_path}")
        print(f"- 총 분석한 영상 프레임: {total_processed_frames}장")
        print(f"- AI가 찾아낸 프레임: {detected_frames}장")
        print(f"*** 최종 탐지율 (Detection Rate): {accuracy:.2f}%")
        print(f"결과 영상이 '{output_filename}' 이름으로 저장되었습니다!")
    else:
        print("영상을 읽을 수 없거나 프레임이 0장입니다.")

if __name__ == "__main__":
    measure_custom_accuracy(
        video_path="test.mp4",
        model_path="PM-Tracker.pt",
        target_classes=[0],
        test_name="전동 킥보드(PM-Tracker)"
    )