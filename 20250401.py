import cv2 as cv
import sys
import matplotlib.pyplot as plt

img = cv.imread('C:/Users/user/Downloads/soccer/soccer.jpg')

if img is None:
    sys.exit('File not found')
    
cv.imshow('original_RGB', img)
cv.imshow('Upper left half', img[img.shape[0]//2 , img.shape[1]//2, :])
#cv.imshow('test', img[473 , 716, 2])
print(img.shape)
print(img.shape[0])
print(img.shape[0]//2)
print(img.shape[1]//2)
print(img[img.shape[0]//4:3*img.shape[0]//4, img.shape[1]//4:3*img.shape[1]//4,       :].shape)
# 행, 열 , 채널
cv.imshow('Center half', img[img.shape[0]//4:3*img.shape[0]//4, img.shape[1]//4:3*img.shape[1]//4,       :])

print(img.shape[0]//4)
# print(img[img.shape[0]//4:3*img.shape[0]//4, img.shape[1]//4:3*img.shape[1]//4, :1])
cv.imshow('R channel', img[:,:,2])
cv.imshow('G channel', img[:,:,1])
cv.imshow('B channel', img[:,:,0])

h=cv.calcHist([img], [2], None, [256],[0,256])
plt.plot(h,color='r',linewidth=1)

t,bin_img = cv.threshold(img[:,:,2], 0,255, cv.THRESH_BINARY+cv.THRESH_OTSU)
print('오츄 알고리즘이 찾은 최적 임곗값=', t)

cv.imshow('R channel', img[:, :, 2])
cv.imshow('R channel binarization', bin_img)

cv.waitKey()
cv.destroyAllWindows()
