class Doggy: # 도기 클래스를 생성
    num_of_dogs = 0 # 개는 한 마리도 없음
    birth_of_dogs = 0 # 태어난 개도 한 마리도 없음

    def __init__(self, name, dog): # 개가 태어날때는 이름과 견종을 입력
        Doggy.increase() # 개가 태어나면 영향을 받을 메서드

        self.name = name # 개 이름은 입력의 네임
        self.dog = dog # 개 견종은 입력의 개
        self.bark = ('baw_wow') # 바크를 입력하면 짖을 수 있음

    @classmethod # 클래스 메서드로 개가 태어날 경우 개와 태어난 개 수 +1    
    def increase(cls):
        cls.num_of_dogs += 1
        cls.birth_of_dogs += 1

    def __del__(self): # 개가 죽을 때는 self 값만 입력
        Doggy.dog_die() # 개가 죽으면 영향을 받을 메서드
        pass # 아무것도 출력하거나 반환하지 않음

    @classmethod # 클래스 메서드로 개가 죽을 경우 개 -1
    def dog_die(cls):
        cls.num_of_dogs -= 1

    @classmethod # 클래스 메서드로 상태를 물어볼 경우 태어난 개와 현재 개 수 반환
    def get_status(cls):
        return (cls.birth_of_dogs, cls.num_of_dogs)

choco = Doggy('choco', 'poodle') # 새 개 초코 태어남
# print(Doggy.num_of_dogs)       # 1
# print(Doggy.birth_of_dogs)     # 1
print(choco.bark) # 초코 짖음

del choco # 초코 죽음
# print(Doggy.num_of_dogs)       # 0
# print(Doggy.birth_of_dogs)     # 1

dubu = Doggy('dubu', 'jindo') # 새 개 두부 태어남

print(Doggy.get_status())        # (2, 1)
# 만약 dubu가 프린트 아래에 위치하면 죽어버림...!