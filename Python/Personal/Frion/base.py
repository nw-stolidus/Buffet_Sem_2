import random

#Variables
questions = ["What is your favorite thing today?", "what is the worst thing that happened today?", "Who is your fav person you've seen today?","What is your favorite food?"]
answer = random.randrange(0,3)
Response = ["Nice, that's cool!", "I hope I can help brighten your day!", "Oh, that person is fun, you're my favorite that I've met today!","Ooh, that sounds good, I think I need to try it."]


print("Hi there, what's your name?")
name = str(input())

print("It's nice to meet you, "+name)

print(questions[answer])
intake = str(input())
print(Response[answer])


print(" ")
print("Ope, I'm outta time, so I gotta go sadly, but I'll talk to you later. Bye!")



