 #!/usr/local/bin/python
 # -*- coding: utf-8 -*-
from Tkinter import *
from tkFileDialog import askopenfilename
from PIL import Image
from psd_tools import PSDImage
import sys
import os


def loopLayer( layers ):

	for layer in layers.layers: 
		if layer.visible == False:
			continue
		if type(layer).__name__ == 'Group':
			#print 'Group'
			loopLayer(layer)
		else:
			#print 'layer'
			savePng(layer)
	return;
def savePng( layer ):
	# print 'layer :', layer.name
	# print 'BBox :', layer.bbox
	# imageAndroid =  './pngs/android/png_'+str(layer.bbox.x1)+'_'+str(layer.bbox.y1)+'_'+str(layer.bbox.width)+'_'+str(layer.bbox.height)+'.png'
	imageiOS =  './pngs/ios/png_'+str(layer.bbox.x1)+'_'+str(layer.bbox.y1)+'_'+str(layer.bbox.width)+'_'+str(layer.bbox.height)+'.png'
	print imageiOS
	layer_image = layer.as_PIL()
	layer_image.save(imageiOS)

	# layer.as_PIL().resize((int(layer.bbox.width*1.5), int(layer.bbox.height*1.5)), Image.ANTIALIAS).save(imageAndroid)
	return;

root = Tk()
print "脚本名：", sys.argv[0]
if os.path.exists('pngs') == False:
	os.mkdir('pngs')
if os.path.exists('pngs/android') == False:
	os.mkdir('pngs/android')
if os.path.exists('pngs/ios') == False:
	os.mkdir('pngs/ios')

file = askopenfilename(parent=root, initialdir="C:/",title='Choose an image.')
psd = PSDImage.load(file)
loopLayer(psd)
psd.as_PIL().save('./pngs/main.png')
# for group in psd.layers:        # 第二个实例
# 	print 'group :', group.name  
# 	for layer in group.layers: 
		



