from booth_form import *
from add_form import *
from div_form import *


def add():
    AddForm(1)


def sub():
    AddForm(0)


def main():
    rootmain = Tk()
    rootmain.title('Calculator')

    Label(rootmain, text="Calculator").pack()

    Label(rootmain, text="ـــــــــــــــــــــــــــــ").pack()

    Label(rootmain, text="  ").pack()

    Button(rootmain, text="      ADDITION      ", command=add).pack()

    Label(rootmain, text="  ").pack()

    Button(rootmain, text="  SUBTRACTION  ", command=sub).pack()

    Label(rootmain, text="  ").pack()

    Button(rootmain, text="MULTIPLICATION", command=BoothForm).pack()

    Label(rootmain, text="  ").pack()

    Button(rootmain, text="       DIVISION       ", command=DivForm).pack()

    Label(rootmain, text="  ").pack()

    rootmain.mainloop()


main()
