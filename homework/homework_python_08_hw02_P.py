'''
스택(Stack)은 LIFO(Last in First Out)으로 구조화된 자료구조를 의미한다. 
아래 구성요소를 포함하는 Stack class를 생성하라.

구성 요소(메서드)      
i.  __init__(): 인스턴스가 생성될 때 빈 리스트를 각 인스턴스의 이름 공간에 넣는다.      
ii. empty(): 스택이 비었다면 True을 반환하고, 그렇지 않다면 False를 반환한다.      
iii.top(): 스택의 가장 마지막 데이터를 반환한다. 스택이 비었다면 None을 반환한다.      
iv. pop(): 스택의 가장 마지막 데이터의 값을 반환하고, 해당 데이터를 삭제한다. 스택이 비었다면 None을 반환한다.
v.  push(): 스택의 가장 마지막 데이터 뒤에 값을 추가한다. 반환값은 없다.      
vi. __repr__: 현재 스택의 요소들을 보여준다.
'''
class Stack: # 스택 클래스 생성
    pass

    def __init__(self): # 인스턴스 생성 시 빈 리스트 생성
        self = []
    
    def empty(self):
        if self == []: # 만약 인스턴스가 비어있다면 True를 반환
            return True
        else: # 어떤 요소를 가지고있다면 False를 반환
            return False

    def top(self): 
        if self != []: # 만약 인스턴스가 빈 리스트가 아니라면 마지막 요소 반환
            return self[-1] # 인스턴스가 비어있다면 None 반환될 것
        
    def pop(self): 
        if self != []: # 만약 인스턴스가 빈 리스트가 아니라면 마지막 요소 반환 및 삭제
            return self.pop[-1] # 인스턴스가 비어있다면 None이 반환될 것

    def push(self, x): # 인스턴스에 push와 함께 값을 입력하면
        self.push(x) # 해당 값을 인스턴스에 추가

    def __repr__(self): # 인스턴스의 현재 요소들을 출력
        return print(self)