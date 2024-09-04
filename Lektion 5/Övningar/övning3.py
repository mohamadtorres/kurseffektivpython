# Generator f¨or textfiler
# Skriv en generator som l¨aser en stor textfil rad f¨or rad. T¨ank p˚a hur du kan
# anv¨anda generatorer f¨or att spara minne n¨ar du arbetar med stora filer

def read_txt():
    with open ("C:/Users/mrahi/Desktop/Effektivpythonkurs/kurseffektivpython/Lektion 5/Övningar/mamad.txt", "r") as f:
        for line in f:
            yield line

mamad = read_txt()
for rad in mamad:
    print(rad)
