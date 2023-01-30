def label(func):
    def wrapper(name):
        print(name, end=' : ')
        func(name)
    return wrapper

def prof(name):
    # name : 반갑네 {name} 교수라네
    print(f'반갑네 {name} 교수라네.')
    print('과제 했나?')

def student(name):
    # name : 안녕하세요, {name} 입니다.
    print(f'안녕하세요, {name} 입니다.')

label('이름', prof)
label('이름', student)