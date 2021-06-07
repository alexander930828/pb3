def find_same_name(a):
    n = len(a) # 탐색 범위 설정
    result = set()
    for i in range(0, n-1): # 0부터 n-2까지 반복(맨 마지막을 제외하고 측정해야하기 때문)
        for j in range(i+1, n): # i+1부터 n-1까지 반복(앞에있는 것을 제외하고 측정해야 하기 때문)
            if a[i] == a[j]:
                result.add(a[i])
    return result

v = ['Tom', 'mike', 'sexy', 'Tom']

print(find_same_name(v))