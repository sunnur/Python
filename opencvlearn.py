import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

#图像读取与显示
def imgShow(img):
    if img.ndim == 2:
        plt.imshow(img, cmap='gray')
    else:
        plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    plt.show()

img = cv.imread('pic/preview.jpg', 0)
result = cv.imwrite('output/test.jpg',img)
print(result)

#imgShow(img)

#折线图绘制
x = np.arange(1,20)

y = 2 * x + np.random.rand(x.size) * 10
print('x = \n', x)
print('y = \n', y)
plt.plot(x,y,'*-', label = 'x-y', color = 'r')
plt.plot(y,x,'*-', label = 'y-x', color = 'g')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.grid() 
plt.xlim([0,20])
plt.ylim([0,20])
plt.show()

#柱状图绘制
a = np.random.randint(0, 101, 1000)
plt.hist(a, rwidth=0.9, color='b')
plt.show()

bins = np.arange(-0.5, 101, 1)
plt.hist(a, bins, rwidth = 0.9, color ='r')
plt.show()
