import random

choices=["scissors","paper","stone"]
user_choice=input("Enter the choices, scissors or paper or stone  ")


computer_choice=random.choice(choices)
print(computer_choice)

if(user_choice==computer_choice):
    print("Its a draw")
elif(user_choice=="scissors" and computer_choice=="paper"):
    print("Congrats! YOU WIN")  
elif(user_choice=="stone" and computer_choice=="scissors"):
    print("Congrats! YOU WIN") 
elif(user_choice=="paper" and computer_choice=="stone"):
    print("Congrats! YOU WIN") 
else:
    print("COMPUTER WIN")             
