import random

import matplotlib.pyplot as plt


names_males_2000 = [
("Filip",25/1000),
("Oscar",24/1000),
("William",24/1000),
("Viktor",23/1000),
("Simon",23/1000),
("Anton",23/1000),
("Erik",23/1000),
("Alexander",21/1000),
("Emil",19/1000),
("Lucas",19/1000),
("Jonathan",19/1000),
("Linus",17/1000),
("Adam",17/1000),
("Marcus",16/1000),
("Jacob",16/1000),
("Albin",15/1000),
("Gustav",15/1000),
("Isak",14/1000),
("Sebastian",14/1000),
("David",14/1000),
("Daniel",13/1000),
("Hugo",13/1000),
("Rasmus",13/1000),
("Carl",13/1000),
("Elias",13/1000),
("Samuel",12/1000),
("Hampus",12/1000),
("Kevin",12/1000),
("Oliver",12/1000),
("Axel",11/1000),
("Johan",11/1000),
("Jesper",10/1000),
("Ludvig",10/1000),
("Felix",10/1000),
("Max",9/1000),
("Robin",9/1000),
("Joel",9/1000),
("Mattias",8/1000),
("Martin",8/1000),
("Andreas",8/1000),
("Pontus",8/1000),
("Christoffer",8/1000),
("Fredrik",7/1000),
("Gabriel",7/1000),
("Edvin",7/1000),
("Tobias",7/1000),
("Casper",6/1000),
("Dennis",6/1000),
("Tim",6/1000),
("Johannes",6/1000),
("Joakim",5/1000),
("Arvid",5/1000),
("Benjamin",5/1000),
("Niklas",5/1000),
("Nils",4/1000),
("Noah",4/1000),
("Elliot",4/1000),
("Hannes",4/1000),
("Alex",4/1000),
("Fabian",4/1000),
("Olle",4/1000),
("Henrik",4/1000),
("Christian",4/1000),
("Leo",4/1000),
("John",4/1000),
("Mikael",4/1000),
("Jonas",4/1000),
("Mohamed",4/1000),
("Rickard",4/1000),
("Josef",4/1000),
("Adrian",3/1000),
("Liam",3/1000),
("Alfred",3/1000),
("André",3/1000),
("Theodor",3/1000),
("Melker",3/1000),
("Wilhelm",3/1000),
("Patrik",2/1000),
("Kalle",2/1000),
("Måns",2/1000),
("August",2/1000),
("Theo",2/1000),
("Kim",2/1000),
("Love",2/1000),
("Melvin",2/1000),
("Petter",2/1000),
("Robert",2/1000),
("Vincent",2/1000),
("Ahmed",2/1000),
("Douglas",2/1000),
("Ali",2/1000),
("Emanuel",2/1000),
("Herman",2/1000),
("Albert",2/1000),
("Eddie",2/1000),
("Leon",2/1000),
("Julius",2/1000),
("Aron",2/1000),
("Thomas",2/1000),
("Jack",2/1000)
]
names_females_2000 = [
("Julia",0.028),
("Emma",0.027),
("Wilma",0.026),
("Hanna",0.023),
("Elin",0.022),
("Linnéa",0.022),
("Amanda",0.020),
("Ida",0.018),
("Matilda",0.018),
("Moa",0.017),
("Maja",0.017),
("Sara",0.017),
("Ebba",0.015),
("Felicia",0.015),
("Emilia",0.014),
("Klara",0.013),
("Josefine",0.013),
("Johanna",0.012),
("Emelie",0.012),
("Linn",0.011),
("Sofia",0.011),
("Frida",0.011),
("Anna",0.011),
("Ellen",0.01),
("Alice",0.01),
("Alva",0.01),
("Isabelle",0.01),
("Olivia",0.01),
("Rebecca",0.01),
("Lisa",0.009),
("Lovisa",0.009),
("Nathalie",0.009),
("Jennifer",0.009),
("Tilda",0.009),
("Kajsa",0.008),
("Fanny",0.007),
("Filippa",0.007),
("Sandra",0.007),
("Alexandra",0.007),
("Saga",0.007),
("Lina",0.006),
("Tilde",0.006),
("Evelina",0.006),
("Agnes",0.006),
("Ella",0.006),
("Victoria",0.006),
("Malin",0.006),
("Elsa",0.006),
("Nora",0.006),
("Isabella",0.005),
("Sanna",0.005),
("Louise",0.005),
("Alma",0.005),
("Emmy",0.005),
("Jenny",0.005),
("Madeleine",0.005),
("Cornelia",0.005),
("Sofie",0.004),
("Nellie",0.004),
("Mikaela",0.004),
("Alicia",0.004),
("Maria",0.004),
("Erika",0.004),
("Tova",0.004),
("Ronja",0.004),
("My",0.004),
("Jasmine",0.004),
("Ellinor",0.004),
("Elvira",0.004),
("Jessica",0.004),
("Stina",0.004),
("Jonna",0.003),
("Caroline",0.003),
("Tove",0.003),
("Nicole",0.003),
("Thea",0.003),
("Elina",0.003),
("Cecilia",0.003),
("Vendela",0.003),
("Annie",0.003),
("Astrid",0.003),
("Gabriella",0.003),
("Molly",0.003),
("Andrea",0.003),
("Carolina",0.003),
("Selma",0.003),
("Linda",0.002),
("Michelle",0.002),
("Tuva",0.002),
("Karin",0.002),
("Cassandra",0.002),
("Therese",0.002),
("Melissa",0.002),
("Daniella",0.002),
("Hilda",0.002),
("Miranda",0.002),
("Vanessa",0.002),
("Angelica",0.002),
("Beatrice",0.002),
("Vera",0.002)
]


