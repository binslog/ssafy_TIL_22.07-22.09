
## 데일리실습 8-2
## 이름과 나이를 인스턴스로 하는 인자를 생성. details/check_age

class Person() :
    def __init__(self,name,age) :
        self.name = name
        self.age = age

    @classmethod # @classmethod 가져오는 것이 포인트!
    def detail(cls,name,year): # detail을 선언할 때는 cls를 가져온다.
        age = 2022 - int(year) + 1  # age는 local variable            
        return cls(name,str(age))

    def check_age(self) :
        print(f'현재 나이는 {self.age}살 입니다.')
        if int(self.age) > 19 :
            return True
        return False


person2 = Person.detail('박승빈',2000)
print('미성년자 입니다.') if person2.check_age() == True else print('성인입니다.')



## 데일리실습 8-3
## 탑승객 수(passengers) 와 요금(fare)를 받는다.
class PublicTransport():
    # 탑승객 수와 요금을 입력받아 초기화하는 메서드
    def __init__ (self,passengers,fare) :
        self.passengers = passengers # 인당 요금
        self.fare = fare
        self.total = 0

    # 탑승 메서드
    # passenger 를 파라미터로 받음
    # 새로 탄 승객에 따라 총 요금에 추가
    def get_in(self, passenger):
        self.passengers += passenger
        self.total += passenger * self.fare

    # 내리는 메서드
    # 승객 수만 감소
    def get_off(self, passenger):
        self.passengers -= passenger

    # 현재 탑승중인 인원과 최종 수익을 출력
    def profit(self):
        print(f'현재 탑승중인 인원: {self.passengers} / 총 수익: {self.total}')

if __name__ == '__main__':
    transport = PublicTransport(0, 100)
    transport.get_in(20)
    transport.get_in(10)
    transport.get_in(40)
    transport.get_off(30)
    transport.profit() # 탑승인원 : 40 / 총 수익 : 7000


# 8-4 
# 오버라이딩 : 무시하다, 우선하다.
# 말 그대로 기반 클래스의 메서드를 무시하고 새로운 메서드를 반든다.

# 8-3 함수 가져오고 싶을 때, from 함수 import 파일명

class Bus(PublicTransport):
    def __init__(self, limit, passengers, fare) :
        self.limit=limit 
        super().__init__(passengers, fare) # 버스에서도 탑승객 인스턴스 변수 쓰고 싶다!!

    def test(self):
        print('self.limit = ' , self.limit)
        print('self.pessengers = ' , self.passengers)
        print('self.fare = ' , self.fare)
        print('self.total = ' , self.total)

    # override
    def get_in(self, passenger) :
        if self.passengers + passenger > self.limit :
            print('더 이상 탑승할 수 없습니다.')
        else:
            self.passengers += passenger
            self.total += passenger * self.fare
            print(f'현재 탑승중인 인원 : {self.passengers}')

if __name__ == '__main__' :
    bus = Bus(100,0,1200)
    bus.get_in(90)
    bus.get_off(30)
    bus.profit()
    bus.get_in(20)
    bus.profit()


# 데일리과제 8-2. 객체지향의 특성과 심화 사용


class Point :
    def __init__(self,x,y) :
        self.x=x
        self.y=y

# p1 = Point(x=1, y=3)
# p2 = Point(x=3, y=1)
# p3 = Point(x=3, y=7)
# p4 = Point(x=6, y=4)
# 굳이 할 필요가 없다!

class Rectangle(Point) :
    def __init__(self,p1,p2) :
        self.p1=p1
        self.p2=p2

    def get_area(self) :
        return abs((self.p2.x - self.p1.x)) * abs((self.p2.y - self.p1.y))

    def get_perimeter(self) :
        return (abs(self.p2.x - self.p1.x) + abs(self.p2.y - self.p1.y)) * 2

    def is_square(self):
        return abs(self.p2.x - self.p1.x) == abs(self.p2.y - self.p1.y)


p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)

print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)

print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())

__



