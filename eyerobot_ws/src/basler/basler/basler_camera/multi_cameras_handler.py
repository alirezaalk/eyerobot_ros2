import os

from pypylon import genicam
from pypylon import pylon
import sys

class MultiCameras():
    def __init__(self):
        # Get the transport layer factory.
        self.tlFactory = pylon.TlFactory.GetInstance()
        self.devices = self.tlFactory.EnumerateDevices()
        
        if len(self.devices) == 0:
            print("Check the device connection")
        self.cameras = pylon.InstantCameraArray(min(len(self.devices), 2))
        for i, cam in enumerate(self.cameras):
            print(cam)
            cam.Attach(self.tlFactory.CreateDevice(self.devices[i]))
            print("Using device ", cam.GetDeviceInfo().Get)

            # print("Using device ", cam.GetDeviceInfo().GetModelName())
        # print("Using device ", self.cameras[0].GetDeviceInfo().GetModelName())
        print(self.cameras[0])
        self.cam0 = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateDevice(self.cameras[0]))
        #self.cam0.Open()
            # print("Using device ", cam.GetDeviceInfo().GetModelName())
           # Create an array of instant cameras for the found devices and avoid exceeding a maximum number of devices.
        self.cameras = pylon.InstantCameraArray(min(len(self.cameras), 2))
        # self.cameras[0].attach(tlFactory.Create)
        print(self.cameras[0])


if __name__ == "__main__":
    MultiCameras()