# Two arrays are given arr1 and arr2. (Interview qu. sankeySolutions)
# Find out which element of arr1 are not present in arr2
#  i/p      arr1:{1,2,3,4,5}
#         arr2:{0,3,2,4}
#  o/p      {0,5}


arr1 = {1,2,3,4,5}
arr2 = {0,3,2,4}

result = arr1.difference(arr2)

print(result)
