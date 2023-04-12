from django.shortcuts import render
from .models import PetSitter, Pet
from django.db import connection
from django.db import reset_queries

# Create your views here.

# 데코레이터 함수
def get_sql_qureies(origin_func):
    def wrapper(*args, **kWargs):
        reset_queries()

        # origin_func()
        pet_qs = Pet.objects.all()
        for pet in pet_qs:
            print(pet.name, pet.pet_sitter.first_name)

        query_info = connection.queries
        for query in query_info:
            print(query['sql'])

    return wrapper

# 요청이 아닌 진짜 함수 | 모든 펫의 집사 이름을 출력
# 장고 내부 기능을 사용하니 shell 에서 실행
def get_pet_data():
    # reset_queries()

    # 내가 원하는 ORM
    pets = Pet.objects.all()
    for pet in pets:
        print(f'{pet.name} | 집사 {pet.pet_sitter.first_name}')

    # 실제 함수 출력시 어떤 식으로 sql이 나가는지 for문을 돌며 출력
    # 상단 reset_queries() 포함
    # query_info = connection.queries
    # for query in query_info:
    #     print(query['sql'])