import os


def get_tif_files():
    
    """
    Returns a list of the tif filenames inside the zip files inside the folder /data/raw.
    The filenames are in the format the can be read wihout decompressing the file, directly from the zip.
    """
    
    dir_path = '../../../data/raw/'
    zip_files = []
    tif_files = []
    rasterio_files = []

    # append all zip files in the target directory
    for path in os.listdir(dir_path):
        # Check if it's a file
        if os.path.isfile(os.path.join(dir_path, path)):
            # Check if is a zip file (extension)
            if path[-4:] == '.zip':
                zip_files.append(path)

    for zip_file in zip_files:      
        tif_filename = zip_file.replace('-geotiff.zip', '.tif')
        tif_files.append(tif_filename)
        rasterio_files.append('zip+file:' + dir_path + zip_file + '!' + tif_filename)
             
    return rasterio_files
