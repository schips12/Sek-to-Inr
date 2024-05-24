
SEK_TO_INR = 8.50  
def sek_to_inr(sek_amount):
    inr_amount = sek_amount * SEK_TO_INR
    return inr_amount

print("Currency Converter: SEK to INR")
sek_amount = float(input("Enter amount in SEK: "))
inr_amount = sek_to_inr(sek_amount)
print(f"{sek_amount} SEK is equal to {inr_amount} INR")
 
