import cv2
from darkflow.net.build import TFNet

options = {
    'model': 'cfg/yolov2-tiny-voc-1c.cfg',
    'load': 875,
    'threshold': 0.01,
    'gpu': 0.7
}

tfnet = TFNet(options)

img = cv2.imread('sample_img/000028.png', cv2.IMREAD_COLOR)

result = tfnet.return_predict(img)

for res in result:
    tl = (res['topleft']['x'], res['topleft']['y'])
    br = (res['bottomright']['x'], res['bottomright']['y'])
    label = res['label']
    confidence = res['confidence']
    text = '{}: {:.0f}%'.format(label, confidence * 100)
    img = cv2.rectangle(img, tl, br, (0, 255, 0), 1)
    img = cv2.putText(img, text, tl, cv2.FONT_HERSHEY_COMPLEX,0.5, (255, 255, 255), 1)
cv2.imwrite('sonuc.png',img)

cv2.imshow('sonuc',img)
cv2.waitKey(0)
cv2.destroyAllWindows()