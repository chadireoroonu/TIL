def is_user_data_valid(user_data):
    pass
    # 여기에 코드를 작성합니다.
    if len(user_data['id']) >= 1: # id키 밸류 문자열의 길이가 있는지 확인
        if len(user_data['password']) >= 1: # password키 밸류 문자열의 길이가 있는지 확인
            return True # 두 문자열 모두 길이가 있다면 True 반환
    else: # 아니라면 False를 반환
        return False



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': '',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data1)) 
    # False 

    user_data2 = {
        'id': 'jungssafy',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data2)) 
    # True