#!/usr/bin/python3
import os
from ctypes import *

os.environ["path"] += ";/"
lib = CDLL("libCameraFactoryPythonBridge.dll", winmode = 0)

def opaque_ptr(name):
    cls = type(name, (Structure,), {})
    return POINTER(cls)

class CameraFactory(object):    
    def __init__(self, jsonName = "defaultCamera", func=lib.createCameraFactory):
        self.Camera_type = opaque_ptr('Camera')

        lib.createCameraFactory.argtypes = c_char_p,
        lib.createCameraFactory.restype = self.Camera_type
        self.Camera = func(jsonName.encode())

        self.imageWidth = -1
        self.imageHeight = -1
        self.imageChannel = -1

    def __del__(self):
        print("Delete Camera controller !")

    # === DeviceInterface(Camera) === #
    ##
    # @brief Initialize the camera.
    # @return Result of initialize().
    def initialize(self, func=lib.initializeCamera):
        if not self.Camera:
            raise RuntimeError
        lib.initializeCamera.argtypes = self.Camera_type,
        lib.initializeCamera.restype = c_int
        return func(self.Camera)        

    ##
    # @brief Connect to the camera.
    # @return Result of connect().
    def connect(self, func=lib.connectCamera):
        if not self.Camera:
            raise RuntimeError
        lib.connectCamera.argtypes = self.Camera_type,
        lib.connectCamera.restype = c_int
        res = func(self.Camera) 
        _ ,self.imageWidth = self.getWidth()
        _ ,self.imageHeight = self.getHeight()
        _ ,self.imageChannel = self.getChannel()
        return res

    ##
    # @brief Disconnect from the camera.
    # @return Result of disconnect().
    def disconnect(self, func=lib.disconnectCamera):
        if not self.Camera:
            raise RuntimeError
        lib.disconnectCamera.argtypes = self.Camera_type,
        lib.disconnectCamera.restype = c_int
        return func(self.Camera) 

    ##
    # @brief Reconnect to the camera.
    # @return Result of reconnect().
    def reconnect(self, func=lib.reconnectCamera):
        if not self.Camera:
            raise RuntimeError
        lib.reconnectCamera.argtypes = self.Camera_type,
        lib.reconnectCamera.restype = c_int
        return func(self.Camera)     

    ##
    # @brief Reload camera parameters.
    # @return Result of reloadParam().
    def reloadParam(self, func=lib.reloadParamCamera):
        if not self.Camera:
            raise RuntimeError
        lib.reloadParamCamera.argtypes = self.Camera_type,
        lib.reloadParamCamera.restype = c_int
        return func(self.Camera)     

    ##
    # @brief Finalize the camera.
    #
    # Resets the simulated environment if the device is virtual.
    #
    # @return Result of finalize().
    def finalize(self, func=lib.finalizeCamera):
        if not self.Camera:
            raise RuntimeError
        lib.finalizeCamera.argtypes = self.Camera_type,
        lib.finalizeCamera.restype = c_int
        return func(self.Camera)     

    ##
    # @brief Stop any operation of the camera.
    # @return Result of stop().
    def stop(self, func=lib.stopCamera):
        if not self.Camera:
            raise RuntimeError
        lib.stopCamera.argtypes = self.Camera_type,
        lib.stopCamera.restype = c_int
        return func(self.Camera)  

    # === CameraInterface === #
    ##
    # @brief Get image buffer.
    # @return Result of getImageBuffer(), The buffer obtained from the camera.
    def getImageBuffer(self, func=lib.getImageBufferCamera):
        if not self.Camera:
            raise RuntimeError
        bufferSize = self.imageWidth*self.imageHeight*self.imageChannel
        lib.getImageBufferCamera.argtypes = [self.Camera_type, POINTER(c_ubyte*(bufferSize))]
        lib.getImageBufferCamera.restype = c_int
        buffer = (c_ubyte*(bufferSize))()
        res = func(self.Camera, byref(buffer))
        buffer = bytes(buffer) 
        return res, buffer  
    
    ##
    # @brief Save an image at the specified path.
    # @param imagePath  The path to save the image.
    # @return Result of saveImage().
    def saveImage(self, imagePath, func=lib.saveImageCamera):
        if not self.Camera:
            raise RuntimeError
        lib.saveImageCamera.argtypes = [self.Camera_type, c_void_p]
        lib.saveImageCamera.restype = c_int
        return func(self.Camera, imagePath.encode('utf-8'))
    
    ##
    # @brief Get gain.
    # @return Result of getGain(), the gain obtained from the camera.
    def getGain(self, func=lib.getGainCamera):
        if not self.Camera:
            raise RuntimeError
        lib.getGainCamera.argtypes = [self.Camera_type, POINTER(c_double)]
        lib.getGainCamera.restype = c_int  
        gain = c_double()
        res = func(self.Camera, byref(gain))
        return res, float(gain.value)

    ##
    # @brief Set gain.
    # @param value  gain value
    # @return Result of setGain().
    def setGain(self, value, func=lib.setGainCamera):
        if not self.Camera:
            raise RuntimeError
        lib.setGainCamera.argtypes = [self.Camera_type, c_double]
        lib.setGainCamera.restype = c_int  
        return func(self.Camera, value)

    ##
    # @brief Get exposure time.
    # @return Result of getExposureTime(), the exposure time obtained from the camera.
    def getExposureTime(self, func=lib.getExposureTimeCamera):
        if not self.Camera:
            raise RuntimeError  
        lib.getExposureTimeCamera.argtypes = [self.Camera_type, POINTER(c_double)]
        lib.getExposureTimeCamera.restype = c_int  
        exposureTime = c_double()
        res = func(self.Camera, byref(exposureTime))
        return res, float(exposureTime.value)
 
    ##
    # @brief Set exposure time.
    # @param value  exposure time.
    # @return Result of setExposureTime().
    def setExposureTime(self, value, func=lib.setExposureTimeCamera):    
        if not self.Camera:
            raise RuntimeError  
        lib.setExposureTimeCamera.argtypes = [self.Camera_type, c_double]
        lib.setExposureTimeCamera.restype = c_int  
        return func(self.Camera, value)          

    ##
    # @brief Get width.
    # @return Result of getWidth(), the image width obtained from the camera.
    def getWidth(self, func=lib.getWidthCamera):
        if not self.Camera:
            raise RuntimeError 
        lib.getWidthCamera.argtypes = [self.Camera_type, POINTER(c_int)]
        lib.getWidthCamera.restype = c_int  
        imageWidth = c_int()
        res = func(self.Camera, byref(imageWidth))
        return res, int(imageWidth.value)

    ##
    # @brief Get height.
    # @return Result of getHeight(), the image height obtained from the camera.
    def getHeight(self, func=lib.getHeightCamera):
        if not self.Camera:
            raise RuntimeError 
        lib.getHeightCamera.argtypes = [self.Camera_type, POINTER(c_int)]
        lib.getHeightCamera.restype = c_int  
        imageHeight = c_int()
        res = func(self.Camera, byref(imageHeight))
        return res, int(imageHeight.value)           

    ##
    # @brief Get channel.
    # @return Result of getChannel(), the image channel obtained from the camera.
    def getChannel(self, func=lib.getChannelCamera):  
        if not self.Camera:
            raise RuntimeError 
        lib.getChannelCamera.argtypes = [self.Camera_type, POINTER(c_int)]
        lib.getChannelCamera.restype = c_int  
        imageChannel = c_int()
        res = func(self.Camera, byref(imageChannel))
        return res, int(imageChannel.value)                                 
    
    ##
    # @brief Get camera namespace.
    # @return Namespace of the camera.
    def getDeviceNameSpace(self, func=lib.getDeviceNameSpaceCamera):
        if not self.Camera:
            raise RuntimeError
        lib.getDeviceNameSpaceCamera.argtypes = self.Camera_type,
        lib.getDeviceNameSpaceCamera.restype = c_char_p

        return func(self.Camera)
