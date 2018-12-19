# -*- coding: utf-8 -*-
"""
@author: Yi_Zhou
"""
import os
import time
import numpy
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from PIL import Image

need_update = True

def get_screen_image():
	os.system("adb shell screencap -p /sdcard/screen.png")
	os.system("adb pull /sdcard/screen.png")
	return numpy.array(Image.open("screen.png"))

def jump_to_next(point1, point2):
	x1, y1 = point1; x2, y2 = point2
	distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
	os.system("adb shell input swipe 320 410 320 410 {}".format(int(distance*1.35)))


def on_calck(event, coor=[]):
	global need_update
	coor.append((event.xdata, event.ydata))
	if len(coor) == 2:
		jump_to_next(coor.pop(), coor.pop())
	need_update = True

def update_screen(frame):
	global need_update
	if need_update:
		time.sleep(2)
		axes_image.set_array(get_screen_image())
		need_update = False
	return axes_image,

print("enjoy your game！")
print("Please click the image coordinate origin and target position successively！")
print("Exit by closing the image window！")
figure = plt.figure()
axes_image = plt.imshow(get_screen_image(), animated=True)
figure.canvas.mpl_connect("button_press_event", on_calck)
ai = FuncAnimation(figure, update_screen, interval=50, blit=True)
plt.show()

