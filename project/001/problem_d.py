import json


def max_revenue(movies):
    pass 
    # 여기에 코드를 작성합니다.  

    list_movie = [] # 정보를 담아줄 새 리스트 생성
    for t in range(len(movies_list)): # t가 무비리스트의 길이 범위안에 있을 때
        new_dict = { 
        'title': movies_list[t]['title'], # 무비 리스트의 t번째 항목의 정보들 수집
        }

        list_movie.append(new_dict)
    # print(list_movie)
        
        movies_num = [13, 122, 129, 155, 238, 278, 311, 424, 497, 550, 598, 637, 
        680, 914, 4935, 11216, 324857, 372058, 378064, 496243, 527774, 572154]

        for i in range(len(movies_num)):
            new_movie_json = open(f'data/movies/{movies_num[i]}.json', encoding='utf-8')
            new_movies = json.load(new_movie_json)
            for j in range(len(list_movie)):
                if list_movie[j]['title'] == new_movies['title']:
                    list_movie[j]['revenue'] = new_movies['revenue']

        # # print(new_dict)
    # print(list_movie)
    max_revenue = 0
    the_num = []
    for k in range(len(list_movie)):
        if list_movie[k]['revenue'] > max_revenue:
            max_revenue = list_movie[k]['revenue']
            the_num.append(k)
    
    return list_movie[the_num[-1]]['title']


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))