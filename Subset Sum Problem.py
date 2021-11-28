"""Subset sum problem.
   Presented here is a Dynamic programming solution to the problem.
   Subset sum problem is an example of NP-complete problem. It has both recursive as well as dynamic programming solution.
   The dynamic programming solution has time complexity of O(n*target) as it as a nested loop with limits from 1 to n and 1 to target respectively.
   The recursive solution (brute force) has an exponential time complexity as it will require to check for all subsets in worst case."""

# Visual Explanation on how this dymanic programming algorithm works https://www.youtube.com/watch?v=s6FhG--P7z0


def subset_sum(arr, target):
    mem = {}
    for i in range(len(arr)):
        mem[(i, 0)] = 0
    for j in range(1, target + 1):
        mem[(0, j)] = 0
    for i in range(1, len(arr)):
        for j in range(1, target + 1):
            if arr[i] > j:
                mem[(i, j)] = mem[(i - 1, j)]
            else:
                mem[(i, j)] = max(mem[(i - 1, j)],
                                  mem[(i - 1, j - arr[i])] + arr[i])
    # Here it returns the closest we can get to the target
    return mem[len(arr) - 1, target]


# Setting of sequence and target sum
arr = [4, 1, 5, 3, 2, 9, 11, 23]
target = 52
# Result
result = subset_sum(arr, target)
if result == target:
    print("There is a subset that sums to ", target)
else:
    print("There isnt a subset that sums to", target,
          ", closest subset sum to the target we can get is", result)


"""
#Another solution that prints out all the possible combinations of the elements that contribute to the target sum 
def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target: 
        print ("sum(%s)=%s" % (partial, target))
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n])

subset_sum([1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 9], 23)        
"""
