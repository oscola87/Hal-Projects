import random
class Character:
    def __init__(self, name ,point ,good):
        self.name = name
        self.point = point
        self.good = "good"

    def __str__(self):
        return "{} and is {}".format()
        self.good,
        "good" if self.good else "bad"

characters = {
    "Elsa": Character("Elsa", 4, "good"),
    "Andy": Character("Andy", 8, "good"),
    "Simba": Character("Simba", 3, "good"),
    "Aladin": Character("Aladin", 7, "good"),
    "Aladin": Character("Aladin", 7, "good"),
    "Judy Hopps": Character("Judy Hopps" ,1, "good"),
    "Andy": Character("Andy" ,8, "good"),
    "Nemo": Character("Nemo" ,9, "good"),
    "Sully": Character("Sully" ,3, "good"),
    "Mr Incredible": Character("Mr Incredible" ,6, "good"),
    "Lightnng McQueen": Character("Lightnng McQueen" ,8, "good"),
    "Steve Rodgers": Character("Steve Rodgers" ,5, "good"),
    "Tony Stark": Character("Tony Stark" ,5, "good"),
    "Wade Willlson": Character("Wade Willlson" ,3, "good"),
    "Thor": Character("Thor" ,7, "good"),
    "Peter Parker": Character("Peter Parker" ,6, "good"),
    "The Monsters Snowman": Character("The Monsters Snowman" ,5, "bad"),
    "Scar": Character("Scar" ,3, "bad"),
    "Jafar": Character("Jafar" ,5, "bad"),
    "Assistent Mayor bellware": Character("Assistent Mayor bellware" ,5, "bad"),
    "Lotso Bear": Character("Lotso Bear" ,6, "bad"),
    "Darla": Character("Darla" ,1, "bad"),
    "Randal": Character("Randal" ,9, "bad"),
    "Buddy": Character("Buddy" ,3, "bad"),
    "Loki": Character("Loki" ,6, "bad"),
    "Fransis": Character("Fransis" ,5, "bad"),
    "The Frost Giants": Character("The Frost Giants" ,9, "bad"),
}
print ("\n---------------------------------\n")
x = input("Welcome the story generator. To generate a story type normal or random. if you would like two charcters to fight, print fight" "\n\n" "Answer: ")

if x == "normal":
    print ("\n")
    theme=random.choice(["Disney","Pixar","Marvel"])
    if theme == "Disney" :
      story=random.choice(["frozen","lion king","Aladdn","Beauty and the Beast","Zootopia"])
      if story == "frozen" :
        protagonist=random.choice(["Anna","Elsa","Christof"])
        antagonist=random.choice(["Hans","The Snowman"])
      if story == "lion king" :
        protagonist=random.choice(["Simba","Timone","Pumbaa"])
        antagonist=random.choice(["Scar","The vultures"])
      if story == "Aladdn" :
        protagonist=random.choice(["Jasmine","Carpet","Genie"])
        antagonist=random.choice(["Jafar"])
      if story == "Beauty and the Beast" :
        protagonist=random.choice(["Bell","The beast","Chip"])
        antagonist=random.choice(["The Towns people"])
      if story == "Zootopia" :
        protagonist=random.choice(["Judy Hopps","Nick wilde"])
        antagonist=random.choice(["Assistent Mayor bellware"])
    if theme == "Pixar" :
      story=random.choice(["Toy story","Finding Nemo","Monsters Inc","The Incredibles","Cars"])
      if story == "Toy story" :
        protagonist=random.choice(["Woddy","Buzz","Mr. Potato Head"])
        antagonist=random.choice(["Lotso Bear"])
      if story == "Finding Nemo" :
        protagonist=random.choice(["Nemo","Marlen","Dory"])
        antagonist=random.choice([" Darla"])
      if story == "Monsters Inc" :
        protagonist=random.choice(["Sully","Mike","Boo"])
        antagonist=random.choice(["Randal"])
      if story == "The Incredibles" :
        protagonist=random.choice(["Mr. Incredible","Elasta Women","Violet"])
        antagonist=random.choice(["Buddy"])
      if story == "Cars" :
        protagonist=random.choice(["Lightning McQueen","Mator"])
        antagonist=random.choice(["Chick Hicks"])
    if theme == "Marvel" :
      story=random.choice(["Captian America","Iron Man","Thor","Deadpool","Spiderman"])
      if story == "Captian America" :
        protagonist=random.choice(["Steve Rogers","Bucky","Peggy Carter"])
        antagonist=random.choice(["Nazis"])
      if story == "Iron Man" :
        protagonist=random.choice(["Tony Stark","Pepper Pots","Rody"])
        antagonist=random.choice(["The iron Monger"])
      if story == "Thor" :
        protagonist=random.choice(["Thor","Odin","Jane Foster"])
        antagonist=random.choice(["Loki","The Frost Giants"])
      if story == "Deadpool" :
        protagonist=random.choice(["Wade Willlson","Negasonic Teenage Warhead","Angle Dust"])
        antagonist=random.choice(["Ajax","Fransis"])
      if story == "Spiderman" :
        protagonist=random.choice(["Aunt May","Peter"])
        antagonist=random.choice(["Aron"])

    conflict=random.choice([" fought against "," attempted to stop "," defended against "," explored with "," tried to evade "," competed with "," sought revenge against "])
    end=random.choice(["It did not end well.","It went very well.","They died tragically.","It ended sadly.","It was glorious.","There was a twist."])

    print("In the " + theme + " Universe and the Story of " + story + ", there was once a character named " + protagonist + " who"+ conflict + antagonist + ". " + end + " The End")

