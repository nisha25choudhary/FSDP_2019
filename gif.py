# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 18:03:31 2019

@author: Lenovo
"""
 

from PIL import Image

im1 = Image.open('png\\download.png')
im2 = Image.open('png\\download (1).png')
im1.save("png\\out.gif", save_all=True, append_images=[im2], duration=1, loop=0)
 



import os,sys
import datetime
import imageio
import time
e=sys.exit
def create_gif(filenames, duration):
	images = []
	for filename in filenames:
		images.append(imageio.imread(filename))
	output_file = 'Gif-%s.gif' % datetime.datetime.now().strftime('%Y-%d-%H-%M')
	imageio.mimsave(output_file, images, duration=duration)
 
if __name__ == "__main__":
    duration = 0.2 
    filenames = sorted(filter(os.path.isfile, [x for x in os.listdir() if x.endswith(('.jpg','.png'))]), key=lambda p: os.path.exists(p) and os.stat(p).st_mtime or time.mktime(datetime.now().timetuple()))
 
create_gif(filenames, duration)



import imageio
import os

filenames = []

for file in os.listdir('E:\\FSDP2019\\Day10'):
    filename = os.fsdecode(file)
    if filename.endswith( ('.jpg', '.png') ):
        filenames.append(filename)

filenames.sort() # this iteration technique has no built in order, so sort the frames

images = list(map(lambda filename: imageio.imread(filename), filenames))

imageio.mimsave(os.path.join('movie.gif'), images, duration = 1) # modify duration as needed