import sys
sys.stdin = open('input.txt', encoding='utf-8')

for t in range(10):
    tc = int(input())
    pattern = input()
    target = input()

    # 조사하려고 하는 두 대상의 조사 대상을
    # 내가 직접 컨트롤 하기 위해 인덱스 설정
    p_idx = 0
    t_idx = 0

    count = 0

    while t_idx < len(target):
        # # 두 값이 같으면 인덱스 증가
        # if target[t_idx] == pattern[p_idx]:
        #     p_idx += 1
        #     t_idx += 1
        # # 모든 패턴에 대해 조사했다면

        if target[t_idx] != pattern[p_idx]:
            t_idx = t_idx - p_idx
            p_idx = -1 # 왜 -1이냐면
        # 모든 상황에 대해서 항상 증가할 것이기 때문에
        p_idx += 1
        t_idx += 1

        if p_idx == len(pattern):
            count += 1
            p_idx = 0  # 다음 위치부터는 처음부터 다시 조사

    print(f'#{tc} {count}')