#Marks input

print("Enter the marks obtained in the Subjects")
maths= int(input("Enter marks obtained in Mathematics: "))
english= int(input("Enter marks obtained in English: "))
urdu= int(input("Enter marks obtained in Urdu: "))
science= int(input("Enter marks obtained in Science: "))

sum= maths+ english+ urdu+ science

percentage= (sum/400)*100
print("You achieved", percentage, "%")