# depth = 현재 조사 한 대상의 수
# r = 최대 조사하려는 대상의 수
def perm(depth, r):
    if depth == r:
        print(check)
    else:    # check에 r개 만큼의 대상이 채워지기 전
        for i in range(len(nums)):    # nums가 가진 모든 대상 조사
            if not visited[i]:    # nums의 i 번째를 아직 사용 전이면
                visited[i] = True
                check[depth] = nums[i]
                perm(depth + 1, r)
                visited[i] = False

nums = [1, 2, 3]
# 각 요소의 사용여부
visited = [0] * len(nums)
# 실질적으로 사용한 대상 값
check = [0] * 2

perm(0, 2)

def perm(depth, r):
    if depth == r:
        print(check)
    else:   # check에 아직 r개 만큼의 대상이 채워지지 않았음
        # nums가 가진 모든 대상을 조사
        for i in range(len(nums)):
            check[depth] = nums[i] # check[0] = nums[0]
            perm(depth + 1, r)

    nums = [1, 2, 3]
    # 각 요소의 사용여부
    visited = [0] * len(nums)
    # 실질적으로 사용한 대상값
    check = [0] * 2

    print(visited, check)
    perm(0, 2)
