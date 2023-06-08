import numpy as np
from PIL import Image
from ISR.models import RDN
import os

# generate the image with high resolution and store in the results folder
def generateHighResolutionImage(img_loc, choice='psnr-large'):
    origin_img = Image.open(img_loc)
    origin_img = np.array(origin_img)
    
    # create the model
    rdn = RDN(weights=choice)

    hr_img = rdn.predict(origin_img)
    store_img = Image.fromarray(hr_img)
    filename = img_loc.split('/')[-1]
    
    # check the folder for storing results, if not exist then create it  
    if not os.path.exists('results'):
        os.makedirs('results')
    store_img.save("./results/"+choice+'_'+filename)

if __name__ == '__main__' :
    DATA_FOLDER = './Data'
    for imgname in os.listdir(DATA_FOLDER):
        if imgname == '.DS_Store':
            continue
        generateHighResolutionImage( os.path.join(DATA_FOLDER, imgname), 'psnr-large')
        generateHighResolutionImage( os.path.join(DATA_FOLDER, imgname), 'psnr-small')
