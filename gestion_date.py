dates = []
#gestion sécurité dates bon format grace datetime voir les case |""|

def dates_com():                                                   #prise de conscience des dates
    while True:
        date = input("Donne moi ta date de départ  JJ/MM/AAAAA >>> ")
        dates.append(date)
        date = input("Donne moi ta date de retour JJ/MM/AAAAA >>> ")
        dates.append(date)
        # dates[0] = float(dates[0])
        # dates[1] = float(dates[1])
        # #print(type(dates))
        # if dates[0] == float:
        if dates[1] < dates[0]:            # évitons de bousculer le cours du temps (on ne voyage pas dans le passee)
            print(f"date 1 = {dates[0]}  date 2 = {dates[1]}")
            print("tu ne peux pas revenir avant d'être parti !!! ")
            dates.clear()
        else:
            emp_tps()
            return 0
        # else: exit("code1")

def emp_tps():                                                   #confirmation que ce soit les bonnes dates
    while True:
        validation = input(f"vous partez bien du {dates[0]} au {dates[1]}  o/n >>> ")
        if validation == "o":
            print(f"vos dates du {dates[0]} au {dates[1]}  ont bien ete sélectionées ")
            return validation
        else:
            print("re rentre tes dates")
            dates.clear()
            dates_com()
        return True



if __name__ == "__main__":
    dates_com()

# a = 16/5/2025
# print(type(a))
# a == float