from astropy.io import fits
import numpy as np
# Write your mean_fits function here:
def mean_fits(files):
  all_data = []
  for k, file in enumerate(files):
    if k == 0:
      all_data = fits.getdata(file)
    else:
      data = fits.getdata(file)
      all_data = all_data + data
      
  all_data = all_data / len(files)
  
  return all_data

if __name__ == '__main__':
  
  # Test your function with examples from the question
  data  = mean_fits(['image0.fits', 'image1.fits', 'image2.fits'])
  print(data[100, 100])

  # You can also plot the result:
  import matplotlib.pyplot as plt
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()