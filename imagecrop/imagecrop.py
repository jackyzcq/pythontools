
#coding=utf-8
'''
#====================
#测试一下进程
#====================
'''
import os
import re
from PIL import Image

def image_mirror(name):
	print(name.strip(".jpg"))
	filedest=name.strip(".jpg")+"_mirror.jpg"
	test = re.search(".jpg",name)
	print(test)
	if not test is None :
		im = Image.open(name)
		dest_im = im.transpose(Image.FLIP_LEFT_RIGHT)
		dest_im.save(filedest)

def image_single_crop(name,image,left,top,right,bottom,index):
	box=(left,top,right,bottom)
	im_crop=image.crop(box)
	im_crop.save("{0}_{1}.jpg".format(name.strip(".jpg"),index),quality=95)

def image_multi_crop(name,image,left,top,right,bottom,index):
	box=(left,top,right,bottom)
	step = (right-left)/(3*50)
	lright=right
	for position in range(left,left+step*50,step):
	#for top in range(top_min,top_max,1):
	#	for right in range(right_max,right_min,-1):
	#		for down in range(down_max,down_min,-1):
		lright=lright-step
		savename="{0}_{1}_{2}_{3}_{4}_{5}.jpg".format(name.strip(".jpg"),position,top,lright,bottom,index)
		im_crop=image.crop((position,top,lright,bottom))
		im_crop.save(savename,quality=95)	

	
