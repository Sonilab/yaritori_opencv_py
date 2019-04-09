import PIL
from PIL import Image
import cv2
import sklearn
from sklearn.cluster import KMeans
import colorsys

cv2_img = cv2.imread('test.jpg')

#set analyzing size
resize_width = 150
img_height,img_width,_ = cv2_img.shape
resize_height = resize_width / img_width * img_height

cv2_img = cv2.resize(cv2_img, (int(resize_width), int(resize_height)))
cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)

#analyze main 4 color by sklearn
cv2_img.shape
cv2_img = cv2_img.reshape(
    (cv2_img.shape[0] * cv2_img.shape[1], 3))
cv2_img.shape

cluster = KMeans(n_clusters=3)
cluster.fit(X=cv2_img)
cluster.cluster_centers_

#rgb(0-255, 0-255, 0-255)
main_rgb_color = cluster.cluster_centers_

#hsv(0.0-1.0, 0.0-1.0, 0.0-1.0)
hsv_color = [[], [], []]

for i in range(3):
     hsv_color[i] = colorsys.rgb_to_hsv(main_rgb_color[i][0] / 255.0, main_rgb_color[i][1] / 255.0, main_rgb_color[i][2] / 255.0)

#hsv(0.0-1.0, 0.0-1.0, 0.0-1.0)
color_result = [0.0, 0.0, 0.0]
for c in hsv_color:
     if color_result[1] < c[1]:
          color_result = c

print(color_result)
