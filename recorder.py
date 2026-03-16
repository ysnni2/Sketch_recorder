import cv2

cap = cv2.VideoCapture(0)

recording = False
edge_mode = False
out = None

fourcc = cv2.VideoWriter_fourcc(*'XVID')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    display_frame = frame.copy()

    if edge_mode:
        edges = cv2.Canny(frame, 100, 200)
        edges = cv2.bitwise_not(edges)
        display_frame = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

        cv2.putText(display_frame, "EDGE FILTER",
                    (10, 70),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 0, 0),
                    2)

    if recording:
        if out is None:
            h, w = frame.shape[:2]
            out = cv2.VideoWriter('record.avi', fourcc, 20.0, (w, h))

        out.write(frame)

        cv2.circle(display_frame, (30, 30), 10, (0, 0, 255), -1)
        cv2.putText(display_frame, "REC",
                    (50, 35),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 0, 255),
                    2)
    else:
        cv2.putText(display_frame, "PREVIEW",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (255, 255, 255),
                    2)

    cv2.imshow("Video Recorder", display_frame)

    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        break
    elif key == 32:
        recording = not recording
    elif key == ord('e'):
        edge_mode = not edge_mode

cap.release()
if out is not None:
    out.release()
cv2.destroyAllWindows()