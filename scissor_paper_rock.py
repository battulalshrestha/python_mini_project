import random 
user = input("Enter the 'rock' 'paper' or 'scissor': ")
computer = ['rock','scissor','paper']
c_user = random.choice(computer)
print(f"your choice {user} and computer chose {c_user}")
if (user == c_user):
  print('draw')
elif (user == "paper"and c_user== "rock"):
  print("user won!!")
elif (user == "scissor" and c_user == "paper"):
  print("user won ")
elif (user == "rock" and c_user == "scissor"):
   print("user won")
else:
  print("computer win")