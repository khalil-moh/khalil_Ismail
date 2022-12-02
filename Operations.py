from ClientsClass import Clients
from LibrarianClass import Libarian
from BooksClass import Book
from BorrowingOrder import Borrowing_Order


class LibraryOperations :
    clients_list:list[Clients]=[]
    id_counter = 1

    def add_clients(self,full_name:str,age,id_no,phone_number):
        if full_name.isspace() or full_name == None:
            print("un")
            return

        cli = Clients(full_name=full_name,age=age,id_no=id_no,phone_number=phone_number,id=self.id_counter)
        self.id_counter += 1
        self.clients_list.append(cli)

class BookOperations :
    clients_list:list[Clients]=[]
    id_counter = 1

    def add_clients(self,full_name:str,age,id_no,phone_number):
        if full_name.isspace() or full_name == None:
            print("un")
            return

        cli = Clients(full_name=full_name,age=age,id_no=id_no,phone_number=phone_number,id=self.id_counter)
        self.id_counter += 1
        self.clients_list.append(cli)