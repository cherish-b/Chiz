# skeleton code for obamicon
from PIL import Image
dankobama = Image.open("dankobama.jpg")
pixel_list = list(dankobama.getdata())
new_list =  []
# ===============================================================
# define colors as variables so we can recall them later:
dark_blue =  (0, 51, 76)
red =  (217, 26, 33)
light_blue =  (112, 150, 158)
yellow =  (252, 227, 166)
# ===============================================================
def obamafy(pixel_list):
	for item in pixel_list:
		intensity = item[0] + item[1] + item[2]
		if intensity < 182:
			new_list.append(dark_blue)
		elif intensity >= 182 and intensity < 364:
			new_list.append(red)
		elif intensity >= 364 and intensity < 546: 
			new_list.append(light_blue)
		else:
			new_list.append(yellow)
	return new_list

obamafy(pixel_list)
dankobama.putdata(new_list)
dankobama.show()

# #imgobj = Image.open('x.png')
# pixels = imgobj.convert('RGBA')
# data = imgobj.getdata()
# lofpixels = []
# for pixel in data:
#     lofpixels.extend(pixel)

# ===============================================================
# define a function that obama-fies the image.
# this function will take your images' pixel list as a parameter.
# for each pixel in your image's pixel list, "obama-fy" it by 
# creating a new RGB value (dark blue, red, light blue, or yellow) 
# based on the intensity of that pixel. return a pixel list 
# containing the RGB values of the obamafied picture.
# ===============================================================

# ===============================================================
# ask the user for the image name and open the image
# ===============================================================

# ===============================================================
# convert the image into a list of pixel RGB values
# ===============================================================

# ===============================================================
# obamafy your image by calling your function
# ===============================================================

# ===============================================================
# create a new image and copy the new obama-fied pixel list into the image
# ===============================================================

# ===============================================================
# finally, show and save the image
# ===============================================================