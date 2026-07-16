import numpy as np
def rescale(input_array):
   """Rescales an array from 0 to 1."""
   low = np.min(input_array)
   high = np.max(input_array)
   output_array = (input_array - low) / (high - low)
   return output_array