elif x == "random":
    print ("\n")
    theme=random.choice(["Disney","Pixar","Marvel"])
    story=random.choice(["Captian America","Iron Man","Thor","Deadpool","Spiderman","Toy story","Finding Nemo","Monsters Inc","The Incredibles","Cars","frozen","lion king","Aladdn","Beauty and the Beast","Zootopia"])
    protagonist=random.choice(["Elsa","Simba","Aladdn","Bell","Judy Hopps","Andy","Nemo","Sully","Mr.Incredible","Lightning McQueen","Steve Rogers","Tony Stark","Thor","Wade Willlson","Peter Parker"])
    antagonist=random.choice(["The Monsters Snowman from frozen","Scar from lion king","Jafar from Aladdn","Assistent Mayor bellware from Zootopia","Lotso Bear from toy story","Darla from finding Nemo","Randal from Monsters Inc","Buddy from the Incredible","Loki from Asgard","The Frost Giants from Asgard","Fransis from Deadpool"])
    conflict=random.choice([" fighting against "," attempting to stop "," defending against "," exploring with "," trying to evade "," competing with "])
    end=random.choice(["This will not end well.","This will end very well.","This will end sadly.","This will end glorious.","This is a twist."])
    tragedy=random.choice(["There was a story tornado mixing all storylines! Now we are in the "])
    print("OH NO! " + tragedy + theme + " Universe and the Story of " + story + ", The character named " + protagonist + " is"+ conflict + antagonist + ". " + end + " The End")

elif x == "fight":
    print("You are now in fight mode. In this you will be able to battle diffrent charcters. Pick a protaginist from the list below\n")
    x = input("\n".join(["Elsa","Simba","Aladdn","Judy Hopps","Andy","Nemo","Sully","Mr.Incredible","Lightning McQueen","Steve Rogers","Tony Stark","Thor","Wade Willlson","Peter Parker\n","Answer: "]))
    first_character = characters[x]
    print ("\n---------------------------------\n")
    print("Now choose an antagonist:")
    y = input("\n".join(["\nThe Monsters Snowman","Scar","Jafar","Assistent Mayor bellware","Lotso Bear","Darla","Randal","Buddy","Loki","The Frost Giants","Fransis from Deadpool\n","Answer:"]))
    for key, value in characters.items():
        if value.good is False:
            print("{}: {}".format(key, value))

    second_character = characters[y]
    winner = first_character if first_character.point > second_character.point else second_character
    loser = first_character if first_character.point < second_character.point else second_character
    adj = random.choice(["valent","horiffic"])
    fight = random.choice(["Unicorn Swords","paper bags","bands"])

    print("\n In the " + adj + " battle of the " + fight + " {winners_name} " "vanquished" " {loser_name} ".format(
    winners_name=winner.name,
    loser_name=loser.name

    ))

else:
    print("\n\n")
    print("Thats not how you spell random, normal or fight dummy")

print ("\n")
