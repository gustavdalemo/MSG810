import random

gender = ["female","male"]

names_boys_1998 = [
"Filip",
"Erik",
"Oscar",
"Simon",
"Anton",
"Alexander",
"Viktor",
"Jonathan",
"Marcus",
"Jacob",
"William",
"Emil",
"Daniel",
"Lukas",
"Linus",
"David",
"Jesper",
"Gustav",
"Johan",
"Albin",
"Carl",
"Sebastian",
"Adam",
"Rasmus",
"Andreas",
"Oliver",
"Axel",
"Kevin",
"Isak",
"Martin",
"Felix",
"Samuel",
"Robin",
"Tobias",
"Pontus",
"Christoffer",
"Mattias",
"Ludvig",
"Fredrik",
"Hampus",
"Joel",
"Elias",
"Niklas",
"Max",
"Joakim",
"Jonas",
"Dennis",
"Johannes",
"Hugo",
"Gabriel",
"Tim",
"Henrik",
"Edvin",
"Casper",
"Mikael",
"Alex",
"Arvid",
"John",
"Benjamin",
"Christian",
"Rickard",
"André",
"Olle",
"Patrik",
"Adrian",
"Mohammed",
"Nils",
"Fabian",
"Hannes",
"Theodor",
"Alfred",
"Josef",
"Kim",
"Leo",
"Wilhelm",
"Måns",
"Robert",
"Jimmy",
"Ali",
"Petter",
"Tom",
"Thomas",
"August",
"Olof",
"Love",
"Eddie",
"Vincent",
"Kalle",
"Ahmed",
"Magnus",
"Jens",
"Elliot",
"Noah",
"Per",
"Jack",
"Anders",
"Björn",
"Douglas",
"Emanuel",
"Julius"]
names_girls_1998 = [
"Emma"
,"Julia"
,"Elin"
,"Amanda"
,"Hanna"
,"Linnéa"
,"Matilda"
,"Wilma"
,"Moa"
,"Ida"
,"Johanna"
,"Sara"
,"Felicia"
,"Emelie"
,"Josefine"
,"Frida"
,"Sofia"
,"Ebba"
,"Rebecka"
,"Anna"
,"Klara"
,"Maja"
,"Lovisa"
,"Nathalie"
,"Malin"
,"Sandra"
,"Fanny"
,"Alice"
,"Isabelle"
,"Lisa"
,"Ellen"
,"Olivia"
,"Linn"
,"Jennifer"
,"Mikaela"
,"Victoria"
,"Louise"
,"Evelina"
,"Lina"
,"Emilia"
,"Alexandra"
,"Alva"
,"Kajsa"
,"Madeleine"
,"Jenny"
,"Sofie"
,"Sanna"
,"Caroline"
,"Filippa"
,"Alicia"
,"Maria"
,"Isabella"
,"Erika"
,"Elsa"
,"Agnes"
,"Nellie"
,"Jessica"
,"Linda"
,"Ella"
,"Cornelia"
,"Emmy"
,"Carolina"
,"Stina"
,"Therese"
,"Saga"
,"Nora"
,"Tilda"
,"Jasmine"
,"Ellinor"
,"Ronja"
,"Annie"
,"Cecilia"
,"Jonna"
,"Alma"
,"Gabriella"
,"Michelle"
,"Nicole"
,"Elvira"
,"Tove"
,"My"
,"Angelica"
,"Vendela"
,"Andrea"
,"Daniella"
,"Elina"
,"Karin"
,"Kristina"
,"Astrid"
,"Cassandra"
,"Tova"
,"Molly"
,"Sabina"
,"Beatrice"
,"Denise"
,"Patricia"
,"Paulina"
,"Miranda"
,"Thea"
,"Nina"
,"Melissa"
,"Emily"
]

def genNum():
    return random.randint

class Person:
    def __init__(self, name, gender, birthYear):
        self.name = name
        self.gender = gender
        self.birthYear = birthYear
    
    def introduce(self):
        print(f"Hello, my name is {self.name}. I'm a {self.gender} and I was born in {self.birthYear}")

    def info(self):
        print(f"{self.name}_{self.gender}_{self.birthYear}")
person1 = Person("Alice","Girl",1998)

def genPerson():
    birthYear = random.randint(1998,2021)
    index = random.randint(0,100)
    g = gender[random.randint(0,1)]
    if g=="Male":
        return Person(names_boys_1998[index],g,1998)
    else:
        return Person(names_girls_1998[index],g,1998)

for i in range(20):
    genPerson().info()