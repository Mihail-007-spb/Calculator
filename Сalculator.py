"""Calculator"""

"""Калькулятор"""



from tkinter import Tk, W, E, StringVar
from tkinter.ttk import Frame, Button, Entry, Style
import math


def get_proc():
    entry.delete(0, len(entry.get()) - 3)
    g = float(entry.get())
    print(g)
    pr = (d*(100+g))/100
    entry.delete(0, 50)
    pr_r = round(pr, 2)
    entry.insert('0', pr_r)
    #дельта процента в числе
    pr_s = (d - pr)
    pr_s0 = round(pr_s, 2)
    pr_0 = abs(pr_s0)
    print(pr_0)
    entry.insert('end', ('[%s]' % pr_0))


def plus():
    global entry, d
    d = float(entry.get())
    entry.insert('end', '+')
    print(d)


def minus():
    global entry, d
    d = float(entry.get())
    entry.insert('end', '-')
    print(d)


def get_ver():
    ver = float(entry.get()) * 1.0668
    entry.delete(0, 50)
    ver_r = round(ver, 3)
    entry.insert('0', ver_r)
    entry.insert('end', "км")


def get_sin():
    s = math.sin((0.017453292519943295 * float(entry.get())))
    entry.delete(0, 50)
    s_r = round(s, 4)
    entry.insert('0', s_r)


def get_cos():
    cos = math.cos(0.017453292519943295 * (float(entry.get())))
    entry.delete(0, 50)
    cos_r = round(cos, 4)
    entry.insert('0', cos_r)


def get_tg():
    tg = math.tan(0.017453292519943295 * (float(entry.get())))
    entry.delete(0, 50)
    tg_r = round(tg, 4)
    entry.insert('0', tg_r)


def get_ctg():
    tg = math.tan(0.017453292519943295 * (float(entry.get())))
    ctg = 1/tg
    entry.delete(0, 50)
    ctg_r = round(ctg, 4)
    entry.insert('0', ctg_r)


def get_vet():
    vet = float(entry.get()) * 3.6
    entry.delete(0, 50)
    vet_r = round(vet, 3)
    entry.insert('0', vet_r)
    entry.insert('end', "км/ч")


def get_fut():
    fut = float(entry.get()) * 30.48
    entry.delete(0, 50)
    fut_r = round(fut, 3)
    entry.insert('0', fut_r)
    entry.insert('end', "см")


def get_u():
    u = float(entry.get()) * 28.35
    entry.delete(0, 50)
    u_r = round(u, 3)
    entry.insert('0', u_r)
    entry.insert('end', "г")


def get_f():
    f = float(entry.get()) * 453.59/1000
    entry.delete(0, 50)
    f_r = round(f, 3)
    entry.insert('0', f_r)
    entry.insert('end', "кг")


def get_km_avto():
    km_a = float(entry.get())*1.61
    entry.delete(0, 50)
    km_a_r = round(km_a, 3)
    entry.insert('0', km_a_r)
    entry.insert('end', "км/ч")


def get_Celc():
    cel = (float(entry.get()) - 32)/1.8
    entry.delete(0, 50)
    cel_r = round(cel, 3)
    entry.insert('0', cel_r)
    entry.insert('end', "гр.Цельсия")


def get_km():
    km = 1.852 * float(entry.get())
    entry.delete(0, 50)
    km_r = round(km, 3)
    entry.insert('0', km_r)
    entry.insert('end', "км/ч")


def get_sm():
    cm = 2.54*float(entry.get())
    entry.delete(0, 50)
    cm_r = round(cm, 3)
    entry.insert('0', cm_r)
    entry.insert('end', "см")


def get_kor_Kvad():
    k_kv = math.sqrt(float(entry.get()))
    entry.delete(0, 50)
    k_kv_r = round(k_kv, 5)
    entry.insert('0', k_kv_r)


def get_Rad():
    rad = math.radians(float(entry.get()))
    entry.delete(0, 50)
    rad_r = round(rad, 5)
    entry.insert('0', rad_r)
    entry.insert('end', "радиан")


def get_Pi():
    a = math.pi
    entry.insert('end', a)
    print(a)


def get_M():
    entry.insert('end', m)


def save_M():
    global m
    m = entry.get()


