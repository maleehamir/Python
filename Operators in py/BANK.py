Amount =int(input("Enter the Amount for Withdrawl:"))
note_1 =Amount//100
note_2 =(Amount%100)//50
note_3 =((Amount%100)%50)//10
print("notes of 100 ruppees:", note_1)
print("notes of 50 rupees:", note_2)
print("notes of 10 rupees:", note_3)
