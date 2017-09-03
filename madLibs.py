"""This program will create a fun mad lib for you!"""

print "Mad libs has started, let's create a fun story!"

name = raw_input("What name do you want your character to have? ")
first_adj = raw_input("Enter an adjective: ")
second_adj = raw_input("Enter a second adjective: ")
third_adj = raw_input("Enter one more adjective: ")
first_verb = raw_input("Enter a verb: ")
second_verb = raw_input("Enter a second verb: ")
third_verb = raw_input("Enter one more verb: ")
first_noun = raw_input("Enter a noun: ")
second_noun = raw_input("Enter a second noun: ")
third_noun = raw_input("Enter a third noun: ")
fourth_noun = raw_input("Enter a fourth noun: ")
animal = raw_input("Enter an animal: ")
food = raw_input("Enter a food you like: ")
fruit = raw_input("Enter a fruit you like: ")
number = raw_input("Enter a number: ")
superhero = raw_input("Enter a Super Hero Name: ")
country = raw_input("Enter a country name: ")
dessert = raw_input("Enter a dessert you like: ")
year = raw_input("Enter a year: ")





#The template for the story
STORY = "\n\nThis morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rhythm of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world.\n\n" 

print STORY % (first_adj, name, first_verb, second_adj, first_noun, second_noun, animal, food, second_verb, third_noun, fruit, third_adj, name, third_verb, number, name, superhero, superhero, name, country, name, dessert, name, year, fourth_noun)