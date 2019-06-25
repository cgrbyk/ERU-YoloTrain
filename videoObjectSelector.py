import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt
import numpy as np
import time

#%config InlineBackend.figure_format = 'svg'
# define the model options and run

kaydet=True

options = {
    'model': 'cfg/yolov2-tiny-voc-9c.cfg',
    'load': 4750,
    'threshold': 0.15,
    'gpu': 0.7
}

tfnet = TFNet(options)
colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]

if kaydet:
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('parkcam.avi',fourcc, 20.0, (640,480))
capture = cv2.VideoCapture('Train_Data\\Videos\\parkcam_Trim.mp4')
cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
cv2.resizeWindow('frame',640,480)

while capture.isOpened():
    stime = time.time()
    ret, frame = capture.read()
    if ret:
        results = tfnet.return_predict(frame)
        for color, result in zip(colors, results):
            tl = (result['topleft']['x'], result['topleft']['y'])
            br = (result['bottomright']['x'], result['bottomright']['y'])
            label = result['label']
            confidence = result['confidence']
           # text = '{}: {:.0f}%'.format(label, confidence * 100)
            text = '{}'.format(label)
            frame = cv2.rectangle(frame, tl, br, color, 5)
            frame = cv2.putText(
                frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
        cv2.imshow('frame', frame)
        if kaydet:
            kayitframe = cv2.resize(frame, (640,480))
            out.write(kayitframe)
        print('FPS {:.1f}'.format(1 / (time.time() - stime)))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
if kaydet:
    out.release()