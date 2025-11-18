

import cv2


from il import ImageLabel

mapIL = ImageLabel.from_file('MAP.IL')


vc = cv2.VideoCapture(0)
vc.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
vc.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
cv2.namedWindow('USB Camera', cv2.WINDOW_NORMAL)
try:
    while vc.isOpened():
        ret, frame = vc.read()
        if ret:
            degree, loc = mapIL.search(frame)
            cv2.rectangle(frame, loc, (loc[0] + mapIL.TargetWidth, loc[1] + mapIL.TargetHeight), (0, 255, 0), 2)
            cv2.rectangle(frame, 
                          (mapIL.RangeX, mapIL.RangeY), 
                          (mapIL.RangeX + mapIL.RangeWidth, mapIL.RangeY + mapIL.RangeHeight), 
                          (0, 0, 255), 2)
            # cv2.putText(frame, f'{degree * 100:.2f}%', loc, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('USB Camera', frame)
            if cv2.waitKey(1) & 0xff  == ord('q'):
                break
        else:
            break
except Exception as e:
    
    vc.release()
    cv2.destroyAllWindows()
    raise e
    
vc.release()
cv2.destroyAllWindows()
