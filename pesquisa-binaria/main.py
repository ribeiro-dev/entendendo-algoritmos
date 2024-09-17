def binary_search(array, item, tries=False):
   low = 0
   high = len(array) - 1
   counter = 1

   while low <= high:
      middle = (low + high) // 2
      guess = array[middle]

      # Number found
      if guess == item:
         if tries: print('Tries:', counter)
         return middle

      # Number not found
      if guess > item:
         high = middle - 1

      else:
         low = middle + 1

      counter += 1

   return None


# -----
my_array = [-945, -848, -794, -562, -545, -508, -429, -388, -345, -149, 82, 193, 265, 314, 424, 575, 760, 945, 946]
print(binary_search(my_array, 575)) # -- 15
print(binary_search(my_array, -149, True)) # -- 9
