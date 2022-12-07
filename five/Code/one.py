# 导入所需模块
import cv2
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import os
import numpy as np

# 定义必要函数

# 显示图片
def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey()
    cv2.destroyAllWindows()


# plt显示彩色图片
def plt_show0(img):
    b, g, r = cv2.split(img)
    img = cv2.merge([r, g, b])
    plt.imshow(img)
    plt.show()


# plt显示灰度图片
def plt_show(img):
    plt.imshow(img, cmap='gray')
    plt.show()


# 图像去噪灰度处理
def gray_guss(image):
    image = cv2.GaussianBlur(image, (3, 3), 0)
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return gray_image

# 读取待检测图片
origin_image = cv2.imread('../image/test2.png')
plt_show0(origin_image)