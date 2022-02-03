from tkinter import *
from tkinter.messagebox import *
def sõnastik():
    tk={}
    file=open("tunnikirjeldus.txt","r")
    for line in file:
        tund, kirjeldus=line.strip().split(":")
        tk[tund.strip()]=kirjeldus.strip()
    file.close()
    print(tk)
    return tk
def kirjeldus_aknasse(t:str,r:str):
    if (askyesno("Küsimus","Kas tahad kirjeldust näha?")):
        alam_aken=Toplevel()
        alam_aken.title(r)
        lbl_kirjeldus=Label(alam_aken,text=tk[t]).pack()
        c=Canvas(alam_aken,height=640,width=640)
        file=PhotoImage(file=t)
        c.create_image(10,10,image=file,anchor=NW)
        c.pack()
        alam_aken.mainloop()
    else:
        showinfo("Vastus","Kui ei taha, siis ei taha!!!")
    print(tk[t])



tk=sõnastik()
aken = Tk()
aken.title("Tunniplaan")
aken.geometry("867x500")
p=["Esmaspäev","Teisipäev","Kolmapäev","Neljapäev","Reede"]
kell=["7:40 - 8:25","8:30 - 9:15","9:20 - 10:05","10:10 - 10:55","11:00 - 11:45","11:50 - 12:35","12:40 - 13:25","13:30 - 14:15","14:20 - 15:05","15:10 - 15:55","16:00 - 16:45"]
j=0



for i in range(1, 10, 2):
    Label(aken, height = 5, width = 15, text=p[j], relief = "groove").grid(row = i, column = 0, rowspan = 2, sticky = N+S+W+E)
    j+=1

#Ep = Label(aken, height = 5, width = 15, text = "Esmaspäev", relief = "groove").grid(row = 1, column = 0, rowspan = 2, sticky = N+S+W+E)
#Tp = Label(aken, height = 5, width = 15, text = "Teisipäev", relief = "groove").grid(row = 3, column = 0, rowspan = 2, sticky = N+S+W+E)
#Kp = Label(aken, height = 5, width = 15, text = "Kolmapäev", relief = "groove").grid(row = 5, column = 0, rowspan = 2, sticky = N+S+W+E)
#Np = Label(aken, height = 5, width = 15, text = "Neljapäev", relief = "groove").grid(row = 7, column = 0, rowspan = 2, sticky = N+S+W+E)
#Rp = Label(aken, height = 5, width = 15, text = "Reede", relief = "groove").grid(row = 9, column = 0, rowspan = 2, sticky = N+S+W+E)

for i in range(11):
    tn="t"+str(i)
    tn=Label(aken, text=str(i)+"\n"+kell[i],relief="ridge").grid(row=0,column=i+1,sticky=N+S+W+E)

#t0=Label(aken, text="0\n7:40 - 8:25",relief="ridge").grid(row=0,column=1,sticky=N+S+W+E)
#t1=Label(aken, text="1\n8:30 - 9:15",relief="ridge").grid(row=0,column=2,sticky=N+S+W+E)
#t2=Label(aken, text="2\n9:20 - 10:05",relief="ridge").grid(row=0,column=3,sticky=N+S+W+E)
#t3=Label(aken, text="3\n10:10 - 10:55",relief="ridge").grid(row=0,column=4,sticky=N+S+W+E)
#t4=Label(aken, text="4\n11:00 - 11:45",relief="ridge").grid(row=0,column=5,sticky=N+S+W+E)
#t5=Label(aken, text="5\n11:50 - 12:35",relief="ridge").grid(row=0,column=6,sticky=N+S+W+E)
#t6=Label(aken, text="6\n12:40 - 13:25",relief="ridge").grid(row=0,column=7,sticky=N+S+W+E)
#t7=Label(aken, text="7\n13:30 - 14:15",relief="ridge").grid(row=0,column=8,sticky=N+S+W+E)
#t8=Label(aken, text="8\n14:20 - 15:05",relief="ridge").grid(row=0,column=9,sticky=N+S+W+E)
#t9=Label(aken, text="9\n15:10 - 15:55",relief="ridge").grid(row=0,column=10,sticky=N+S+W+E)
#t10=Label(aken, text="10\n16:00 - 16:45",relief="ridge").grid(row=0,column=11,sticky=N+S+W+E)

