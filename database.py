# name,address,phone
# 1) add data 2) show data 3) delete data

name = []
address = []
phone = []

while True:
    print("1. Add data\n2. Show data\n3. Delete data\n4. Exit")

    ch = int(input("Enter your choice:"))
    if ch == 1:
        # while n.isalpha() == False:
        
        n = input("Enter name:")
        while n.isalpha() != True:
            print("Invalid name!! Please try again")
            n = input("Enter name:")
        name.append(n)

        a = input("Enter address:")
        address.append(a)

        p = input("Enter phone number:")
        phone.append(p)

        print("-------------DATA STORED--------------")

    elif ch == 2:
        n = input("Enter name to display the data:") # karan
        if n in name:
            print("-----DATA FOUND------")
            index_num = name.index(n)
            print("Name:",name[index_num])
            print("Address:",address[index_num])
            print("Phone:",phone[index_num])
            print("--------------------------------------")
        else:
            print("-----DATA NOT FOUND------")

    elif ch == 3:
        n = input("Enter name to delete the data:") 
        if n in name:
            print("-----DATA FOUND------")
            index_num = name.index(n)
            name.pop(index_num)
            address.pop(index_num)
            phone.pop(index_num)
            print("------DATA DELETED------")

        else:
            print("-----DATA NOT FOUND------")
        








            

        