def image_crop(name,type):
	#print name
	# The crop method from the Image module takes four coordinates as input.
	# The right can also be represented as (left+width)
	# and lower can be represented as (upper+height).
	#(left, upper, right, lower) = (66, 66, 3200, 645)
	#U36 中文8M 焦距30厘米
	if type == 1:
		box=((66, 64, 3200, 702),
		(66, 702, 3200, 1175),
		(66, 1175, 3200, 1520),
		(66, 1520, 3200, 1790),
		(66, 1790, 3200, 2037),
		(66, 2039, 3200, 2300))
	elif type == 11:
	#U36 英文8M 焦距30厘米
		box=((66, 64, 3200, 700),
		(66, 700, 3200, 1175),
		(66, 1175, 3200, 1534),
		(66, 1534, 3200, 1819),
		(66, 1819, 3200, 2070),
		(66, 2070, 3200, 2299))
	elif type == 111:
	#U36 中文8M 焦距27厘米
		box=((109, 135, 3188, 788),
		(109, 788, 3188, 1275),
		(109, 1275, 3188, 1639),
		(109, 1639, 3188, 1931),
		(109, 1931, 3188, 2202),
		(109, 2202, 3188, 2420))
	elif type == 112:
	#U36 英文8M 焦距27厘米
		box=((159, 152, 3200, 785),
		(159, 785, 3200, 1258),
		(159, 1258, 3200, 1635),
		(159, 1635, 3200, 1964),
		(159, 1964, 3200, 2205),
		(159, 2205, 3200, 2460)	)		
	elif type == 113:
	#U36 英文8M 焦距23.5厘米
		box=((159, 152, 3200, 785),
		(159, 785, 3200, 1258),
		(159, 1258, 3200, 1600),
		(159, 1600, 3200, 1871),
		(159, 1871, 3200, 2106),
		(159, 2106, 3200, 2365)	)
	elif type == 114:
	#U36 中文8M 焦距23.5厘米
		box=((159, 152, 3200, 785),
		(159, 785, 3200, 1258),
		(159, 1258, 3200, 1600),
		(159, 1600, 3200, 1871),
		(159, 1871, 3200, 2106),
		(159, 2106, 3200, 2365)	)
	elif type == 115:
	#U36 中文8M 焦距25厘米
		box=((159, 152, 3200, 725),
		(159, 725, 3200, 1200),
		(159, 1200, 3200, 1533),
		(159, 1533, 3200, 1806),
		(159, 1806, 3200, 2050),
		(159, 2050, 3200, 2285)	)
	elif type == 116:
	#U36 英文8M 焦距25厘米
		box=((159, 100, 3200, 725),
		(159, 725, 3200, 1200),
		(159, 1200, 3200, 1533),
		(159, 1533, 3200, 1806),
		(159, 1806, 3200, 2080),
		(159, 2050, 3200, 2285)	)		
	elif type == 117:
	#U36 中文8M 焦距27厘米
		box=((66, 129, 3137, 768),
		(66, 742, 3137, 1258),
		(66, 1200, 3137, 1593),
		(66, 1586, 3137, 1878),
		(66, 1878, 3137, 2133),
		(66, 2133, 3137, 2375)	)	
	elif type == 118:
	#U36 英文8M 焦距27厘米
		box=((66, 129, 3137, 742),
		(66, 742, 3137, 1200),
		(66, 1200, 3137, 1586),
		(66, 1586, 3137, 1878),
		(66, 1878, 3137, 2133),
		(66, 2133, 3137, 2375)	)			
	elif type == 2:
	# U36 5M 中文 区域
		box=((0, 0, 2560, 475),
		(0, 475, 2560, 875),
		(0, 875, 2560, 1165),
		(0, 1165, 2560, 1390),
		(0, 1390, 2560, 1590),
		(0, 1590, 2560, 1800))
	elif type == 21:
	# U36 5M 英文 区域
		box=((0, 0, 2560, 475),
		(0, 475, 2560, 875),
		(0, 875, 2560, 1174),
		(0, 1174, 2560, 1426),
		(0, 1426, 2560, 1628),
		(0, 1628, 2560, 1814))
	elif type == 22:
	# U36 5M 中文 hei 区域
		box=((0, 0, 2560, 475),
		(0, 490, 2560, 875),
		(0, 890, 2560, 1165),
		(0, 1175, 2560, 1400),
		(0, 1410, 2560, 1600),
		(0, 1600, 2560, 1810))	
	elif type == 23:
	# U36 5M 英文 hei 区域
		box=((0, 0, 2560, 475),
		(0, 490, 2560, 875),
		(0, 890, 2560, 1165),
		(0, 1175, 2560, 1400),
		(0, 1410, 2560, 1600),
		(0, 1620, 2560, 1810))	
	elif type == 25:
	#U36 英文8M 黑 焦距25厘米
		box=((140, 39, 3200, 700),
		(159, 725, 3200, 1190),
		(159, 1200, 3200, 1533),
		(159, 1540, 3200, 1806),
		(159, 1820, 3200, 2050),
		(159, 2070, 3200, 2300)	)		
	elif type == 26:
	#U36 中文8M 黑 焦距25厘米
		box=((140, 39, 3200, 700),
		(159, 725, 3200, 1190),
		(159, 1200, 3200, 1533),
		(159, 1550, 3200, 1820),
		(159, 1830, 3200, 2060),
		(159, 2090, 3200, 2320)	)			
	elif type == 3:
	# C12Pro 中文 区域
		box=((66, 64, 3200, 688),
		(66, 688, 3200, 1068),
		(66, 1068, 3200, 1346),
		(66, 1346, 3200, 1572),
		(66, 1572, 3200, 1768),
		(66, 1768, 3200, 1964))
	elif type == 31:
	# C12Pro 英文 区域
		box=((66, 64, 3200, 688),
		(66, 688, 3200, 1068),
		(66, 1068, 3200, 1374),
		(66, 1374, 3200, 1600),
		(66, 1600, 3200, 1792),
		(66, 1792, 3200, 1964))
	elif type == 4:
	# Umix6 5M 中文 区域
		box=((134, 512, 1840, 910),
		(134, 910, 1840, 1210),
		(134, 1210, 1840, 1466),
		(134, 1466, 1840, 1680),
		(134, 1680, 1840, 1866),
		(134, 1866, 1840, 2096))
	elif type == 41:
	# Umix6 5M 英文 区域
		box=((134, 522, 1840, 916),
		(134, 916, 1840, 1206),
		(134, 1206, 1840, 1466),
		(134, 1466, 1840, 1690),
		(134, 1690, 1840, 1890),
		(134, 1890, 1840, 2098)	)	
	elif type == 5:
	# Umix6 8M 区域
		box=((82, 786, 2200, 1228),
		(82, 1228, 2200, 1580),
		(82, 1580, 2200, 1888),
		(82, 1888, 2200, 2150),
		(82, 2150, 2200, 2400),
		(82, 2400, 2200, 2628)	)
	elif type == 6:
	# S5 8M 区域
		box=((272, 632, 2134, 1044),
		(272, 1044, 2134, 1370),
		(272, 1370, 2134, 1632),
		(272, 1632, 2134, 1856),
		(272, 1856, 2134, 2060),
		(272, 2060, 2134, 2244)	)
	elif type == 71:
	# 378 8M 中文 区域
		box=((94, 669, 2379, 1150),
		(94, 1150, 2379, 1544),
		(94, 1544, 2379, 1845),
		(94, 1845, 2379, 2079),
		(94, 2079, 2379, 2284),
		(94, 2284, 2379, 2506)	)		
	elif type == 72:
	# 378 8M 英文 区域
		box=((94, 669, 2379, 1150),
		(94, 1150, 2379, 1544),
		(94, 1544, 2379, 1845),
		(94, 1845, 2379, 2079),
		(94, 2079, 2379, 2307),
		(94, 2300, 2379, 2506)	)
	elif type == 81:
	# 711 8M 中文 区域
		box=((87, 711, 2335, 1203),
		(87, 1203, 2335, 1586),
		(87, 1586, 2335, 1881),
		(87, 1881, 2335, 2120),
		(87, 2120, 2335, 2310),
		(87, 2310, 2335, 2542)	)		
	elif type == 82:
	# 711 8M 英文 区域
		box=((87, 711, 2335, 1203),
		(87, 1203, 2335, 1586),
		(87, 1586, 2335, 1881),
		(87, 1881, 2335, 2120),
		(87, 2120, 2335, 2348),
		(87, 2348, 2335, 2542)	)	
	elif type == 83:
	# 711 8M 英文 宋体 小四 区域
		box=((87, 711, 2335, 1203),
		(87, 1203, 2335, 1586),
		(87, 1586, 2335, 1881),
		(87, 1881, 2335, 2120),
		(87, 2120, 2335, 2318),
		(87, 2318, 2335, 2542)	)		
	test = re.search(".jpg",name)
	print(test)
	if not test is None :
		if type == 6:
			im = Image.open(name).transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_270)
		else:
			im = Image.open(name).transpose(Image.FLIP_LEFT_RIGHT)
	# Here the image "im" is cropped and assigned to new variable im_crop
		index = 0
		for b in box:
			index=index+1
			image_single_crop(name,im,b[0],b[1],b[2],b[3],index)
			if index in (4,5,6):
				image_multi_crop(name,im,b[0],b[1],b[2],b[3],index)
		#im0_crop = im.crop(box0)
		#im1_crop = im.crop(box1)
		#im2_crop = im.crop(box2)
		#im3_crop = im.crop(box3)
		#im4_crop = im.crop(box4)
		#im5_crop = im.crop(box5)
		#im0_crop.save(name.strip(".jpg")+"_0.jpg",quality=95)
		#im1_crop.save(name.strip(".jpg")+"_1.jpg",quality=95)
		#im2_crop.save(name.strip(".jpg")+"_2.jpg",quality=95)
		#im3_crop.save(name.strip(".jpg")+"_3.jpg",quality=95)
		#im4_crop.save(name.strip(".jpg")+"_4.jpg",quality=95)
		#im5_crop.save(name.strip(".jpg")+"_5.jpg",quality=95)

