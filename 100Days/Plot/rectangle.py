'''通过对角线画矩形'''
left, top, right, bottom = 1, 2, 3, 4
color = (255,0,0)   # 颜色
thick = 2     # 线条粗细

cv2.rectangle(targetIm, (left, top), (right, bottom), color, thick)
