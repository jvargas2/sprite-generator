""""
Program by Megan "Milk" Charity
Crops and saves individual tiles from a tileset
"""

from PIL import Image
import os
import sys


#divides a tileset into seperate tiles
def extract(img_name, tsize, output_dir):

	try:
		#get the original image information
		img = Image.open(img_name)
		width, height = img.size

		pw = width / tsize
		ph = height / tsize

		index = 0

		#make the output directory
		if not os.path.exists(output_dir):
			os.mkdir(output_dir)

		#iterate through the entire image
		for i in range(int(ph)):
			for j in range(int(pw)):
				#grab the tile
				cy = i*tsize
				cx = j*tsize
				area = (cx, cy, cx+tsize, cy+tsize)
				
				#crop out the tile from the original image
				tile = img.crop(area)

				#skip this image if it's completely transparent
				if is_empty(tile):
					continue

				tile_name = output_dir + "/" + os.path.splitext(img_name)[0] + "_" + str(index) + ".png"
				#print(tile_name)
				tile.save(tile_name)

				index += 1
				

	except IOError:
		pass

#checks if an image is completely transparent
def is_empty(img):
	#print(img.getcolors())
	return img.getcolors()[0][1][3] == 0

def main():
	#grab the parameters
	IMG_NAME = sys.argv[1]
	TILE_SIZE = 16
	DIR = "tiles"

	if len(sys.argv) > 2:
		TILE_SIZE = int(sys.argv[2])

	if len(sys.argv) > 3:
		DIR = sys.argv[3]

	extract(IMG_NAME, TILE_SIZE, DIR)

if __name__ == "__main__":
	main()