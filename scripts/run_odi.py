import cv2

if __name__ == '__main__':
    # 顔検出用のカスケード分類器を読み込む
    face_cascade = cv2.CascadeClassifier('./data/haarcascade_frontalface_default.xml')

    # 動画を読み込む
    cap = cv2.VideoCapture('./data/face.mp4')

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # グレースケールに変換
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 顔検出
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # 顔の周りに赤い矩形を描画
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

        # 結果を表示
        cv2.imshow('Face Detection', frame)

        # 'q'を押すとループから抜ける
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # リソースを解放
    cap.release()
    cv2.destroyAllWindows()
