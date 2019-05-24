""""
Program by Megan "Milk" Charity
Special crop for a larger tileset
"""

from PIL import Image
import os
import sys


def divide(img_name, mapX, mapY, border, output_dir):
	"""
	divides a tileset into seperate tiles
	"""
	try:
		#get the original image information
		img = Image.open(img_name)
		width, height = img.size

		altX = (mapX+2*border)
		altY = (mapY+2*border)

		pw = width / altX
		ph = height / altY

		index = 0

		#make the output directory
		if not os.path.exists(output_dir):
			os.mkdir(output_dir)

		#iterate through the entire image
		for i in range(int(ph)):
			for j in range(int(pw)):
				#grab the tile
				cy = i*altY 
				cx = j*altX

				#print(str(cx) + " " + str(cy))
				area = (cx, cy, cx+altX, cy+altY)
				actual_area = (border, border, border+mapX, border+mapY)
				
				#crop out the tile from the original image
				game_map = img.crop(area)
				game_map = game_map.crop(actual_area)

				#skip this image if it's completely transparent
				if is_empty(game_map):
					continue

				#save the new tile to the output directory specified
				map_name = output_dir + "/" + os.path.splitext(img_name)[0] + "_" + str(index) + ".png"
				#print(tile_name)
				game_map.save(map_name)

				index += 1
		


	except IOError:
		print("ERROR: Image not found!")
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
	MAPX = 160
	MAPY = 128
	DIR = "maps"

	BORDER = 1

	if len(sys.argv) > 2:
		MAPX = int(sys.argv[2])

	if len(sys.argv) > 3:
		MAPY = int(sys.argv[3])

	if len(sys.argv) > 4:
		DIR = sys.argv[4]





	divide(IMG_NAME, MAPX, MAPY, BORDER, DIR)

if __name__ == "__main__":
	main()