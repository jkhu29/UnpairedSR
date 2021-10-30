import os

import numpy as np
import SimpleITK as sitk
import tfrecord

import cv2
import sys

from tfrecord.reader import tfrecord_loader


stride = 32


def clip(file_path):
    image_paths = file_path.split(".")[0]
    if os.path.exists(image_paths):
        return image_paths
    os.makedirs(image_paths)
    image = sitk.ReadImage(file_path)
    data = sitk.GetArrayFromImage(image)
    for i in range(data.shape[0]):
        out = sitk.GetImageFromArray(data[i, ...])
        sitk.WriteImage(out, os.path.join(image_paths, "{}.nii.gz".format(i+1)))
    return image_paths


def norm(file_path, maximum: int = 255, minimum: int = 0):
    image = sitk.ReadImage(file_path)
    resacleFilter = sitk.RescaleIntensityImageFilter()
    resacleFilter.SetOutputMaximum(maximum)
    resacleFilter.SetOutputMinimum(minimum)
    image = resacleFilter.Execute(image)
    data = sitk.GetArrayFromImage(image)
    return data


def make_data(data_path, cnt=0, split="train", size_image=64, kind="lr"):
    writer = tfrecord.TFRecordWriter("{}_".format(split) + kind + ".tfrecord")
    for file_name in os.listdir(data_path):
        file_path = clip(os.path.join(data_path, file_name))
        print("images dictionary: {}".format(file_path))
        for image_name in os.listdir(file_path):
            data = norm(os.path.join(file_path, image_name))[0]
            for x in np.arange(0, data.shape[0] - size_image + 1, stride):
                for y in np.arange(0, data.shape[1] - size_image + 1, stride):
                    data_part = data[int(x): int(x + size_image), int(y): int(y + size_image)].astype(np.uint8)
                    assert np.isnan(data_part).sum() == 0 and np.isinf(data_part).sum() == 0
                    if np.mean(data_part) > 50:
                        cnt += 1
                        writer.write({
                            "image": (data_part.tobytes(), "byte"),
                            "size": (size_image, "int"),
                        })
    writer.close()
    print("length of " + split + ": {}".format(cnt))
    return cnt


size_image = 32

for split in ["train", "valid"]:
    lr_path = "dataset/low/{}".format(split)
    hr_path = lr_path.replace("low", "high")
    lr_cnt = make_data(data_path=lr_path, split=split, size_image=32)
    hr_cnt = make_data(data_path=hr_path, split=split, kind="hr")
    cnt = min(lr_cnt, hr_cnt)
    description = {
        "image": "byte",
        "size": "int",
    }
    writer = tfrecord.TFRecordWriter("{}.tfrecord".format(split))
    lr_loader = tfrecord.tfrecord_loader("{}_lr.tfrecord".format(split), None, description)
    hr_loader = tfrecord.tfrecord_loader("{}_hr.tfrecord".format(split), None, description)
    for record in lr_loader:
        lr_data = record["image"]
        hr_data = next(iter(hr_loader))["image"]
        writer.write({
            "lr": (lr_data.tobytes(), "byte"),
            "hr": (hr_data.tobytes(), "byte"),
            "size": (size_image, "int"),
        })
    writer.close()
