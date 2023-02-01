score = {
    'python': 80,
    'django': 89,
    'web': 83
}
# 알고리즘 성적을 추가하고 파이썬 점수를 수정
score.update({'algorithm': 90, 'python': 85})

add = sum(score.values()) # 딕셔너리의 값을 모아서 평균을 구함


print(add/len(score)) # 딕셔너리 값의 합을 딕셔너리 개수로 나눔