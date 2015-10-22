#Program that simulates a snarky Magic 8 Ball

#Import statements
import random

#Declarations
phrases = ["As I see it, yes", "It is certain", "Most likely", "Outlook good", "Without a doubt", "Yes - definitely", "You may rely on it", "Reply hazy, try again",
"Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no",
"Outlook not so good", "Very doubtful", "Do I Look Like I Care?", "Yeah, Right", "Ask Again Later", "DUH!"]
inputValue = ""

#Greeting statements
print("Greetings! I am the magic 8 ball!")
print("Please ask me a Yes or No question! Or say 'Farewell' to leave forever!!!!\n\n")

#Main loop - Sentinel value is a case insensitive 'farewell'
while(inputValue.lower() != "farewell"):
    inputValue = input("Your decision?: ")
    if(inputValue.lower() == "farewell"):
        print("Fare thee well!")
    else:
        print(phrases[random.randint(0, 20)], "\n\n")