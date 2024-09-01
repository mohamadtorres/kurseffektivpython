# Decorator f¨or att s¨akra funktioner med l¨osenord
# Skapa en decorator som endast till˚ater att en funktion k¨ors om r¨att l¨osenord ges som argumen

def password(password):
    def decorator(func):
        def wrapper():
            user_password = input("Enter password:")
            if user_password == password:
                return func()
            else:
                print("fel password")
        return wrapper
    return decorator

@password("Mamad")
def view_secret():
    print("Mamad Khavari dele mano bordi")

view_secret()