# 데일리실습 7-1
class Nationality() :
    def __init__(self, name):
        self.name = name
    def __str__(self) :
        return f'나의 국적은 {self.name}'


korea_nationality = Nationality("대한민국")
print(korea_nationality) # 나의 국적은 대한민국


# # 데일리실습 7-2
# class Wordrelay():
#     # 1. words 리스트를 전달받아 인스턴스 변수로 만드는 생성자를 구현하세요
#     # def __init__(self ~~~~ )

#     # 2. 실패와 성공 여부를 결정하는 함수를 구현하세요
#     def check_fail(self):
#         pass
    
#     # 3. 결과를 돌려주는 함수를 작성하세요.
#     def get_result(self):
#         pass


# if __name__ == '__main__':
#     words = ["round","dream","magnet","tweet","tweet","trick","kiwi"]
#     wordrelay = Wordrelay(words)
#     print(wordrelay.get_result()) # 5번째 참가자가 탈락하였습니다.
