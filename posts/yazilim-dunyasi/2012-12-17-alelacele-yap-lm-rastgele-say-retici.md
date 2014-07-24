<!--
.. date: 2012-12-17 14:13:00
.. slug: alelacele-yapilmis-rastgele-sayi-uretici
.. title: Alelacele yapılmış rastgele sayı üretici
.. description: Tkinter kullanarak yapılmış, belli bir aralıkta rasgele sayılar üretmeye yarayan bir programcık.
-->


Aynı zamanda ilk, muhtemelen son Tkinter programım. Zaten arayüz
oluşturmayı da hiç sevmem :) <!-- TEASER_END -->

    :::python
    from Tkinter import *
    from random import shuffle
    
    master = Tk()
    Label(master, text="Start:").pack()
    stt = Entry(master)
    stt.pack()
    stt.delete(0, END)
    stt.insert(0, "0")
    stt.focus_set()
    Label(master, text="End:").pack()
    end = Entry(master)
    end.pack()
    end.delete(0, END)
    end.insert(0, "500")
    Label(master, text="How Many?:").pack()
    kactane = Entry(master)
    kactane.pack()
    kactane.delete(0, END)
    kactane.insert(0, "10")
    
    scrollbar = Scrollbar(master)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    sonuclar = Listbox(master, width=50, height=20)
    sonuclar.pack()
    sonuclar.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=sonuclar.yview)
    
    def callback():
        sayilar = range(int(stt.get()),int(end.get()))
        shuffle(sayilar)
        sonuclar.delete(0, END)
        for i in range(int(kactane.get())):
            sonuclar.insert(END,sayilar[i])
        
    
    b = Button(master, text="generate", width=10, command=callback)
    b.pack()
    
    mainloop()