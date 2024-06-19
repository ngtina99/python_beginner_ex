from chef import Chef

class ChineseChef(Chef): #inherit, you can overwrite it
    
    def make_special(self):
        print("The chef makes an orange chicken")
    def make_fried_rice(self):
        print("The chef makes a fried rice")