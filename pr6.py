import tkinter as tk
class NoticeBoard :
    def __init__(self,name):  
        self.name= name
        self.__board={}
        self.__temporary_stroage ={} 
    def write(self,title,deatil): 
        self.__temporary_stroage[title] = deatil
        return True
        # print(f"임시저장 되었습니다.[{title}]")
    def save(self):
        self.__board.update(self.__temporary_stroage)
        self.__temporary_stroage = {}
        print("board에 저장했습니다.")
    def check(self,name) :
        if name in self.__board : 
            print(f"저장된글[{name}]")
        elif name in self.__temporary_stroage :
            print(f"임시저장된글[{name}]")
        else :
            print("저장된 글이 없습니다.")
    # def output(self,name) :
    #     if name in self.__board :
    #         print(f"내용{self.__board[name]}")
    def get_contet(self,name):#output코드 리팩토링 기능을 분리해서 데이터를 출력할수있게하고, 데이터를 처리해서 
        if name in self.__board :
            return self.__board[name]
        return None
    def output(self,name):
        content = self.get_contet(name)
        if content :
            print(f"내용:{content}")
    def delete(self,name) :
        if name in self.__board :
            del self.__board[name]
            print(f"[{name}]을 지웠습니다")
nb = NoticeBoard("코코몽매니아")