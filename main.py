clear = "\n" * 100
array = []


class User:
    def __init__(self):
        self.name = input("User Name: ").strip()
        self.email = input("User Email: ").strip()
        self.age = input("User Age: ").strip()

    def show(self):
        print("User Name:" + self.name)
        print("User Email:" + self.email)
        print("User Age :" + self.age)


Running = 1
while Running==1:
    print("1.Add User")
    print("2.Show User List")
    print("3.Delete User")
    print("4.Show User Data")
    print("5.Exit")
    inp = input("Your Input: ")
    if inp == "1":
        array.append(User())
        print(clear)
    elif inp == "2":
        print(clear)
        print("Users: ")
        for i in array:
            print(i.name)
        print("\n")
    elif inp == "3":
        del_name = input("Which user you want to delete: ")
        for s, i in enumerate(array):
            if i.name == del_name:
                array.pop(s)
        print(clear)
    elif inp == "4":
        print(clear)
        shw_name = input("Which user data you want to see: ")
        for i in array:
            if i.name == shw_name:
                i.show()
        print(2*"\n")
    elif inp == "5":
        print(inp)
        Running = 0