project_dir = os.path.dirname(os.path.abspath(__file__))
def get_filelist(dir):
 
    Filelist = []
 
    for home, dirs, files in os.walk(project_dir):
 
        for filename in files:

             Filelist.append(os.path.join(home, filename))
 
    return Filelist
 
if __name__ =="__main__":
 
    Filelist = get_filelist(dir)
 
    print(len( Filelist))
 
    for file in Filelist :
		print file
		# 1 U36 中文8M
		# 11 U36 英文8M
		# 111 U36 中文8M 焦距27厘米
		# 112 U36 英文 焦距27厘米
		# 113 U36 中文8M 焦距23.5厘米
		# 114 U36 英文 焦距23.5厘米
		# 115 U36 中文8M 焦距25厘米
		# 116 U36 英文 焦距25厘米
		# 117 U36 中文8M 焦距27厘米
		# 118 U36 英文 焦距27厘米
		# 2 U36 5M 区域
		# 21 U36 5M 英文 区域
		# 3 C12Pro 中文 区域
		# 31 C12Pro 英文 区域
		# 4 Umix6 5M 中文 区域
		# 41 Umix6 5M 英文 区域
		# 5 Umix6 8M 区域
		# 6 S5 8M 区域
		# 378 8M 中文 区域
		# 378 8M 英文 区域
		# 711 8M 中文 区域
		# 711 8M 英文 区域
		image_crop(file,81)
