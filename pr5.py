#리팩토링 작업 더 깔끔한 캡슐화 시킬것

import tkinter as tk
class NoticeBoard :
    def __init__(self,name):  
        self.name= name
        self.__board={}
        self.__temporary_stroage ={}
    def write(self,title,deatil): 
        print(f"임시저장 되었습니다.[{title}]")
    def save(self):
        self.board.update(self.temporary_stroage)
        self.temporary_stroage = {}
        print("board에 저장했습니다.")
    def check(self,name) :
        if name in self.board : 
            print(f"저장된글[{name}]")
        elif name in self.temporary_stroage :
            print(f"임시저장된글[{name}]")
        else :
            print("저장된 글이 없습니다.")
    def output(self,name) :
        if name in self.board :
            print(f"내용{self.board[name]}")
    def delete(self,name) :
        if name in self.board :
            del self.board[name]
            print(f"[{name}]을 지웠습니다")
nb = NoticeBoard("코코몽매니아")
