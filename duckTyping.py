class TextBox:
    def draw(self):
        print("Text Box")


class DropDownList:
    def draw(self):
        print("Drop Down List")


def draw(controls):
    for control in controls:
        control.draw()


# program utama
ddl = DropDownList()
textbox = TextBox()
print(draw([ddl, textbox]))
# stringbiasa = "string"
# print(draw([ddl, textbox, stringbiasa]))
