alter = int(input("Wie alt bist du?: "))

if alter >= 18:
    print("Du bist volljährig")
elif alter < 18:
    print("Du bist noch nicht volljährig")
else:
    print("Bitte gib eine Zahl ein")


fach = input("Was ist dein Leistungsfach?: ")

match fach:
    case "Mathe":
        print("Du hast Mathe gewählt")
    case "Deutsch":
        print("Du hast Deutsch gewählt")
    case _:
        print("Dieses Fach gibt es als Leistungsfach nicht an unserer Schule")


