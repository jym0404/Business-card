class Card:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    def info(self):
        print("---------------------------")
        print("name:",self.name)
        print("phone:",self.phone)
        print("E - mail:",self.email)
        print("---------------------------")
    def edit_info(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    def write_info(self, name, po):
        f = open(po + "\\" + name, "wt")
        f.write("---------------------------\n")
        f.write("name:" + self.name + "\n")
        f.write("phone:" + self.phone + "\n")
        f.write("E - mail:" + self.email + "\n")
        f.write("---------------------------")
