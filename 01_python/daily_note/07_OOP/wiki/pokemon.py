# 푸키먼이라는 게임 만들기
# 푸키먼은 가상 세계의 동물들이 있는데
# 각각 고유의 lv, hp, skill, info 를 가진 생명체
# 푸키먼 둘이 만나면 싸우는데, 한쪽의 hp가 0이 될때까지 싸움

# 공통 속성을 가진 객체를 정의
# 클래스명 정의시, ClassName -> Pascal Case -> 단어 기준으로 맨 앞글자 대문자 처리
class Pokemon:
    # 모든 푸키먼들이 공통으로 가지는 속성
    # 클래스 변수, 클래스 속성
    info = '푸키먼...'
    population = 0

    # 생성자
    # 매직 메서드 -> __name__
    # 인스턴스 메서드 -> 첫번째 인자는 자기 자신
    # 함수 정의하는 것과 동일하다 -> 모든 규칙이 똑같이 작동
    def __init__(self, name, lv=1):
        # classmethod인 increase를 호출
        Pokemon.increase()

        # 인스턴스 변수에 생성될 때 넘겨받은 이름을 할당
        self.name = name
        self.lv = lv
        # 스킬명과 공격력 같이 입력받음
        self.skill = ('몸통 박치기', 10)
        self.hp = 100

        # 본인만의 독특한 소개법
        self.info = self.name[:2] * 2

    # 행동을 정의해보자
    # 인스턴스 메서드 -> 첫 번째 인자로 self를 넘겨받고,
    # 인스턴스가 접근 가능한 메서드 (함수)
    def attack(self):
        print(f'{self.info}')
        return self.skill[1] # 공격력

    @classmethod
    def increase(cls):
        cls.population += 1

    # 첫 번째 인자로 self, cls 둘다 받지 않는다.
    @staticmethod
    def battle(pok1, pok2): # 함수 정의와 동일
        # 영원히 싸움
        while True:
            pok2.hp -= pok1.attack()
            if pok2.hp <= 0:
                print(f'{pok2.name}이 쓰러졌다.')
                return
            
            pok1.hp -= pok2.attack()
            if pok1.hp <= 0:
                print(f'{pok1.name}이 쓰러졌다,')
                return
            

# pika == Pokemon의 인스턴스
# 생성자에는 2개 인자를 입력하기로 함
# lv은 기본 값이 있어서 이름만 입력해도 됨
# print(Pokemon.population, '피카츄 태어나기 전')
# pika = Pokemon('피카츄') # 새로운 객체를 생성하여 pika에 할당
# print(Pokemon.population, '피카츄 태어난 이후')
# print(pika.name)
# print(pika.lv, pika.skill, pika.hp)
# print(pika.info)
# pika.attack()

# # 똑같이 Pokemon에 해당하는 새로운 객체를 생성한다.
# meta = Pokemon('메타몽', 5)
# print(meta.name)
# print(meta.lv, meta.skill, meta.hp)
# print(meta.info)
# meta.attack()

# Pokemon.battle(pika, meta)
# pika.battle(pika, meta)

# print(pika.population) # 접근해서 출력은 가능한데

# pika.population += 1
# print(pika.population)      # 1
# print(Pokemon.population)   # 0