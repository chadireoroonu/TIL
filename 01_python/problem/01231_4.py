def is_id_valid(user_data):
    pass
    # 여기에 코드를 작성합니다.
    last_data = user_data['id'][-1] # password 값의 마지막 글자를 추출
    i = 0
    while i <= 9: # i가 9보다 작거나 같은 동안
        if str(i) == last_data: # 문자열 i와 마지막 글자를 비교
            return True # 한번이라도 같은 값이 나오면 True 반환
        else: # 그렇지 않으면 i를 1 증가시켜 반복
            i += 1
    return False # 같은 값이 없다면 False 반환



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': 'jungssafy5',
        'password': '1q2w3e4',
    }
    print(is_id_valid(user_data1)) 
    # True
    
    user_data2 = {
        'id': 'kimssafy!',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data2)) 
    # False