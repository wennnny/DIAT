#!/usr/bin/python3
import os
from ctypes import *

os.environ["path"] += ";/"
lib = CDLL("libRobotFactoryPythonBridge.dll", winmode = 0)

def opaque_ptr(name):
    cls = type(name, (Structure,), {})
    return POINTER(cls)

class Pose_obj(Structure):
    _fields_ = [("x", c_double),
                ("y", c_double),
                ("z", c_double),
                ("rz", c_double)]
    
class Joint_obj(Structure):
    _fields_ = [("J1", c_double),
                ("J2", c_double),
                ("J3", c_double),
                ("J4", c_double)]

class PoseInfo():
    def __init__(self, x = 0, y = 0, z = 0, rz = 0):
        self.pose_p = None
        self.x = x
        self.y = y
        self.z = z
        self.rz = rz

class JointInfo():
    def __init__(self, J1 = 0, J2 = 0, J3 = 0, J4 = 0):
        self.joint_p = None
        self.J1 = J1
        self.J2 = J2
        self.J3 = J3
        self.J4 = J4

class RobotFactory(object): 
    def __init__(self, jsonName = "defaultRobot", func=lib.createRobotFactory):    
        self.Robot_type = opaque_ptr('Robot')

        lib.createRobotFactory.argtypes = c_char_p,
        lib.createRobotFactory.restype = self.Robot_type
        self.Robot = func(jsonName.encode())

    def __del__(self):
        print("Delete robot controller !")

    ##
    # @brief Create a pose object.
    # @param x  x value of pose.
    # @param y  y value of pose.
    # @param z  z value of pose.
    # @param rz  rz value of pose. 
    # @return a instance of PoseInfo class.
    def creatPose(self, x, y, z, rz, func=lib.newPose):
        lib.newPose.argtypes = ()
        lib.newPose.restype = c_void_p
        pose = func()

        pose_new = PoseInfo(x, y, z, rz)
        pose_new.pose_p = pose

        self.__setPose_Dll(pose_new)
        return pose_new

    ##
    # @brief Register a pose for HAL
    # @param Pose  Specific pose.
    def __setPose_Dll(self, Pose, func=lib.setPoseData):
        lib.setPoseData.argtypes = [c_void_p, c_double, c_double, c_double, c_double]
        lib.setPoseData.restype = None

        return func(Pose.pose_p, Pose.x, Pose.y, Pose.z, Pose.rz)

    # === DeviceInterface(Robot) === #

    ##
    # @brief Initialize the robot.
    # @return Result of initialize().
    def initialize(self, func=lib.initializeRobot):
        if not self.Robot:
            raise RuntimeError
        lib.initializeRobot.argtypes = self.Robot_type,
        lib.initializeRobot.restype = c_int
        return func(self.Robot)

    ##
    # @brief Connect to the robot.
    # @return Result of connect().
    def connect(self, func=lib.connectRobot):
        if not self.Robot:
            raise RuntimeError
        lib.connectRobot.argtypes = self.Robot_type,
        lib.connectRobot.restype = c_int
        return func(self.Robot)

    ##
    # @brief Disconnect from the robot.
    # @return Result of disconnect().
    def disconnect(self, func=lib.disconnectRobot):
        if not self.Robot:
            raise RuntimeError
        lib.disconnectRobot.argtypes = self.Robot_type,
        lib.disconnectRobot.restype = c_int
        return func(self.Robot)

    ##
    # @brief Reconnect to the robot.
    # @return Result of reconnect().
    def reconnect(self, func=lib.reconnectRobot):
        if not self.Robot:
            raise RuntimeError
        lib.reconnectRobot.argtypes = self.Robot_type,
        lib.reconnectRobot.restype = c_int
        return func(self.Robot)

    ##
    # @brief Reload robot parameters.
    # @return Result of reloadParam().
    def reloadParam(self, func=lib.reloadParamRobot):
        if not self.Robot:
            raise RuntimeError
        lib.reloadParamRobot.argtypes = self.Robot_type,
        lib.reloadParamRobot.restype = c_int
        return func(self.Robot)
    
    ##
    # @brief Finalize the robot.
    #
    # Resets the simulated environment if the device is virtual.
    #
    # @return Result of finalize().
    def finalize(self, func=lib.finalizeRobot):
        if not self.Robot:
            raise RuntimeError
        lib.finalizeRobot.argtypes = self.Robot_type,
        lib.finalizeRobot.restype = c_int
        return func(self.Robot)

    ##
    # @brief Stop any operation of the robot.
    # @return Result of stop().
    def stop(self, func=lib.stopRobot):
        if not self.Robot:
            raise RuntimeError
        lib.stopRobot.argtypes = self.Robot_type,
        lib.stopRobot.restype = c_int
        return func(self.Robot)

    # === RobotInterface === #
    ##
    # @brief Clear the robot error state.
    # @return Result of alarmReset().
    def alarmReset(self, func=lib.alarmResetRobot):
        if not self.Robot:
            raise RuntimeError
        lib.stopRobot.argtypes = self.Robot_type,
        lib.stopRobot.restype = c_int
        return func(self.Robot)

    ##
    # @brief Set the robot speed.
    # @param type_list  A list that determines the speed-related parameters to be set (SPDL, ACCL, DECL, SPDJ, ACCJ, DECJ).
    # @param values  A list of speed values corresponding to the order of type_list. 
    # @return Result of setSpeed().
    def setSpeed(self, type_list, values, func=lib.setSpeedRobot):
        if not self.Robot:
            raise RuntimeError
        lib.setSpeedRobot.argtypes = [self.Robot_type, c_int*len(type_list), c_double*len(values), c_int]
        lib.setSpeedRobot.restype = c_int

        if len(type_list) != len(values):
            print("setting_type's number not match setting_value")
            return False

        return func(self.Robot, (c_int*len(type_list))(*type_list), (c_double*len(values))(*values), len(type_list))

    ##
    # @brief Set the robot pass mode.
    # @param mode  Choose which pass mode to use.
    # @param value  Value corresponding to pass mode.
    # @return Result of setPassMode().
    def setPassMode(self, mode, value, func=lib.setPassModeRobot):
        if not self.Robot:
            raise RuntimeError
        lib.setPassModeRobot.argtypes = [self.Robot_type, c_char_p, c_float]
        lib.setPassModeRobot.restype = c_int

        return func(self.Robot, mode.encode(), value)

    ##
    # @brief Get the user frame definition.
    # @param index  The index of the user frame.
    # @param transform  The transform of the user frame.
    # @return Result of getUserFrame().
    def getUserFrame(self, index, transform, func=lib.getUserFrameRobot):
        if not self.Robot:
            raise RuntimeError
        lib.getUserFrameRobot.argtypes = [self.Robot_type, c_int, POINTER(Pose_obj)]
        lib.getUserFrameRobot.restype = c_int 

        pose_cls = Pose_obj() 
        res = func(self.Robot, index, pose_cls)

        transform.x = pose_cls.x
        transform.y = pose_cls.y
        transform.z = pose_cls.z
        transform.rz = pose_cls.rz

        return res

    ##
    # @brief Get the tool frame definition.
    # @param index  The index of the tool frame.
    # @param transform  The transform of the tool frame.
    # @return Result of getToolFrame().
    def getToolFrame(self, index, transform, func=lib.getToolFrameRobot):
        if not self.Robot:
            raise RuntimeError
        lib.getToolFrameRobot.argtypes = [self.Robot_type, c_int, POINTER(Pose_obj)]
        lib.getToolFrameRobot.restype = c_int  

        pose_cls = Pose_obj() 
        res = func(self.Robot, index, pose_cls)

        transform.x = pose_cls.x
        transform.y = pose_cls.y
        transform.z = pose_cls.z
        transform.rz = pose_cls.rz

        return res        

    ##
    # @brief Set the user frame definition.
    # @param index  The index of the new user frame.
    # @param p0  Origin for the new UserFrame.
    # @param px  The point where the new UserFrame extends along the origin in the X direction.
    # @param py  The point where the new UserFrame extends along the origin in the Y direction.
    # @param referenceFrameIndex  The user frame index of p0, px, py. 
    # @return Result of setUserFrame().
    def setUserFrame(self, index, p0, px, py, referenceFrameIndex, func=lib.setUserFrameRobot):
        if not self.Robot:
            raise RuntimeError
        lib.setUserFrameRobot.argtypes = [self.Robot_type, c_int, c_void_p, c_void_p, c_void_p, c_int]
        lib.setUserFrameRobot.restype = c_int
        return func(self.Robot, index, p0.pose_p, px.pose_p, py.pose_p, referenceFrameIndex)

    ##
    # @brief Set the tool frame definition.
    # @param index  The index of the new tool frame.
    # @param transform The transform of the tool frame.
    # @return Result of setToolFrame().
    def setToolFrame(self, index, transform, func=lib.setToolFrameRobot):
        if not self.Robot:
            raise RuntimeError
        lib.setToolFrameRobot.argtypes = [self.Robot_type, c_int, c_void_p]
        lib.setToolFrameRobot.restype = c_int
        return func(self.Robot, index, transform.pose_p)

    ##
    # @brief Switch user frame and tool frame indexs.
    # @param UF_Index  User frame index. If UFindex is negative, won't switch the frame index.
    # @param TF_Index  Tool frame index. If TFindex is negative, won't switch the frame index.
    # @return Result of switchFrameIndex().
    def switchFrameIndex(self, UF_Index, TF_Index, func=lib.switchFrameIndexRobot):
        if not self.Robot:
            raise RuntimeError
        lib.switchFrameIndexRobot.argtypes = [self.Robot_type, c_int, c_int]
        lib.switchFrameIndexRobot.restype = c_int    
        return func(self.Robot, UF_Index, TF_Index)

    ##
    # @brief Moves the robot to the specific pose.
    # @param type  The type that determines how the robot moves (type: 0 => MovL , 1=> MovP).
    # @param target  Specific pose.
    # @param isPass  Choose whether to PASS.
    # @param block  Determines whether to wait for the robot to complete the command after sending the move command.
    # @return Result of absMove().
    def absMove(self, type, target, isPass = False, block = True, func=lib.absMoveRobot):
        if not self.Robot:
            raise RuntimeError
        lib.absMoveRobot.argtypes = [self.Robot_type, c_int, c_void_p, c_bool, c_bool]
        lib.absMoveRobot.restype = c_int

        return func(self.Robot, type, target.pose_p, isPass, block)

    ##
    # @brief Jump to the specific pose.
    # @param target  Specific pose.
    # @param safe_height  The safety height of the robot when jumping. 
    # @param block  Determines whether to wait for the robot to complete the command after sending the move command.
    # @return Result of jump().
    def jump(self, target, safe_height, block = True, func=lib.jumpRobot):
        if not self.Robot:
            raise RuntimeError
        lib.jumpRobot.argtypes = [self.Robot_type, c_void_p, c_double, c_bool]
        lib.jumpRobot.restype = c_int
        return func(self.Robot, target.pose_p, safe_height, block)

    ##
    # @brief Get current pose.
    # @param currentPose  The current pose that obtained from robot.
    # @return Result of getPose().
    def getPose(self, currentPose, func=lib.getPoseRobot):
        if not self.Robot:
            raise RuntimeError
        lib.getPoseRobot.argtypes = [self.Robot_type, POINTER(Pose_obj)]
        lib.getPoseRobot.restype = c_int

        pose_cls = Pose_obj()
        res = func(self.Robot, pose_cls)

        currentPose.x = pose_cls.x
        currentPose.y = pose_cls.y
        currentPose.z = pose_cls.z
        currentPose.rz = pose_cls.rz

        return res
    
    ###
    # @brief Get current JointState.
    # @param currentJoint  The current joint state that obtained from robot.
    # @return Result of getJointState().
    def getJointState(self, currentJoint, func=lib.getJointStateRobot):
        if not self.Robot:
            raise RuntimeError
        lib.getJointStateRobot.argtypes = [self.Robot_type, POINTER(Joint_obj)]
        lib.getJointStateRobot.restype = c_int

        joint_cls = Joint_obj()
        res = func(self.Robot, joint_cls)

        currentJoint.J1 = joint_cls.J1
        currentJoint.J2 = joint_cls.J2
        currentJoint.J3 = joint_cls.J3
        currentJoint.J4 = joint_cls.J4

        return res
    
    ###
    # @brief Get robot status.
    # @return Result of getRobotStatus() (true -> busy, false -> idle).
    def getRobotStatus(self, func = lib.getRobotStatus):
        if not self.Robot:
            raise RuntimeError
        lib.getRobotStatus.argtypes = self.Robot_type,
        lib.getRobotStatus.restype = c_bool

        return func(self.Robot)

    ##
    # @brief Get robot namespace.
    # @return Namespace of the robot.
    def getDeviceNameSpace(self, func=lib.getDeviceNameSpaceRobot):
        if not self.Robot:
            raise RuntimeError
        lib.getDeviceNameSpaceRobot.argtypes = self.Robot_type,
        lib.getDeviceNameSpaceRobot.restype = c_char_p

        return func(self.Robot)
