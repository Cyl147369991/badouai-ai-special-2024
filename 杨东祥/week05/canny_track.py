#!/usr/bin/env python
# encoding=gbk

'''
Canny边缘检测：优化的程序
'''
import cv2
import numpy as np


def CannyThreshold(lowThreshold):
    # 进行Canny边缘检测
    detected_edges = cv2.Canny(gray, lowThreshold, lowThreshold * ratio, apertureSize=kernel_size)

    # 用原始颜色添加到检测的边缘上。
    # 按位“与”操作。对于每个像素,将两幅输入图像相应位置的像素值分别进行按位“与”运算,输出的结果图像的对应像素值即为这两幅输入图像对应像素值的按位与结果。
    # src1和src2表示要进行按位“与”操作的两幅输入图像；
    #mask 是可选参数，如果指定了掩膜，则只对掩膜对应位置的像素进行按位“与”操作。函数的返回值表示按位“与”运算的结果。
    dst = cv2.bitwise_and(resized_image, resized_image, mask=detected_edges)
    cv2.imshow('Canny Result', dst)


lowThreshold = 0
max_lowThreshold = 100
ratio = 3
kernel_size = 3

img = cv2.imread("../sea.jpg")

# 获取显示器分辨率
screen_width = 2560
screen_height = 1440

# 调整图像大小，保持纵横比
aspect_ratio = img.shape[1] / img.shape[0]
if aspect_ratio > 1:  # 宽大于高
    new_width = screen_width
    new_height = int(screen_width / aspect_ratio)
else:  # 高大于宽
    new_height = screen_height
    new_width = int(screen_height * aspect_ratio)

# 调整图像大小
resized_image = cv2.resize(img, (new_width, new_height))

gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)  # 转换彩色图像为灰度图

cv2.namedWindow('canny result')

# 设置调节杠,
'''
下面是第二个函数，cv2.createTrackbar()
共有5个参数，其实这五个参数看变量名就大概能知道是什么意思了
第一个参数，是这个trackbar对象的名字
第二个参数，是这个trackbar对象所在面板的名字
第三个参数，是这个trackbar的默认值,也是调节的对象
第四个参数，是这个trackbar上调节的范围(0~count)
第五个参数，是调节trackbar时调用的回调函数名
'''
cv2.createTrackbar('Min threshold', 'canny result', lowThreshold, max_lowThreshold, CannyThreshold)

CannyThreshold(0)  # initialization
if cv2.waitKey(0) == 27:  # wait for ESC key to exit cv2
    cv2.destroyAllWindows()
