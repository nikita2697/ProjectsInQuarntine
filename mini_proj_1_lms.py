class Library:
    aval_books=["Harry Potter","Panchantra","Champak","Kuran"]
    taken_books={}
    def __init__(self,name):
        self.name=name
    def add_books(self,booknm):
        self.bookname=booknm
        self.aval_books.append(self.bookname)

    def print_books(self):
        for i in range(len(self.aval_books)):
            print(self.aval_books[i],end="  ")

    def print_aval_books(self):
        for i in range(len(self.aval_books)):
            print(f"{i}\t for {self.aval_books[i]}")

    def give_book(self,selected_book):
        self.selected=selected_book
        if self.aval_books[self.selected] in self.taken_books:
            print("Sorry this book is Already Taken!!")
        else:
            print(f"You have Taken {self.aval_books[self.selected]} ")
            self.taken_books.update({self.aval_books[self.selected]:self.name})
            print(self.taken_books)
    def return_book(self,rb):
        self.rb=rb
        for i,j in self.taken_books:
            if i==self.rb and j == self.name:
                self.taken_books.pop(self.rb)
                print("Successfully returned")
                print(self.taken_books)
        else:
            print("nothing to delet")


print("Enter your name:")
nm=input()
x=Library(nm)
print(f"Hello {nm} Welcome To our Library!!!\n\nWhat action do you want to perform?")
c='y'
while c!='n':

    print("\nEnter 1 for View Available Books:\nEnter 2 for lend book\nEnter 3 for donate book\n4 for return book")
    action=int(input())
    if action==2:
        print("Select books")
        x.print_aval_books()
        a=int(input())
        x.give_book(a)
    elif action==1:
        x.print_books()
    elif action==3:
        print("Enter book name:")
        a=input()
        x.add_books(a)
    elif action==4:
        print("Enter book name:")
        bk=input()
        x.return_book(bk)
    else:
        print("invalid i/p:")


    c = input("\ndo you want to perform more?[y/n]")


    # if c == 'n':
    #     break;
print("\nThanks for using our library!!!")
