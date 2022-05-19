import os
import pathlib
import platform
import cv2
import numpy as np
import time


class ObjectDetection(object):

    def __init__(self):

        self.yoloNet = cv2.dnn.readNet(
            "yolov4-tiny.weights",
            "yolov4-tiny.cfg",
        )
        with open("coco.names", "r") as f:
            self.objectClasses = [line.strip() for line in f.readlines()]

        # Get the name of al layers of the model
        self.layersNames = self.yoloNet.getLayerNames()
        # Get index of the output layers
        self.outputLayers = [self.layersNames[i[0] - 1] for i in self.yoloNet.getUnconnectedOutLayers()]
        self.colors = np.random.uniform(0, 255, size=(len(self.objectClasses), 3))
        self.font = cv2.FONT_HERSHEY_SIMPLEX

    def yoloObjectDetection(self, frame=None):

        height, width, channels = frame.shape
        detectObjectsBlob = cv2.dnn.blobFromImage(frame,
                                                  0.00392, (320, 320), (0, 0, 0), True, crop=False)
        self.yoloNet.setInput(detectObjectsBlob)

        predictedObjects = self.yoloNet.forward(self.outputLayers)
        drawBoxes = []
        confidences = []
        objectClassesIds = []
        for eachobject in predictedObjects:
            for detection in eachobject:
                scores = detection[5:]
                objectClassesId = np.argmax(scores)
                confidence = scores[objectClassesId]
                if confidence > 0.2:
                    centerX = int(detection[0] * width)
                    centerY = int(detection[1] * height)
                    w = int(detection[3] * width)
                    h = int(detection[4] * height)
                    x = int(centerX - w / 2)
                    y = int(centerY - h / 2)
                    drawBoxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    objectClassesIds.append(objectClassesId)

        indexOfPassObjects = cv2.dnn.NMSBoxes(drawBoxes, confidences, 0.5, 0.4)

        for i in range(len(drawBoxes)):
            if i in indexOfPassObjects:
                x, y, w, h = drawBoxes[i]
                label = str(self.objectClasses[objectClassesIds[i]])
                confidence = confidences[i]
                color = self.colors[objectClassesIds[i]]
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                cv2.putText(frame,
                            label + " " + str(round(confidence, 2)),
                            (x, y + 30),
                            self.font, 1, color, 3)

        return frame