def rezult():
    v = entry.get()
    r = eval(v)
    entry.delete(0, 50)
    r_r = round(r, 5)
    entry.insert(0, r_r)
    print('Введено:', v)
    print('Расчет:', r)


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        s = ' '
        self.master.title(s * 40 + "КАЛЬКУЛЯТОР")
        #self.master.resizable(0, 0)
        self.master.wm_attributes('-topmost', 1)
        self.master.geometry('880x240+350+150')
        self.master.iconbitmap(default=r"C:\\FOTO  Python\\gingerbread.ico")

        Style().configure("TButton", padding=(0, 5, 0, 5),
                          font=('serif', 12, 'bold'), background="green")

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)
        self.columnconfigure(4, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)

        global var1, entry
        self.var1 = StringVar()
        entry = Entry(self, textvariable=self.var1, font='serif 15')
        entry.grid(row=0, columnspan=3, sticky=W + E)

        cls = Button(self, text="M сохр.", command=save_M)
        cls.grid(row=1, column=0)
        bck = Button(self, text="M вызв.", command=get_M)
        bck.grid(row=1, column=1)
        lbl = Button(self, text="(",
                     command=lambda: entry.insert('end', '('))
        lbl.grid(row=1, column=2)
        clo = Button(self, text=")",
                     command=lambda: entry.insert('end', ')'))
        clo.grid(row=1, column=3)
        sev = Button(self, text="7",
                     command=lambda: entry.insert('end', '7'))
        sev.grid(row=2, column=0)
        eig = Button(self, text="8",
                     command=lambda: entry.insert('end', '8'))
        eig.grid(row=2, column=1)
        nin = Button(self, text="9",
                     command=lambda: entry.insert('end', '9'))
        nin.grid(row=2, column=2)
        div = Button(self, text="/",
                     command=lambda: entry.insert('end', '/'))
        div.grid(row=2, column=3)

        fou = Button(self, text="4",
                     command=lambda: entry.insert('end', '4'))
        fou.grid(row=3, column=0)
        fiv = Button(self, text="5",
                     command=lambda: entry.insert('end', '5'))
        fiv.grid(row=3, column=1)
        six = Button(self, text="6",
                     command=lambda: entry.insert('end', '6'))
        six.grid(row=3, column=2)
        mul = Button(self, text="*",
                     command=lambda: entry.insert('end', '*'))
        mul.grid(row=3, column=3)

        one = Button(self, text="1",
                     command=lambda: entry.insert('end', '1'))
        one.grid(row=4, column=0)
        two = Button(self, text="2",
                     command=lambda: entry.insert('end', '2'))
        two.grid(row=4, column=1)
        thr = Button(self, text="3",
                     command=lambda: entry.insert('end', '3'))
        thr.grid(row=4, column=2)
        mns = Button(self, text="-", command=minus)

                     #command=lambda: entry.insert('end', '-'))
        mns.grid(row=4, column=3)

        zer = Button(self, text="0",
                     command=lambda: entry.insert('end', '0'))
        zer.grid(row=5, column=0)
        dot = Button(self, text=".",
                     command=lambda: entry.insert('end', '.'))
        dot.grid(row=5, column=1)
        equ = Button(self, text="=",
                     command=rezult)
        equ.grid(row=5, column=2)
        pls = Button(self, text="+", command=plus)
        pls.grid(row=5, column=3)

        # новые кнопки
        b1 = Button(self, text="кв.\u221a", command=get_kor_Kvad)
        b1.grid(row=1, column=4)

        b2 = Button(self, text="Град. в рад.", command=get_Rad)
        b2.grid(row=2, column=4)

        b3 = Button(self, text='π', command=get_Pi)
        b3.grid(row=3, column=4)

        b4 = Button(self, text="Дюйм в см", command=get_sm)
        b4.grid(row=4, column=4)

        b5 = Button(self, text="%", command=get_proc)
        b5.grid(row=5, column=4)

        b6 = Button(self, text="◄ Удалить",
                    command=lambda: entry.delete(len(entry.get()) - 1))
        b6.grid(row=0, column=3)

        b7 = Button(self, text="ОЧИСТИТЬ", command=lambda: entry.delete(0, 50))
        b7.grid(row=0, column=4)

        #дополнительные кнопки
        b8 = Button(self, text="Узлы в км/ч", command=get_km)
        b8.grid(row=0, column=5)

        b9 = Button(self, text="Фар. в цел", command=get_Celc)
        b9.grid(row=1, column=5)

        b10 = Button(self, text='Мили в км/ч', command=get_km_avto)
        b10.grid(row=2, column=5)

        b11 = Button(self, text="М/С в км/ч", command=get_vet)
        b11.grid(row=3, column=5)

        b12 = Button(self, text="Фунт в кг", command=get_f)
        b12.grid(row=4, column=5)

        b13 = Button(self, text="Унция в г", command=get_u)
        b13.grid(row=5, column=5)

        # дополнительные кнопки
        b14 = Button(self, text="Фут в см", command=get_fut)
        b14.grid(row=0, column=6)

        b15 = Button(self, text="Верста в км", command=get_ver)
        b15.grid(row=1, column=6)

        b16 = Button(self, text='sin', command=get_sin)
        b16.grid(row=2, column=6)

        b17 = Button(self, text="cos", command=get_cos)
        b17.grid(row=3, column=6)

        b18 = Button(self, text="tg", command=get_tg)
        b18.grid(row=4, column=6)

        b19 = Button(self, text="ctg", command=get_ctg)
        b19.grid(row=5, column=6)

        # дополнительные кнопки
        b20 = Button(self, text="")
        b20.grid(row=0, column=7)

        b21 = Button(self, text="", command=get_ver)
        b21.grid(row=1, column=7)

        b22 = Button(self, text='', command=get_sin)
        b22.grid(row=2, column=7)

        b23 = Button(self, text="", command=get_cos)
        b23.grid(row=3, column=7)

        b24 = Button(self, text="", command=get_tg)
        b24.grid(row=4, column=7)

        b25 = Button(self, text="", command=get_ctg)
        b25.grid(row=5, column=7)

        self.pack()


def main():
    root = Tk()
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
