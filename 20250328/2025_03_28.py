import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

#이미지 불러오기
image_path = "C:/Users/user/Downloads/img.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

#히스토그램 평활화 적용
equalized_image = cv2.equalizeHist(image)

#결과 이미지 저장
equalized_image_path = "C:/Users/user/Downloads/equalized_img.jpg"
cv2.imwrite(equalized_image_path, equalized_image)

#결과 이미지 보기
Image.open(equalized_image_path)
