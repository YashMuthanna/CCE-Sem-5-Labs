def checkFreq(db, newItemSet):
  cnt = 0
  for row in db:
    if set(newItemSet).issubset(set(row)):
      cnt += 1
  return cnt >= min_support 

def prune(L, k, newItemSet):
  for i in range(len(newItemSet)):
    smallitemSet = newItemSet[0:i] + newItemSet[i+1:]
    if smallitemSet not in L[k-1]:
      return False
  return True


def candidate_gen(L,C,k):
  n = len(L[k-1])
  for i in range(0,n-1):
    for j in range(i+1, n):
      if L[k-1][i][0:k-1] == L[k-1][j][0:k-1]:
        newItemSet = L[k-1][i] + [L[k-1][j][k-1]]
        if prune(L, k, newItemSet):
          C[k].append(newItemSet)
          if checkFreq(db, newItemSet):
            L[k].append(newItemSet)
      else:
        break

global min_support, count, L, C, k
min_support = 2
count ={}
L = [[]]
C = [[]]
k = 0

db = [[1, 2, 5],
      [2, 4],
      [2, 3],
      [1, 2, 4],
      [1, 3],
      [2, 3],
      [1, 3],
      [1, 2, 3, 5],
      [1, 2, 3]]

for line in db:
  for elem in line:
    if elem in count:
      count[elem] += 1
    else:
      count[elem] = 1
      C[k].append([elem])

    if count[elem] >=min_support and [elem] not in L[k]:
      L[k].append([elem])

while len(L[k]) != 0:
  k = k+1
  C.append([])
  L.append([])
  candidate_gen(L,C,k)

print("\n---Frequent Itemsets: ")
for i,l in enumerate(L):
  print("L [ ", i+1, " ] : ", l)

from itertools import combinations

def generate_rules(L, min_confidence):
    rules = []
    for i in range(1, len(L)):
        for itemset in L[i]:
            for j in range(1, len(itemset)):
                for subset in combinations(itemset, j):
                    remaining = set(itemset) - set(subset)
                    confidence = count_support(itemset) / count_support(subset)
                    if confidence >= min_confidence:
                        rules.append((set(subset), remaining, confidence))
    return rules

def count_support(itemset):
    count = 0
    for row in db:
        if set(itemset).issubset(set(row)):
            count += 1
    return count

min_confidence = 0.3  # Adjust this threshold as needed

association_rules = generate_rules(L, min_confidence)

print("\n---Association Rules: ")
for rule in association_rules:
    print(f"Rule: {rule[0]} -> {rule[1]}, Confidence: {rule[2]:.2f}")
