import numpy as np
# Write your mean_datasets function here
def mean_datasets(files):
  all_data = []
  for k, file in enumerate(files):
    if k == 0:
      all_data = np.array(np.loadtxt(file, delimiter=','))
    else:
      data = np.array(np.loadtxt(file, delimiter=','))
      all_data = all_data + data
      
  all_data = all_data / len(files)
  
  return np.round(all_data, 1)

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example from the question:
  print(mean_datasets(['data/data1.csv', 'data/data2.csv', 'data/data3.csv']))

  # Run your function with the second example from the question:
  print(mean_datasets(['data/data4.csv', 'data/data5.csv', 'data/data6.csv']))