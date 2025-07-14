#Taking the withdrawal amount's input from the user
Amount= int(input("Enter you withdrawal amount: "))

#CAlculating the number of notes of different denominations
note01= Amount//100
note02=(Amount%100)//50
note03= ((Amount%100)%50)//10

print("Notes of 100 rupees:", note01)
print("Notes of 50rupees:", note02)
print("Notes of 10rupees:", note03)