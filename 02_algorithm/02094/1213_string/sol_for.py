import sys
sys.stdin = open('input.txt', encoding='utf-8')

for _ in range(10):
    tc = int(input())
    pattern = input()
    target = input()
    count = 0

    for t_idx in range(len(target)-len(pattern)+1):
        for p_idx in range(len(pattern)):
            # 조사 범위가 pattern으로 설정되어 있기 때문에
            # 끝까지 조사가 이루어진다면 비교 대상이 같은 것
            if pattern[p_idx] != target[t_idx + p_idx]:
                break
        else:
            count += 1
    print(f'#{tc} {count}')
