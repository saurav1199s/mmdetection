_base_ = "./faster_rcnn_r50_fpn_1x_coco.py"

dataset_type = 'CocoDataset'
classes = ("Ignore", "Pedestrian", "People", "Bicycle", "Car", "Van", "Truck", "Tricycle", "Awning-tricycle", "Bus", "Motor", "Others")
data = dict(
    samples_per_gpu=2,
    workers_per_gpu=2,
    train=dict(
        type=dataset_type,
        # explicitly add your class names to the field `classes`
        classes=classes,
        ann_file='VisDrone2019-DET-train/annotations.json',
        img_prefix='VisDrone2019-DET-train/images'),
    val=dict(
        type=dataset_type,
        # explicitly add your class names to the field `classes`
        classes=classes,
        ann_file='VisDrone2019-DET-val/annotations.json',
        img_prefix='VisDrone2019-DET-val/images'),
    test=dict(
        type=dataset_type,
        # explicitly add your class names to the field `classes`
        classes=classes,
        ann_file='VisDrone2019-DET-test/annotations.json',
        img_prefix='VisDrone2019-DET-test/images'))

# 2. model settings

# explicitly over-write all the `num_classes` field from default 80 to 5.
model = dict(
    roi_head=dict(
        bbox_head=[
            dict(
                type='Shared2FCBBoxHead',
                # explicitly over-write all the `num_classes` field from default 80 to 5.
                num_classes=12),
            dict(
                type='Shared2FCBBoxHead',
                # explicitly over-write all the `num_classes` field from default 80 to 5.
                num_classes=12),
            dict(
                type='Shared2FCBBoxHead',
                # explicitly over-write all the `num_classes` field from default 80 to 5.
                num_classes=12)],
    # explicitly over-write all the `num_classes` field from default 80 to 5.
#     mask_head=dict(num_classes=12)))

load_from = "http://download.openmmlab.com/mmdetection/v2.0/faster_rcnn/faster_rcnn_r50_caffe_fpn_1x_coco/faster_rcnn_r50_caffe_fpn_1x_coco_bbox_mAP-0.378_20200504_180032-c5925ee5.pth"
