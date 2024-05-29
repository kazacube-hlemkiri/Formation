
def Bonjour(login):
    utilisateurs = {
        "Houda@kazacube.com": "Houda",
        "Ahmed@kazacube.com": "Ahmed",
        "Rania@kazacube.com": "Rania",
        "Meftah@kazacube.com": "Meftah",
        "Marwa@kazacube.com": "Marwa",
        "Hanna@kazacube.com": "Hanna",

    }

    if login in utilisateurs:
        nom = utilisateurs[login]
        print(f"Bonjour {nom}")
    else:
        print("Login non reconnu")


login_entre = input("Veuillez entrer votre login: ")
Bonjour(login_entre)
print("Premier developpement")
print("Test anas")
print("i'm not really bored, I'm more of frustrated")
print("it'll get better")

print("hanaa dev")

for i in range(10):
    print("thank you teacher Houda ")
