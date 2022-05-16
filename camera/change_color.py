from PIL import Image
import matplotlib.pylab as plt

r = Image.open("./images/test_trimed.jpg")
#plt.imshow(r)
#plt.show()


# 픽셀들 색깔 값 출력
"""
for i in range(0,r.size[0]): # x방향 탐색
    for j in range(0,r.size[1]): # y방향 탐색
        rgb = r.getpixel((i,j))  # i,j 위치에서의 RGB 취득
        print(rgb)
"""

# 기준값
threshold = 127

for i in range(0, r.size[0]):
    for j in range(0, r.size[1]):
        rgb = r.getpixel((i, j))
        rgb_a = round((rgb[0] + rgb[1] + rgb[2])/3)
        if rgb_a <= threshold:
            r.putpixel((i, j), (0, 0, 0))
        else:
            r.putpixel((i, j), (255, 255, 255))


#plt.imshow(r)
#plt.show()

r.save("./images/test_colorChanged.jpg")
        

        
        