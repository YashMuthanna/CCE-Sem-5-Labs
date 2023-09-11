class generateSubsets: 
  @staticmethod
  def subsets(arr, i, subset, res):
    if i == len(arr):
      res.append(subset.copy())
      return
    subset.append(arr[i])
    generateSubsets.subsets(arr,i+1,subset,res)
    subset.pop()
    generateSubsets.subsets(arr,i+1,subset,res)
    return res
arr = list(map(int,input("Enter array: ").split()))
res = []
subset = []
index = 0
print(generateSubsets.subsets(arr,index,subset,res))