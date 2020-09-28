from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("Text Box")


class DropDownList(UIControl):
    def draw(self):
        print("Drop Down List")


# def draw(controls):
#     for control in controls:
#         control.draw()


def draw(control):
    control.draw()


# program utama
ddl = DropDownList()
textbox = TextBox()
# print(draw([ddl, textbox]))
print(draw(ddl))
print(draw(textbox))
