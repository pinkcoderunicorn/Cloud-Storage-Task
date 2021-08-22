import cv2
import dropbox
import os
import time

def take_snapshot():
    camera = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = camera.read()
        print(ret)
        cv2.imwrite("cam1.jpg", frame)
        result = False
    camera.release()
    cv2.destroyAllWindows()

take_snapshot()

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx= dropbox.Dropbox(self.access_token)

        f= open(file_from, 'rb')
        dbx.files_upload(f.read(),file_to)

def upload_camera_image():
    access_token='-Mw059HNExQAAAAAAAAAAdLiKr_VFcSKa6jvcDleHx9tJKuRU8WH44q7xPeFw4zJ'
    transferData = TransferData(access_token)
    cwd = os.getcwd()
    cur = str(time.time())
    file_from = cwd+"/cam1.jpg"
    file_to = "/cam"+cur+".jpg"
    transferData.upload_file(file_from, file_to)

    print("file has been moved")

start = time.time()
while(True):
    if((time.time()-start)<=10):
        upload_camera_image()


