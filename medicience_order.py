print("Welcome to our cozy village pharmacy! We're delighted to have you here.")
print("Please feel free to check up first and enroll in our  medicine services!")
medicine_list = {
     'Cefpodoxime 200 mg' :25,
     'Acetylsalicylic acid (aspirin)': 100,
     'Adrenaline (epinephrine)':75,
     'Albendazole':105,
     'Aluminium hydroxide gel + Magnesium hydroxide (Antacid)':195,
     'Amitriptyline':185,
     'Amlodipine':235,
     'Amoxicillin':134,
     'Ampicillin':321
} 
initial_value = 0                            
print(" 1) Cefpodoxime 200 mg : Rs 25 \n 2) Acetylsalicylic acid (aspirin): Rs 100\n 3) Adrenaline (epinephrine):Rs 75\n 4) Albendazole:Rs 105 \n 5) Aluminium hydroxide gel + Magnesium hydroxide (Antacid)':Rs 195\n 6) Amitriptyline:Rs 185 \n 7) Amlodipine:Rs 235 \n 8) Amoxicillin:Rs 134 \n 9) Ampicillin:Rs 321")
while True:
   
    item = input("Enter the medicine tha you want:")
    if item in medicine_list:
        initial_value = initial_value+ medicine_list[item]
        print(f'your item of medicine is added in your the bill. you can take it right now')
    another_item = input("Do you want another medicine also. (yes or no):")
    if another_item == 'no':
      print("Thank you so much for choosing our pharmacy and trusting us with your healthcare needs. We're grateful for your visit!")
    elif another_item == "yes":
       continue 
    else:
       print("you choosed invalid input. please enter the valid input yes or no")
       continue
    print(f'The total cost of your bill is {initial_value}')
    print("Get well soon")