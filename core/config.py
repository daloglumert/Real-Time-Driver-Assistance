#! /usr/bin/env python
# coding=utf-8
from easydict import EasyDict as edict


__C                           = edict()

cfg                           = __C

__C.iou                       = 0.45

__C.score                     = 0.25

__C.size                      = 416

__C.output_format             = 'XVID'

__C.weights                   = './yolov4-416'

__C.YOLO                      = edict()

__C.YOLO.CLASSES              = "./data/classes/coco.names"
__C.YOLO.ANCHORS              = [12,16, 19,36, 40,28, 36,75, 76,55, 72,146, 142,110, 192,243, 459,401]
__C.YOLO.STRIDES              = [8, 16, 32]
__C.YOLO.XYSCALE              = [1.2, 1.1, 1.05]
