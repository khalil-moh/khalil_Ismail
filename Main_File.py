from Operations import LibraryOperations
kh_LibraryOperations = LibraryOperations()
print("مرحبا بكم في المغازي ")
def get_client():
     full_name= input()
     age=input()
     id_no = input()
     phone_number=input()
     kh_LibraryOperations.add_clients(full_name=full_name, age=age, id_no=id_no, phone_number=phone_number)
get_client()
