from itertools import permutations

def get_permutations(s, n):
    ans = []
    for i, j in permutations(s, n):
        ans.append(i+j)
    return sorted(ans)

print (get_permutations("cat", 2) == ["ac", "at", "ca", "ct", "ta", "tc"] )