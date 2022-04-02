import os 
import ntpath
from PIL import Image

# whatever --> PNG 
def convert_image_type(image_dir, basename):
    # basename = ntpath.basename(path_to_img)
    f_name, f_ext = os.path.splitext(basename)
    if (f_ext!='PNG' or f_ext!='JPG' or f_ext!='JPEG'):
        img = Image.open(image_dir + basename)
        img.save(image_dir + f_name + '.PNG')
    # does this delete the old file? (we don't want duplicates)