#
lbl = Label(aken, text = "TARpv21", borderwidth = 2, relief = "groove").grid(row = 0, column = 0, sticky = N+S+W+E)

#Понедельник
b1 = Button(aken, text = "Multimeedia", bg = "cornflowerblue", relief = "groove",command=lambda:kirjeldus_aknasse("Multimeedia"))
b1.grid(row = 1, column = 2, columnspan = 2, sticky = N+S+W+E)
b2 = Button(aken, text = "Programmeerimise alused", bg = "skyblue", relief = "groove",command=lambda:kirjeldus_aknasse("Programmeerimise alused"))
b2.grid(row = 2, column = 2, columnspan = 3, sticky = N+S+W+E)
b3 = Button(aken, text = "Programmeerimise alused", bg = "skyblue", relief = "groove",command=lambda:kirjeldus_aknasse("ty.png","Programmeerimise alused"))
b3.grid(row = 1, column = 5, columnspan = 3, sticky = N+S+W+E)
b4 = Button(aken, text = "Multimeedia", bg = "cornflowerblue", relief = "groove",command=lambda:kirjeldus_aknasse("Multimeedia"))
b4.grid(row = 2, column = 5, columnspan = 2, sticky = N+S+W+E)
b5 = Button(aken, text = "Rühma \n juhataja \n tund", bg = "skyblue", relief = "groove",command=lambda:kirjeldus_aknasse("Rühma juhataja tund"))
#Вторник
b5.grid(row = 1, column = 8, rowspan = 2, sticky = N+S+W+E)
b6 = Button(aken, text = "Inglise keel", bg = "oldlace", relief = "groove",command=lambda:kirjeldus_aknasse("Inglise keel1"))
b6.grid(row = 3, column = 2, columnspan = 2, sticky = N+S+W+E)
b7 = Button(aken, text = "Inglise keel", bg = "plum", relief = "groove",command=lambda:kirjeldus_aknasse("Inglise keel2"))
b7.grid(row = 4, column = 2, columnspan = 2, sticky = N+S+W+E)
b8 = Button(aken, text = "Operatsiooni \n süsteemide \n alused", bg = "mediumorchid", relief = "groove",command=lambda:kirjeldus_aknasse("Operatsiooni süsteemide alused"))
b8.grid(row = 3, column = 4, columnspan = 2, rowspan = 2, sticky = N+S+W+E)
b9 = Button(aken, text = "Kehaline kasvatus", bg = "palevioletred", relief = "groove",command=lambda:kirjeldus_aknasse("Kehaline kasvatus"))
b9.grid(row = 3, column = 7, columnspan = 2, rowspan = 2, sticky = N+S+W+E)
b10 = Button(aken, text = "Eesti keel", bg = "orchid", relief = "groove",command=lambda:kirjeldus_aknasse("Eesti keel2"))
b10.grid(row = 3, column = 9, sticky = N+S+W+E)
b11 = Button(aken, text = "Eesti keel", bg = "thistle", relief = "groove",command=lambda:kirjeldus_aknasse("Eesti keel1"))
b11.grid(row = 4, column = 9, sticky = N+S+W+E)
b12 = Button(aken, text = "Ajalugu,\n inimgeo\n graafia \n ja inimese\n õpetus\n eesti keeles", bg = "wheat", relief = "groove",command=lambda:kirjeldus_aknasse("Ajalugu inimgeograafia ja inimese õpetus eesti keeles"))
#Среда
b12.grid(row = 3, column = 10, rowspan = 2, sticky = N+S+W+E)
b13 = Button(aken, text = "Programmeerimise alused", bg = "skyblue", relief = "groove",command=lambda:kirjeldus_aknasse("Programmeerimise alused"))
b13.grid(row = 5, column = 2, columnspan = 3, sticky = N+S+W+E)
b14 = Button(aken, text = "Multimeedia", bg = "cornflowerblue", relief = "groove",command=lambda:kirjeldus_aknasse("Multimeedia"))
b14.grid(row = 6, column = 2, columnspan = 3, sticky = N+S+W+E)
b15 = Button(aken, text = "Multimeedia", bg = "cornflowerblue", relief = "groove")
b15.grid(row = 5, column = 6, columnspan = 3, sticky = N+S+W+E)
b16 = Button(aken, text = "Programmeerimise alused", bg = "skyblue", relief = "groove",command=lambda:kirjeldus_aknasse("Programmeerimise alused"))
b16.grid(row = 6, column = 6, columnspan = 3, sticky = N+S+W+E)
b17 = Button(aken, text = "Kunstiained", bg = "hotpink", relief = "groove",command=lambda:kirjeldus_aknasse("Kunstiained"))
#Четверг
b17.grid(row = 5, column = 9, columnspan = 2, rowspan = 2, sticky = N+S+W+E)
b18 = Button(aken, text = "Andmebaasisüsteemide alused \n (eesti keeles)", bg = "lightcoral", relief = "groove",command=lambda:kirjeldus_aknasse("Andmebaasisüsteemide alused (eesti keeles)"))
b18.grid(row = 7, column = 2, columnspan = 5, rowspan = 2, sticky = N+S+W+E)
b19 = Button(aken, text = "Ajalugu,\n inimgeo\n graafia \n ja inimese\n õpetus\n eesti keeles", bg = "wheat", relief = "groove")
b19.grid(row = 7, column = 7, rowspan = 2, sticky = N+S+W+E)
b20 = Button(aken, text = "Eesti keel", bg = "orchid", relief = "groove",command=lambda:kirjeldus_aknasse("Eesti keel1"))
b20.grid(row = 7, column = 8, sticky = N+S+W+E)
b21 = Button(aken, text = "Eesti keel", bg = "thistle", relief = "groove",command=lambda:kirjeldus_aknasse("Eesti keel2"))
#Пятница
b21.grid(row = 8, column = 8, sticky = N+S+W+E)
b22 = Button(aken, text = "Keel ja kirjandus", bg = "greenyellow", relief = "groove",command=lambda:kirjeldus_aknasse("Keel ja kirjandus"))
b22.grid(row = 9, column = 3, columnspan = 2, rowspan = 2, sticky = N+S+W+E)
b23 = Button(aken, text = "Matemaatika", bg = "pink", relief = "groove",command=lambda:kirjeldus_aknasse("Matemaatika"))
b23.grid(row = 9, column = 6, columnspan = 2, rowspan = 2, sticky = N+S+W+E)
b24 = Button(aken, text = "Suhtlemine ja \n klienditeenindus", bg = "blueviolet", relief = "groove",command=lambda:kirjeldus_aknasse("Suhtlemine ja klienditeenindus"))
b24.grid(row = 9, column = 8, columnspan = 2, rowspan = 2, sticky = N+S+W+E)
b25 = Button(aken, text = "Ajalugu,\n inimgeo\n graafia \n ja inimese\n õpetus\n eesti keeles", bg = "wheat", relief = "groove",command=lambda:kirjeldus_aknasse("Ajalugu inimgeograafia ja inimese õpetus eesti keeles"))
b25.grid(row = 9, column = 10, rowspan = 2, sticky = N+S+W+E)

tund1=Button(aken,text="Kehaline kasvatus",command=lambda:kirjeldus_aknasse("Kehaline kasvatus"))

aken.mainloop()
