import json
from pprint import pprint


def movie_info(movies, genres):
    pass
    list_movie = [] # 정보를 담아줄 새 리스트 생성
    for t in range(len(movies_list)): # t가 무비리스트의 길이 범위안에 있을 때
        new_dict = {
        'id': movies_list[t]['id'], # 무비 리스트의 t번째 항목의 정보들 수집
        'title': movies_list[t]['title'],
        'poster_path': movies_list[t]['poster_path'],
        'vote_average': movies_list[t]['vote_average'],
        'overview': movies_list[t]['overview'],
        'genre_ids': movies_list[t]['genre_ids']
        }
        
        genres_names = [] # 장르네임을 담아줄 빈 리스트 생성
        for j in range(len(movies_list[t]['genre_ids'])): # 장르의 길이까지의 범위동안
            for i in range(len(genres_list)): # 장르리스트를 순회하며 같은 숫자를 찾아냄
                if movies_list[t]['genre_ids'][j] == genres_list[i]['id']: # 같은 숫자를 비교할 대상
                    genres_names.append(genres_list[i]['name']) # 일치하는 숫자의 장르 이름 추가
                else:
                    pass

        del new_dict['genre_ids'] # 장르 아이디를 딕셔너리에서 삭제
        new_dict['genre_name'] = genres_names # 장르 네임을 딕셔너리에 추가

        list_movie.append(new_dict)
        
    return list_movie

    # del new_dict['genre_ids'] # 장르 아이디를 딕셔너리에서 삭제
    # new_dict['genre_name'] = genres_names # 장르 네임을 딕셔너리에 추가

    # # new_dict[5] = print(genres_name) 
    # return new_dict
  
            


        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
