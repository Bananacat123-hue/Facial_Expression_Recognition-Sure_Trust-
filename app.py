from flask import Flask, render_template, request, Response
from ultralytics import YOLO
from PIL import Image
import os
import uuid
import cv2

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

model = YOLO('model/face_emotion_recognition.pt')
camera = None

def get_emoji_path(emotion):
    jpeg_path = f'static/emojis/{emotion}.jpeg'
    jpg_path = f'static/emojis/{emotion}.jpg'
    if os.path.exists(jpeg_path):
        return jpeg_path
    elif os.path.exists(jpg_path):
        return jpg_path
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    emotion = None
    emoji_path = None
    uploaded_path = None
    show_text = False

    if request.method == 'POST':
        file = request.files.get('image')
        if file:
            filename = f'{uuid.uuid4()}.jpg'
            uploaded_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(uploaded_path)

            results = model(uploaded_path)
            if results and results[0].boxes and len(results[0].boxes.cls) > 0:
                pred_idx = int(results[0].boxes.cls[0])
                emotion = model.names[pred_idx]
                emoji_path = get_emoji_path(emotion)
                if not emoji_path:
                    show_text = True

    return render_template('index.html',
                           emotion=emotion,
                           emoji_path=emoji_path,
                           uploaded_path=uploaded_path,
                           show_text=show_text)

def gen_frames():
    global camera
    if camera is None:
        camera = cv2.VideoCapture(0)

    while True:
        success, frame = camera.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)

        results = model(frame)
        if results and results[0].boxes and len(results[0].boxes.cls) > 0:
            pred_idx = int(results[0].boxes.cls[0])
            label = model.names[pred_idx]
            cv2.putText(frame, label, (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/shutdown_camera')
def shutdown_camera():
    global camera
    if camera:
        camera.release()
        camera = None
    return "Camera released"

if __name__ == '__main__':
    app.run(debug=True)
