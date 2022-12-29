from tkinter import *
from gensim.models import KeyedVectors

pencere1 = Tk()
pencere1.title("Optimizasyona Hoşgeldiniz")
kelimeVektoru = KeyedVectors.load_word2vec_format('trModel100', binary=True)
def kelimeal():
    anahtarKelimeler = entry.get().split()
    print("Girilen kelimeler: " + " ".join(anahtarKelimeler))
    if anahtarKelimeler:
        try:
            oneriler = kelimeVektoru.most_similar(positive=anahtarKelimeler)
            for oneri in oneriler:
                if not any(keyword in oneri[0] for keyword in anahtarKelimeler):
                    label3 = Label(pencere1, text= "Benzer Kelime:" + oneri[0])
                    label3.pack()
                    label2 = Label(pencere1, text="https://www.google.com.tr/search?q=" + oneri[0])
                    label2.pack()
        except KeyError:
            label4 = Label(pencere1, text="Kelime bulunamadı.", fg="white", bg="red", font="Times 14" )
            label4.pack()

pencere1.title("Kelime Optimizasyonu")
label1 = Label(pencere1, text=" Anahtar kelime giriniz: ", font="Times 14 bold")
label1.pack()
entry = Entry(pencere1, bg = "white", fg = "black", width=15, borderwidth=10,)
entry.pack()
buton1 = Button(pencere1, text="Ara", bg="black", fg="white", font="Times 14 bold", command=kelimeal)
buton1.pack()
pencere1.mainloop()