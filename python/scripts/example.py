#!/usr/bin/python3
"""example"""

import json
import os, sys
import copy
import time

sys.path.append("../../libraries")
from robot_factory import*
from camera_factory import*
from connector_factory import*
from pose_handler import*

controllerType = 0
pick_point_list = []
place_point_list = []

SpdL = 0
SpdJ = 3

try:
    scara = RobotFactory("robot1")
    camera = CameraFactory("camera1")
    connector = ConnectorFactory("connector1")

    print("================ initial ================")
    scara.initialize()
    camera.initialize()
    connector.initialize()
    print("================ connect ================")
    scara.connect()
    camera.connect()
    connector.connect()

    with open("../config/robot1.json") as Robot1:
        robot1 = json.load(Robot1)

    pose_handler = PoseHandler(scara)
    if robot1["controllerType"] == "VRCScaraVddImpl":
        print("Use Virtual Controller")
        pose_handler.loadPoses('../config/virtualPoint.json')
    elif robot1["controllerType"] == "DeltaScaraImpl":
        print("Use Real Controller")
        pose_handler.loadPoses('../config/realPoint.json')
    else:
        print("Unknow Controller type: ",controllerType)

    setting_type = [SpdL, SpdJ]
    setting_value = [robot1["SpdL"], robot1["SpdJ"]]
    scara.setSpeed(setting_type, setting_value)


    print("================ set points ================")
    initial_point = pose_handler.getPose('Initial')
    pnt_save_img = pose_handler.getPose('Snap')
    for i in range(0,4):
        pick_point_list.append(pose_handler.getPose('Pick' + str(i+1)))
        place_point_list.append(pose_handler.getPose('Place' + str(i+1)))


    print("========== Send pass Mode: ==========")
    scara.setPassMode("DISTANT", 10)

    print("================ move to initial point ================")    
    scara.absMove(1, initial_point, 0, True)

    current_pose = PoseInfo()
    scara.getPose(current_pose)
    print("Current Pose: ", current_pose.x, ", "
                          , current_pose.y, ", "
                          , current_pose.z, ", "
                          , current_pose.rz)
    
    current_joint = JointInfo()
    scara.getJointState(current_joint)
    print("Current Joint: ", current_joint.J1, ", "
                           , current_joint.J2, ", "
                           , current_joint.J3, ", "
                           , current_joint.J4)

    print("================ switch suerframe and toolframe ================")
    p0, px, py = pose_handler.createUserFramePoses(10, 10, 0, 0, 50, 10, 0, 0, 30, 30, 0, 0)
    scara.setUserFrame(1, p0, px, py, 0);
    tf = pose_handler.createToolFrame(20, 20, 0, 90)
    scara.setToolFrame(1, tf);

    transformUF = PoseInfo()
    transformTF = PoseInfo()
    scara.getUserFrame(1, transformUF)
    scara.getToolFrame(1, transformTF)
    print("UserFrame 1:", transformUF.x, ", ", transformUF.y, ", ", transformUF.z, ", ", transformUF.rz)
    print("ToolFrame 1:", transformTF.x, ", ", transformTF.y, ", ", transformTF.z, ", ", transformTF.rz)

    scara.switchFrameIndex(1, 0);
    scara.getPose(current_pose)
    print("Current Pose: ", current_pose.x, ", "
                          , current_pose.y, ", "
                          , current_pose.z, ", "
                          , current_pose.rz)
    scara.switchFrameIndex(0, 1);
    scara.getPose(current_pose)
    print("Current Pose: ", current_pose.x, ", "
                        , current_pose.y, ", "
                        , current_pose.z, ", "
                        , current_pose.rz)
    scara.switchFrameIndex(0, 0);
    scara.getPose(current_pose)
    print("Current Pose: ", current_pose.x, ", "
                          , current_pose.y, ", "
                          , current_pose.z, ", "
                          , current_pose.rz)

    print("========== Start Planning: ==========")
    for i in range(0,4):
        print("========== Move to Pick", i+1,"==========")
        scara.jump(pick_point_list[i], -60, False)

        while(scara.getRobotStatus()):
            pass
        connector.open()

        print("========== Move to Place", i+1,"==========")
        scara.jump(place_point_list[i], -60, True)
        connector.close()

    scara.absMove(1, pnt_save_img, 0, True)
    camera.saveImage("D:\\test_python.jpg")
    # back to initial point   
    scara.jump(initial_point, -60, True)

    print("========== disconnect ==========")
    connector.disconnect()
    camera.disconnect()
    scara.disconnect()
    print("========== finalize ==========")
    connector.finalize()
    camera.finalize()
    scara.finalize()

except Exception as ex:
    print("Error: ", ex)

    connector.disconnect()
    camera.disconnect()
    scara.disconnect()

    connector.finalize()
    camera.finalize()
    scara.finalize()
