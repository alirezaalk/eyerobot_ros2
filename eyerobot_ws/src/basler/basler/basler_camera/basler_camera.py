import numpy as np 
from pypylon import pylon
from pypylon import genicam
import cv2

# This camera transmits images from a connected basler camera
class BaslerCamera:
    def __init__(self):
        
        self.latest_frame = None
        self.camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
        self.camera.Close()
        self.start_camera()
        self.image_converter = pylon.ImageFormatConverter()
        self.image_converter.OutputPixelFormat = pylon.PixelType_RGB8packed
        self.image_converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
        # try: 
        #     self.camera.Open()
        # except:
        #     self.camera.Close()
    def start_camera(self):
        # print("Starting camera")
        self.camera.Open()
        self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)


    def stop_camera(self):
        print("Stopping camera")
        self.camera.StopGrabbing()
        self.camera.Close()

    def get_latest_frame(self) -> np.ndarray:
        
        try:
            
            self.latest_frame = self.camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
            # pylon_image = self.image_converter.Convert(camera_result)
            if self.latest_frame.GrabSucceeded():
                image = self.image_converter.Convert(self.latest_frame)
                print("SizeX: ", self.latest_frame.Width)
                # print("SizeY: ", self.latest_frame.Height)
                self.img = image.GetArray()
            #cv_image = image.GetArray()
            return self.img
        except genicam.GenericException as e : 
                # self.stop_camera()
                print ("genicam error")
        except Exception as e:
            print("Error called from")  
        
    
    def get_frames(self):
        while self.camera.IsGrabbing():
            self.grabResult = self.camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
            if self.grabResult.GrabSucceeded():
                #time.sleep(0.5)
                #print("SizeX: ", self.grabResult.Width)
                #print("SizeY: ", self.grabResult.Height)
                image = self.image_converter.Convert(self.grabResult)
                self.img = image.GetArray()
                self.width = 720
                self.height = 360
                dsize = (self.width, self.height)
                # resize image
                self.scaled_img = cv2.resize(self.img, dsize)
                # if VisionConfig().IMSHOW:
                cv2.imshow('frame', self.scaled_img)
                # if VisionConfig().IMSHOW_MASK:
                    # cv2.imshow('mask', self.scaled_img_mask)
                if cv2.waitKey(1) == ord('q'):
                    cv2.destroyAllWindows()
                    print("q is pressed. quit")
                    self.camera.Close()
                    break
    

def _test():
    cam = BaslerCamera()
    cam.start_camera()
    cam.get_frames()   

if __name__ == "__main__":
    _test()
    # im = cam.get_latest_frame()
    # cv2.imshow("image", im)
    # cv2.waitKey()
    # cv2.destroyWindow()
    # cam.stop_camera()