gender_type = ["female","male"]

def genNum():
    return random.randint()

class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. I'm a {self.gender}")

    def info(self):
        print(f"{self.name}_{self.gender}")
    
    def __str__(self):
        return f"{self.name}, {self.gender})"


def genMale():
    return genFromList(names_males_2000,"male")

def genFemale():
    return genFromList(names_females_2000,"female")

def genFromList(xs,g):
    values, probabilities = zip(*xs)
    random_value = random.choices(values,probabilities)[0]
    return Person(random_value,g)

def genNPeopleGivenGender(n,g):
    people = []
    if g == "male":
        for i in range(n):
            p = genMale()
            people.append(p)
    else:
        for i in range(n):
            p = genFemale()
            people.append(p)
    return people

def calcDistribution():
    males = genNPeopleGivenGender(46620,"male")
    females = genNPeopleGivenGender(43821,"female")
    maleNames = list(zip(*names_males_2000))[0]
    femaleNames = list(zip(*names_females_2000))[0]
    distributionMales = list(zip(maleNames,100*[0]))
    distributionFemales = list(zip(femaleNames,100*[0]))
    for i in range(len(males)):
        updateDist(males[i].name, distributionMales)
    for i in range(len(females)):
        updateDist(females[i].name, distributionFemales)
    return (distributionMales,males,distributionFemales,females)


def updateDist(name1, distList):
    for i in range(len(distList)):
        name2, dist = distList[i]
        if name1 == name2:
            distList[i] = (name2, dist+1)

def calcSampleDist(sampleMales, sampleFemales):
    maleNames = list(zip(*names_males_2000))[0]
    femaleNames = list(zip(*names_females_2000))[0]
    distMales = list(zip(maleNames,100*[0]))
    distFemales = list(zip(femaleNames,100*[0]))
    for i in range(len(sampleMales)):
        updateDist(sampleMales[i].name, distMales)
    for i in range(len(sampleFemales)):
        updateDist(sampleFemales[i].name, distFemales)
    return(distMales, distFemales)



distMales, males, distFemales, females = calcDistribution()
print("Total number of people generated: ", (len(males) + len(females)))
print("Number of males generated: ", len(males))
#print("Males:\n", list(zip(*distMales))[1])
print("Males:\n", list(distMales))
print("Number of females generated: ", len(females))
#print("Females:\n", list(zip(*distFemales))[1])
print("Females:\n", list(distFemales))
print("_________________________________________________________")
sampleMales = random.sample(males, 178)
sampleFemales = random.sample(females, 168)
(distSampleMales, distSampleFemales) = calcSampleDist(sampleMales, sampleFemales)
print("Total sampleSize: ", len(sampleMales) + len(sampleFemales))
print("Number of males sampled: ", len(sampleMales))
#print("SampleMales:\n", list(zip(*distSampleMales))[1])
print("SampleMales:\n", list(distSampleMales))
print("Number of females sampled: ", len(sampleFemales))
#print("SampleFemales:\n", list(zip(*distSampleFemales))[1])
print("SampleFemales:\n", list(distSampleFemales))


labels = [x[0] for x in names_males_2000]
values = list(zip(*distSampleMales))[1]

plt.bar(labels, values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart Example')
plt.xticks(rotation=-85)

plt.show()