#!/usr/bin/python3
import os
from ctypes import *

os.environ["path"] += ";/"
lib = CDLL("libConnectorFactoryPythonBridge.dll", winmode = 0)

def opaque_ptr(name):
    cls = type(name, (Structure,), {})
    return POINTER(cls)


class ConnectorFactory(object):    
    def __init__(self, jsonName = "defaultConnector", func=lib.createConnectorFactory):
        self.Connector_type = opaque_ptr('Connector')

        lib.createConnectorFactory.argtypes = c_char_p,
        lib.createConnectorFactory.restype = self.Connector_type
        self.Connector = func(jsonName.encode())
    
    def __del__(self):
        print("Delete connector controller !")

    # === DeviceInterface(Connector) === #

    ##
    # @brief Initialize the suction tool.
    # @return Result of initialize().
    def initialize(self, func=lib.initializeConnector):
        if not self.Connector:
            raise RuntimeError
        lib.initializeConnector.argtypes = self.Connector_type,
        lib.initializeConnector.restype = c_int
        return func(self.Connector)        

    ##
    # @brief Connect to the suction tool.
    # @return Result of connect().
    def connect(self, func=lib.connectConnector):
        if not self.Connector:
            raise RuntimeError
        lib.connectConnector.argtypes = self.Connector_type,
        lib.connectConnector.restype = c_int
        return func(self.Connector) 

    ##
    # @brief Disconnect from the suction tool.
    # @return Result of disconnect().
    def disconnect(self, func=lib.disconnectConnector):
        if not self.Connector:
            raise RuntimeError
        lib.disconnectConnector.argtypes = self.Connector_type,
        lib.disconnectConnector.restype = c_int
        return func(self.Connector) 

    ##
    # @brief Reconnect to the suction tool.
    # @return Result of reconnect().
    def reconnect(self, func=lib.reconnectConnector):
        if not self.Connector:
            raise RuntimeError
        lib.reconnectConnector.argtypes = self.Connector_type,
        lib.reconnectConnector.restype = c_int
        return func(self.Connector)     

    ##
    # @brief Reload suction tool parameters.
    # @return Result of reloadParam().
    def reloadParam(self, func=lib.reloadParamConnector):
        if not self.Connector:
            raise RuntimeError
        lib.reloadParamConnector.argtypes = self.Connector_type,
        lib.reloadParamConnector.restype = c_int
        return func(self.Connector)     
    
    ## 
    # @brief Finalize the suction tool.
    #
    # Resets the simulated environment if the device is virtual.
    #
    # @return Result of finalize().
    def finalize(self, func=lib.finalizeConnector):
        if not self.Connector:
            raise RuntimeError
        lib.finalizeConnector.argtypes = self.Connector_type,
        lib.finalizeConnector.restype = c_int
        return func(self.Connector)     

    ##
    # @brief Stop any operation of the suction tool.
    # @return Result of stop().
    def stop(self, func=lib.stopConnector):
        if not self.Connector:
            raise RuntimeError
        lib.stopConnector.argtypes = self.Connector_type,
        lib.stopConnector.restype = c_int
        return func(self.Connector)  

    # === ConnectorInterface === #

    ##
    # @brief Open suction tool.
    # @return Result of open().
    def open(self, func=lib.openConnector):
        if not self.Connector:
            raise RuntimeError
        lib.openConnector.argtypes = self.Connector_type,
        lib.openConnector.restype = c_int
        return func(self.Connector)       

    ##
    # @brief Close suction tool.
    # @return Result of close().
    def close(self, func=lib.closeConnector):
        if not self.Connector:
            raise RuntimeError
        lib.closeConnector.argtypes = self.Connector_type,
        lib.closeConnector.restype = c_int

        return func(self.Connector)  

    ##
    # @brief Get connector namespace.
    # @return Namespace of the connector.
    def getDeviceNameSpace(self, func=lib.getDeviceNameSpaceConnector):
        if not self.Connector:
            raise RuntimeError
        lib.getDeviceNameSpaceConnector.argtypes = self.Connector_type,
        lib.getDeviceNameSpaceConnector.restype = c_char_p

        return func(self.Connector)
