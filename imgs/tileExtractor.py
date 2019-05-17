""""
Program by Megan "Milk" Charity
Crops and saves individual tiles from a tileset
"""

from PIL import Image
import os
import sys


def extract(img_name, tsize, output_dir):
	"""
	divides a tileset into seperate tiles
	"""
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

				#save the new tile to the output directory specified
				tile_name = output_dir + "/" + os.path.splitext(img_name)[0] + "_" + str(index) + ".png"
				#print(tile_name)
				tile.save(tile_name)

				index += 1
				

	except IOError:
		pass

def is_empty(img):
	"""
	checks if an image is completely transparent
	"""

	#print(img.getcolors())
	return img.getcolors()[0][1][3] == 0

def main():
	#grab the parameters
	if len(sys.argv) < 2:
		sys.exit("Invalid number of arguments!\n\t`python3 tileExtractor IMAGE_PATH (TILE_SIZE) (OUTPUT_DIRECTORY)`")

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