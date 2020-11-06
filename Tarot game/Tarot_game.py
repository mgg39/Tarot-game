
import random

print(" Welcome into my tarot game. It will give randomly present you with three cards representing your past, present and future. \n Write 'Ready' whenever you are ready to start")
game = input()

#tarot cards list
tarot_cards = ("The Magician","The High Priestess","The Empress","The Emperor","The Hierophant","The Lovers","The Chariot","Strength","The Hermit","Wheel of Fortune", "Justice","The Hanged Man","Death","Temperance","The Devil","The Tower","The Star","The Moon", "The Sun", "Judgement","The World","The Fool")

#spead of cards
spread = {}
if game == "Ready":
 spread["past"] = random.choice(tarot_cards)
 spread["present"] = random.choice(tarot_cards)
 spread["future"] = random.choice(tarot_cards)

#obtained card
for key, value in spread.items():
  print("Your " +key+ " is the " +value+ " card. ")