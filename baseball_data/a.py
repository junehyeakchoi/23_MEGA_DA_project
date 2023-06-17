class Book:
    def __init__(self,title,writer,publisher,status):
        self.title = title
        self.writer = writer
        self.publisher = publisher
        self.status = status

    def show(self):
        print("제목:",self.title)
        print("저자:",self.writer)
        print("출판사:",self.publisher)
        print("대출상태:",self.status)

class BookList:
    def __init__(self):
        self.bookList = []

    def addBooks(self, book):
        self.bookList.append(book)
        
    def showBooks(self):
        for book in self.bookList:
            book.show()

    def findBooks(self, find):
        for book in self.bookList:
            if book.title == find:
                return True
        return False
    
    def loan(self,findLoan):
        for book in self.bookList:                      
            if book.title == findLoan:
                if book.status == "대출 가능":
                    book.show()
                    loanBookChose = input("대출하시겠습니까?")
                    if loanBookChose == "yes" or "예":
                        print(book.status)
                        print("대출되었습니다.")
                        book.status = "대출됨"
                        book.show()

                    else:
                        print("취소되었습니다.")
                        break

                else:
                    print("이미 대출된 책입니다.")
                    break

            else:
                print("입력하신 책이 존재하지 않습니다.")
                break

    def delete(self,title):
        find = 0
        for book in self.bookList:
            if title == book.title:
                find = book              # ValueError:  list.remove(x): x not in list
        if find == 0:
            print("not")
        else:
            self.bookList.remove(find)
            
library = BookList()

while True:

    print("1. 책 추가")
    print("2. 책 보기")
    print("3. 책 찾기")
    print("4. 대출")
    print("5. 책 삭제")
    print("0. exit")

    option = input("선택 기능: ")

    if option == '1':

        # option1
        addBookTitle = input("제목: ")
        addBookWriter = input("저자: ")
        addBookPublisher = input("출판사: ")
        library.addBooks(Book(addBookTitle,addBookWriter,addBookPublisher,"대출 가능"))

    elif option == '2':

        # option2
        library.showBooks()
    
    elif option == '3':

        # option3
        findTitle = input("찾을 책의 제목 입력: ")

        if library.findBooks(findTitle):
            print("Find")

        else:
            print("not Found")

    elif option == '4':

        # option4
        loanBook = input("대출하실 책의 제목을 입력하세요: ")
        
        library.loan(loanBook)

    elif option == '5':

        # option5
        deleteBook = input("삭제할 책을 입력하세요: ")

        library.delete(deleteBook)

    elif option == '0':
        
        # option0 나가기
        break

    else:

        # fix
        print("잘못 입력되었습니다.")

    print('='*60)