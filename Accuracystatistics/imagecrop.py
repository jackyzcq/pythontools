
#coding=utf-8
'''
#====================
#测试一下进程
#====================
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import re
import codecs
from PIL import Image

def image_mirror(name):
	#print(name.strip(".jpg"))
	filedest=name.strip(".jpg")+"_mirror.jpg"
	test = re.search(".jpg",name)
	#print(test)
	if not test is None :
		im = Image.open(name)
		dest_im = im.transpose(Image.FLIP_LEFT_RIGHT)
		dest_im.save(filedest)

def create_mlf(name):
	test = re.search(".txt",name)
	if not test is None :
		mlf_file=name.strip(".txt")+".mlf"
		#if not os.path.exists(mlf_file):
		cmd="python3 rec2mlf.py '{0}' > '{1}'".format(name,mlf_file)
		#print cmd
		val=os.system(cmd)
		#print val
	
def result_treate(name):
	#print name
	test = re.search(".txt",name)
	if not test is None :
		#print name
		f = codecs.open(name,'a+',encoding='utf-8')
		#content = f.readline();
		for l in open(name):
			if l.startswith("logid:"):
				continue;
			l=l.strip()
			l=l.replace('"',' ')
			l=l.replace("'",' ')
			#print(l)
			#if not l.startswith("1 "):
			l=l.replace("1 ","")
			f.truncate(0);
			result="1 {0}".format(l)
			#print result
			f.seek(0)
			f.write(result)
			f.flush()
			f.close()
			#convert(name)

def convert(file, in_enc="GBK", out_enc="UTF-8"):
    """
    该程序用于将目录下的文件从指定格式转换到指定格式，默认的是GBK转到utf-8
    :param file:    文件路径
    :param in_enc:  输入文件格式
    :param out_enc: 输出文件格式
    :return:
    """
    test = re.search(".txt",file)
    if not test is None :
        in_enc = in_enc.upper()
        out_enc = out_enc.upper()
        try:
            #print("convert [ " + file.split('\\')[-1] + " ].....From " + in_enc + " --> " + out_enc )
            f = codecs.open(file, 'r', in_enc)
            #print file
            #print f.encoding
            new_content = f.read()
            codecs.open(file, 'w', out_enc).write(new_content)
    # print (f.read())
        except IOError as err:
            print("I/O error: {0}".format(err))

def image_crop(name):
	# The crop method from the Image module takes four coordinates as input.
	# The right can also be represented as (left+width)
	# and lower can be represented as (upper+height).
	#(left, upper, right, lower) = (66, 66, 3200, 645)
	#U36 8M
	box0=(66, 64, 3200, 702)
	box1=(66, 702, 3200, 1175)
	box2=(66, 1175, 3200, 1520)
	box3=(66, 1520, 3200, 1790)
	box4=(66, 1790, 3200, 2037)
	box5=(66, 2039, 3200, 2300)
	# U36 5M 区域
	#box0=(0, 0, 2560, 475)
	#box1=(0, 475, 2560, 875)
	#box2=(0, 875, 2560, 1165)
	#box3=(0, 1165, 2560, 1390)
	#box4=(0, 1390, 2560, 1590)
	#box5=(0, 1590, 2560, 1800)
	test = re.search(".jpg",name)
	print(test)
	if not test is None :
		im = Image.open(name).transpose(Image.FLIP_LEFT_RIGHT)
	# Here the image "im" is cropped and assigned to new variable im_crop
		im0_crop = im.crop(box0)
		im1_crop = im.crop(box1)
		im2_crop = im.crop(box2)
		im3_crop = im.crop(box3)
		im4_crop = im.crop(box4)
		im5_crop = im.crop(box5)
		im0_crop.save(name.strip(".jpg")+"_0.jpg")
		im1_crop.save(name.strip(".jpg")+"_1.jpg")
		im2_crop.save(name.strip(".jpg")+"_2.jpg")
		im3_crop.save(name.strip(".jpg")+"_3.jpg")
		im4_crop.save(name.strip(".jpg")+"_4.jpg")
		im5_crop.save(name.strip(".jpg")+"_5.jpg")

project_dir = os.path.dirname(os.path.abspath(__file__))

def get_filelist(dir):
 
    Filelist = []
 
    for home, dirs, files in os.walk(project_dir):
 
        for filename in files:

             Filelist.append(os.path.join(home, filename))
 
    return Filelist
 
def test_result(name,detail,language='Chinese'):
	test = re.search(".txt",name)
	if not test is None :
		#print name
		#test = re.search("英文",name)
		test = re.search("eng",language.lower())
		if not test is None:
			test= re.search("雅黑",name)
			if not test is None:
				#print name
				mlf_file=name.strip(".txt")+".mlf"
				cmd='./HResults -t -I "{0}"  /dev/null "{1}"'.format("eng_yahei.mlf",mlf_file)		
			else :
				#print name
				mlf_file=name.strip(".txt")+".mlf"
				cmd='./HResults -t -I "{0}"  /dev/null "{1}"'.format("english.mlf",mlf_file)
		else:
			test= re.search("雅黑",name)
			if not test is None:
				#print name
				mlf_file=name.strip(".txt")+".mlf"
				cmd='./HResults -t -I "{0}"  /dev/null "{1}"'.format("cn_yahei.mlf",mlf_file)		
			else :
				#print name
				mlf_file=name.strip(".txt")+".mlf"
				cmd='./HResults -t -I "{0}"  /dev/null "{1}"'.format("chinese.mlf",mlf_file)
		if detail:
			val = os.system(cmd)
			if val != 0:
				print name
			return
		#print cmd
		#print("**************")
		#print(name)
		#print("**************")
		val = os.popen(cmd)
		for temp in val.readlines():
			#test=re.search("Rec :",temp)
			#if not test is None :
			#	print temp
			if detail :
				print temp
			else:
				test=re.search("WORD:",temp)
				if not test is None :
					result=re.split(" ",temp.strip("\n"))
					Corr = result[1].strip("%Corr=").strip(",")
					if Corr=="-nan":
						Corr="0"
					acc = result[2].strip("Acc=")
					if acc=="-nan":
						acc="0"
					H = result[3].strip("[H=").strip(",")
					D = result[4].strip("D=").strip(",")
					S = result[5].strip("S=").strip(",")
					I = result[6].strip("I=").strip(",")
					N = result[7].strip("N=").strip("]")
					filename=name.split("/")
					print filename[len(filename)-1].strip(".txt")+","+Corr+","+acc+","+H+","+D+","+S+","+I+","+N
					
if __name__ =="__main__":
 
    Filelist = get_filelist(dir)
    
    #print(len( Filelist))
    for file in Filelist :
		#print(file.split("/"))
		#print(file)
		#convert(file)
		result_treate(file)
		create_mlf(file)
		if len(sys.argv)>=2:
			language = sys.argv[1]
			test_result(file,True,language)
		else:
			test_result(file,True)
