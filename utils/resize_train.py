import cv2
import os

if __name__ == '__main__':
    sub_path = ['masked', 'unmasked']

    for d in os.listdir(os.getcwd()):
        path0 = os.path.join(os.getcwd(), d)
        if(os.path.isdir(path0)):
            for sub in sub_path:
                path1 = os.path.join(path0, sub)
                for file in os.listdir(path1):
                    path2 = os.path.join(path1, file)
                    img = cv2.imread(path2)
                    img = cv2.resize(img, (224, 224))
                    cv2.imwrite(path2, img)
