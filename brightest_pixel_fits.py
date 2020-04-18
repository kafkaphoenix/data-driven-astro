from astropy.io import fits
import numpy as np
# Write your load_fits function here.

def load_fits(filename):
  data = fits.getdata(filename)
  ind = np.unravel_index(np.argmax(data, axis=None), data.shape)
  return(ind)

if __name__ == '__main__':
  # Run your `load_fits` function with examples:
  bright = load_fits('data/502nmos.fits')
  print(bright)

  # You can also confirm your result visually:
  from astropy.io import fits
  import matplotlib.pyplot as plt

  with fits.open('502nmos.fits') as hdulist:
    data = hdulist[0].data

  # Plot the 2D image data
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.savefig('plot.png')
  plt.show()
  hdulist.close()

 
