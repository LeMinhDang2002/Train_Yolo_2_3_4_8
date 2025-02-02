# Dataset config

dataset_cfg = {
    'voc': {
        'data_name': 'VOCdevkit',
        'num_classes': 20,
        'class_indexs': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                         10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        'class_names': ('aeroplane', 'bicycle', 'bird', 'boat',
                         'bottle', 'bus', 'car', 'cat', 'chair',
                         'cow', 'diningtable', 'dog', 'horse',
                         'motorbike', 'person', 'pottedplant',
                         'sheep', 'sofa', 'train', 'tvmonitor'),
    },

    'coco':{
        'data_name': 'COCO',
        'num_classes': 80,
        'class_indexs': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20,
                         21, 22, 23, 24, 25, 27, 28, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                         41, 42, 43, 44, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
                         59, 60, 61, 62, 63, 64, 65, 67, 70, 72, 73, 74, 75, 76, 77, 78, 79,
                         80, 81, 82, 84, 85, 86, 87, 88, 89, 90],
        'class_names': ('background',
                        'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck',
                        'boat', 'traffic light', 'fire hydrant', 'street sign', 'stop sign',
                        'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
                        'elephant', 'bear', 'zebra', 'giraffe', 'hat', 'backpack', 'umbrella',
                        'shoe', 'eye glasses', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis',
                        'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove',
                        'skateboard', 'surfboard', 'tennis racket', 'bottle', 'plate', 'wine glass',
                        'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich',
                        'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair',
                        'couch', 'potted plant', 'bed', 'mirror', 'dining table', 'window', 'desk',
                        'toilet', 'door', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
                        'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'blender', 'book',
                        'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'),
    },

    'widerface':{
        'data_name': 'WiderFace',
        'num_classes': 1,
        'class_indexs': [0],
        'class_names': ('face',),
    },

    'crowdhuman':{
        'data_name': 'CrowdHuman',
        'num_classes': 1,
        'class_indexs': [0],
        'class_names': ('person',),
    },

    'customed':{
        'data_name': 'AnimalDataset',
        'num_classes': 9,
        'class_indexs': [0, 1, 2, 3, 4, 5, 6, 7, 8],
        'class_names': ('bird', 'butterfly', 'cat', 'cow', 'dog', 'lion', 'person', 'pig', 'tiger', ),
    },
    
    'plate_number':{
        'data_name': 'PlateLicense',
        'num_classes': 1,
        'class_indexs': [0],
        'class_names': ('motobike',),
    },

    'character':{
        'data_name': 'Character',
        'num_classes': 36,
        'class_indexs': [0,   1,   2,   3,   4,   5,   6,   7,   8,   9,
                         10,  11,  12,  13,  14,  15,  16,  17,  18,  19,
                         20,  21,  22,  23,  24,  25,  26,  27,  28,  29,
                         30,  31,  32,  33,  34,  35],
        'class_names': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                        'U', 'V', 'W', 'X', 'Y', 'Z'],
    },

}