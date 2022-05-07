import cv2
import os

if __name__ == '__main__':
    for dir in os.listdir(os.getcwd()):
        if os.path.isdir(os.path.join(os.getcwd(), dir)):
            for file in os.listdir(os.path.join(os.getcwd(), dir)):
                if file.endswith('.jpeg'):
                    img = cv2.imread(os.path.join(os.getcwd(), dir, file))
                    img = cv2.resize(img, (224, 224))
                    cv2.imwrite(os.path.join(os.getcwd(), dir, file), img)