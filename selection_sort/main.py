def search_lower(arr):
   """Finds the smallest value in an array"""
   lower = arr[0]
   lower_index = 0

   for i in range(1, len(arr)):
      if arr[i] < lower:
         # updates the variable if a lower value is found
         lower = arr[i]
         lower_index = i

   return lower_index


def order_by_selection(arr):
   """Sort array"""
   new_array = []

   for i in range(len(arr)):
      # removes the lower value and adds to the new array
      lower = search_lower(arr)
      new_array.append(arr.pop(lower))

   return new_array

print(order_by_selection([5, 3, 6, 2, 10])) # [2, 3, 5, 6, 10]
print(order_by_selection([-10, -20, 2, 20, 10])) # [-20, -10, 2, 10, 20]
