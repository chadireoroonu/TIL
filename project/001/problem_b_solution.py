import json
from pprint import pprint


def movie_info(movie, genres):
    pass 

    # genre 정보 아이디를 키, 이름을 밸류로 하는 딕셔너리 만들기
    genres_dict = {}
    for genre in genres:
        # 'dict[key] = value' 넣을 시 딕셔너리에 추가 가능
        genres_dict[genre['id']] = genre['name']

    print(movie['genre_idx'])
    genre_name_list = []
    for idx in movie['genre_idx']:
        print(idx)
        print(genres_dict[idx])
        print()
        genre_name_list += [genres_dict[idx]]
        genre_name_list.append(genres_dict[idx]) # 둘 중 한 방법 사용
    print(genre_name_list)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))

# for i in range(len(genres_list)):
#     print(genres_list[i]['id'])