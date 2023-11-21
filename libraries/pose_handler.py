#!/usr/bin/python3
import csv
import json
import os, sys
import copy
import time

class PoseHandler:
    def __init__(self, robot):
        self.robot = robot
        self.csv_content = []
        self.json_content = [["Key", "x", "y", "z", "rz"]]
        self.extension = ""

    def get_file_extension(self, filename):
        _, extension = os.path.splitext(filename)
        return extension

    def loadPoses(self, filename):
        self.extension = self.get_file_extension(filename)
        if self.extension == ".json":
            try:
                with open(filename, 'r') as json_file:
                    json_data = json.load(json_file)
                    for key, values in json_data.items():
                        row = [key]
                        for value in values.values():
                            row.append(str(value))
                        self.json_content.append(row)
#                    for row in self.json_content:
#                        print(row)
            except FileNotFoundError:
                self.json_content = None
        elif self.extension == ".csv":
            try:
                with open(filename, newline='') as file:
                    csv_reader = csv.reader(file)
                    for row in csv_reader:
                        self.csv_content.append(row)
            except FileNotFoundError:
                self.csv_content = None
        else:
            print("File type is not recognized.")

    def getPose(self, search_string):
        if self.extension == ".json":
            if self.json_content is None:
                return None
#            for row in self.json_content:
#                print(row)
            for row_idx, row in enumerate(self.json_content):
                for col_idx, cell in enumerate(row):
                    if cell == search_string:
                        return self.robot.creatPose(
                    float(self.json_content[row_idx][col_idx + 1]),
                    float(self.json_content[row_idx][col_idx + 2]),
                    float(self.json_content[row_idx][col_idx + 3]),
                    float(self.json_content[row_idx][col_idx + 4]))
        elif self.extension == ".csv":
            if self.csv_content is None:
                return None
            for row_idx, row in enumerate(self.csv_content):
                for col_idx, cell in enumerate(row):
                    if cell == search_string:
                        return self.robot.creatPose(
                    float(self.csv_content[row_idx][col_idx + 1]),
                    float(self.csv_content[row_idx][col_idx + 2]),
                    float(self.csv_content[row_idx][col_idx + 3]),
                    float(self.csv_content[row_idx][col_idx + 6]))
        else:
            return None

    def createToolFrame(self, x, y, z, rz):
        return self.robot.creatPose(x, y, z, rz)

    def createUserFramePoses(self, oriX, oriY, oriZ, oriRZ, xPoseX, xPoseY, xPoseZ, xPoseRZ, yPoseX, yPoseY, yPoseZ, yPoseRZ):
        return self.robot.creatPose(oriX, oriY, oriZ, oriRZ), self.robot.creatPose(xPoseX, xPoseY, xPoseZ, xPoseRZ), self.robot.creatPose(yPoseX, yPoseY, yPoseZ, yPoseRZ)
