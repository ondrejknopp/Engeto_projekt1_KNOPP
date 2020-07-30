'''
author = Ondřej Knopp
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
oddelovac = ("\n" +70*("-") + "\n")
users = {"bob": "123", "ann": "pass123", "mike": "password123", "lizz": "pass123"}
print("Dobrý den! Pro vatup do programu zadejte prosím uživatelské jméno a heslo:\n")
user = input("Uživatelské jméno:\n")
password = input("Heslo:\n")
if (user, password) in users.items():
    print("Uživatel úspěšně přihlášen! Nyní si vyberte k analýze text 1, 2 nebo 3..\n")
    cislo_textu = int(input("Volba textu: "))
    chosen_text = TEXTS[(cislo_textu)-1]
    chosen_text_split = chosen_text.split()
    clean_text = []

    while chosen_text_split:
        slovo = chosen_text_split.pop()
        slovo = slovo.strip('.,:/;')
        if slovo: clean_text.append(slovo)

    pocet_slov = len(clean_text)
    title_words = 0
    upper_words = 0
    lower_words = 0
    numeric_words = 0
    soucet_cisel = 0
    for i in range(pocet_slov):
        if (clean_text[i]).istitle() == True:
            title_words += 1
        elif (clean_text[i]).isupper() == True:
            upper_words += 1
        elif (clean_text[i]).islower() == True:
            lower_words += 1
        elif (clean_text[i]).isnumeric() == True:
            numeric_words += 1
            soucet_cisel = soucet_cisel + float(clean_text[i])
        else:
            continue
    
    print("\nV textu je ", pocet_slov, "slov. Z toho:\n", title_words, "slov, začínajících velkým písmenem,\n", upper_words, "slov, psaných pouze velkými písmeneny,\n",
    lower_words, "slov, psaných pouze malými písmeneny,\n", lower_words, "slov, psaných pouze malými písmeneny a", numeric_words, "čísel.",oddelovac, 
    "Po sečtení všech čísel v textu dostaneme hodnotu ", soucet_cisel, ".", oddelovac)   

    sloup_graf = {}
    for vyskyt in clean_text:
        if len(vyskyt) in sloup_graf.keys():
           sloup_graf[len(vyskyt)] += 1
        else:
            sloup_graf[len(vyskyt)] = 1

    for klic in sorted(sloup_graf.keys()):
        print(klic,"*"*sloup_graf[klic], str(sloup_graf[klic]))
else:
    print("Bohužel, Vámi zadaná kombinace uživatelského jména a hesla nebyla v naší databázi nalezena, zkuste to prosím znovu..")
    
