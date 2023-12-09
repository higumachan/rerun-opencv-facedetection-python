import cv2
import rerun
from rerun.components import DrawOrder

if __name__ == '__main__':
    # 顔検出用のカスケード分類器を読み込む
    face_cascade = cv2.CascadeClassifier('./data/haarcascade_frontalface_default.xml')

    # 動画を読み込む
    cap = cv2.VideoCapture('./data/face.mp4')

    rerun.init("face_detection", spawn=True)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        rerun.log("rgb", rerun.Image(frame[:, :, ::-1], draw_order=[]))

        # グレースケールに変換
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        rerun.log("gray", rerun.Image(gray))

        # 顔検出
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # 顔の周りに赤い矩形を描画
        for (x, y, w, h) in faces:
            rerun.log("rgb/faces", rerun.Boxes2D(mins=[x, y], sizes=[w, h]))
            rerun.log("gray/faces", rerun.Boxes2D(mins=[x, y], sizes=[w, h]))

    # リソースを解放
    cap.release()
    cv2.destroyAllWindows()
