#문법적인 과정들을 다 활용해보고싶어서 자판기를 만들어보기로함

# 자판기에 뭐가 필요할까
# 자판기구조 돈 이라는 입력이 들어가서 무엇인가를 선택하면 
# 무엇 결과물 이 나온다 ,그리고 상태가변한다. 

# 자판기를 만들어놓고  
# 굳이 자판기를 해야하나 게시판을 만들어보자,게시판    Class 게시판 의 속성 정의
# 1.게시판 저장할것 리스트,딕셔너리,DB,서버 뭐 어떤것이든   저장소 [],{},file
# 2.입력 받는것 자판기와 다른점은 토큰개념이 사용자의 입력이다. input 
# 3.그다음 사용자의 입력을 저장소에 저장한다.  저장, 할당 ,추가
# 4.저장한 내용을 조회할수 있다                     조회
# 5.저장한 내용을 출력해서 보여준다.            print, 띄워줄수있고    
# 6.저장한 내용을 지울수있다.                   del 
# 그럼 게시판 자체의 기본적인 속성을 정의하고
#         속성내에 저장할것을 설정하고

#         기능을 분류해서 글쓰기기능

#                         글 저장기능
#                         글 조회기능
#                         글 출력기능
#                         글 삭제기능
# 거기에 어제배운 tkinter 으로 구현해보는 작업을 해보자 그전에 기본로직은 새워보자
import tkinter as tk
class NoticeBoard :#일단 노트북이라는 큰것을 만들고
    def __init__(self,name):  #무엇이 필요할까?,모듈화? 깔아놓고? 어떤것을 깔아놓아야하나?
        self.name= name
        self.board={}#저장할 공간은 리스트로해야하나,딕셔너리로 해야하나? 또무엇이 있어야하지? self저장할공간이 DB일경우에는? 
        self.temporary_stroage ={}#글을 쓰면 임시저장 공간에 담아놓고 그것을 저장하는 느낌
        # self.list = [
        #     self.board,
        #     self.temporary_stroage
        # ]
    def write(self,title,deatil): #글을 쓴다면 어디다가 쓸것인가?
        self.temporary_stroage[title] = deatil
    def save(self):
        self.board.append += self.temporary_stroage
        self.temporary_stroage = {}
        return
    def check(self,name) :
        if name in self.board : 
            print(f"저장된글{name["title"]}")
        if name in self.temporary_stroage :
            print(f"임시저장된글{name["title"]}")
        else :
            print("저장된 글이 없습니다.")
    def output(self,name) :
        if name in self.board :
            print(f"{self.board}")
    def delete(self,name) :
        if name == self.board["title"] :
            del self.board["title"]
    nb =
        








