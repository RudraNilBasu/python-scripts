# Save sreenshots from a video as image 
# Good if you need random images as dataset in your projects 

import matplotlib.pyplot as plt 
import imageio

imageio.plugins.ffmpeg.download() # download ffmpeg plugin if not already present
filename = '/home/arka/Downloads/The.Man.Who.Knew.Infinity.2015.720p.BRRip.x264.AAC-ETRG/tmwki.mp4' # path to video
vid = imageio.get_reader(filename,  'ffmpeg')

len = vid.get_length()
print len

for i in range(0, len):
	if(i%10000 == 0):
		image = vid.get_data(i)
		fig = plt.figure()
		fig.suptitle('image #{}'.format(i), fontsize=10)
		plt.axis('off')
		plt.imshow(image)
		plt.savefig('img_' +str(i)+'.png')
	else:
		continue;
# pylab.show()
