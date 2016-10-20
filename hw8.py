## Dan Smilowitz 
## DATA 602 hw8


## On each image you will count the number of objects in the image and find their center points.
## Perform the following tasks: thresholding; count objects; find center points

import scipy.misc as misc
import scipy.ndimage as ndimage
import pymorph
from os.path import basename

# function to count & locate objects
def get_objects(flnm, sigma):
	raw_img = misc.imread(flnm)
	img = ndimage.gaussian_filter(raw_img, sigma)
	thres = img > img.mean()
	#find objects
	distance = ndimage.distance_transform_edt(thres)
	found, n_found = ndimage.label(distance)
	com = ndimage.measurements.center_of_mass(distance, found, xrange(1, n_found+1))
	coords = com_text(com, n_found)
	return '%d objects were found in %s.\nTheir centers of mass are located at \n  %s' %(n_found, basename(flnm), coords)

# ndimage.distance_transform_edt is not working for circles -- using pymorph.regmax instead
# this solution did not work for the other images
def pymorph_objects(flnm, sigma):
	raw_img = misc.imread('data/circles.png')
	img = ndimage.gaussian_filter(raw_img, sigma)
	thres = img > img.mean()
	#find objects
	peaks = pymorph.regmax(img)
	found, n_found = ndimage.label(peaks)
	com = ndimage.measurements.center_of_mass(peaks, found, xrange(1, n_found+1))
	coords = com_text(com, n_found)
	return '%d objects were found in %s.\nTheir centers of mass are located at \n  %s' %(n_found, basename(flnm), coords)


# convert list of touples to printable form
def com_text(com, n, dec=3):
    txt = []
    for i in range(n):
        coord = '(' + str(round(com[i][0], dec)) + ', ' + str(round(com[i][1], dec)) + ')'
        txt.append(coord)
    ret_text = '\n  '.join(txt)
    return ret_text


# execute for given files
if __name__ == "__main__":
	images = ['data/circles.png', 'data/objects.png', 'data/peppers.png']
	sigmas = [15, 2, 2]
	print(pymorph_objects(images[0], sigmas[0]))
	for i in range(1, len(images)):
		print(get_objects(images[i], sigmas[i]))
