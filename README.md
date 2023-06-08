# prerequisite( https://github.com/idealo/image-super-resolution)
1. conda create --name  python3.7 python=3.7
2. conda activate python3.7
3. pip install ISR
4. pip install 'h5py==2.10.0' --force-reinstall
5. pip install Pillow


# Function Introduction
1. img_loc: the location of the input image
2. choice: which model want to load, two choices:['psnr-large', 'psnr-small']
3. the generated image will be stored in the folder 'results'