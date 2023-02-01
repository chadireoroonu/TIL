import json
from pprint import pprint


def movie_info(movie, genres):
    pass 

    new_dict = {
        'id': movie['id'],
        'title': movie['title'],
        'poster_path': movie['poster_path'],
        'vote_average': movie['vote_average'],
        'overview': movie['overview'],
        'genre_ids': movie['genre_ids']
    }

    
    genres_names = [] # 장르네임을 담아줄 빈 리스트 생성
    for j in range(len(movie['genre_ids'])): # 장르의 길이까지의 범위동안
        for i in range(len(genres_list)): # 장르리스트를 순회하며 같은 숫자를 찾아냄
            if movie['genre_ids'][j] == genres_list[i]['id']: # 같은 숫자를 비교할 대상
                genres_names.append(genres_list[i]['name']) # 일치하는 숫자의 장르 이름 추가
            else:
                pass


    del new_dict['genre_ids'] # 장르 아이디를 딕셔너리에서 삭제
    new_dict['genre_name'] = genres_names # 장르 네임을 딕셔너리에 추가

    # new_dict[5] = print(genres_name) 
    return new_dict


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))