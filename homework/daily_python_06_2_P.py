grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]

max = 0 # 최댓값은 0에서 부터 시작
max_list = [] # 최댓값에 해당하는 작물을 담아줄 빈 리스트 생성
for i in range(len(grain_lst)): # i가 곡물 리스트의 길이 동안 순회
    if grain_lst[i][1] > max: # 만약 곡물가격이 최댓값보다 크다면
        max = grain_lst[i][1] # 최댓값 갱신!
        max_list.append(grain_lst[i][0]) # 맥스 리스트에 해당 작물명 추가

# 마지막에 추가된 작물이 최댓값일 것이므로 리스트 마지막 요소 반환
print(max_list[-1])
