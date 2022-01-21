from tkinter import*
root=Tk()
root.title("")
root.geometry("1500x1000+100+100")
root.resizable(width=False, height=False)
def riik(d:dict, v:int):
    keys_list=(list(d.keys()))
    values_list=(list(d.values()))
    if v=="1":
        mas=[]
        capital=(input("Sisestage pealinn: ")).capitalize()
        capital.title()
        for i in values_list:
            if i==capital:
                for i in range(len(values_list)):
                    if values_list[i]==capital:
                        mas.append(int(i))
                        print("riik -", keys_list[i],"<-->", "peallin -", values_list[i])
    else:
        riik=(input("Sisestage  riik: ")).capitalize()
        a=d.get(riik)
        print("riik -", riik ,"<-->", " -", a)
    return

def new_key_value(d:dict):
    new={}
    riik=(input("Sisestage riik: ")).capitalize()
    capital=(input("Sisestage peallin: ")).capitalize()
    new={riik:capital}

    return d,new    

root.mainloop()