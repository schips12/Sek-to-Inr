
exchange_rates = {
    'USD': 1.0,   
    'EUR': 0.85,   
    'GBP': 0.75,   
    'INR': 74.0,   
    'JPY': 110.0,  
    'AUD': 1.35,   
    'SEK': 8.5,    
 
}

def convert_currency(amount, from_currency, to_currency, exchange_rates):

    amount_in_usd = amount / exchange_rates[from_currency]     #Convert amount from one currency to another using exchange rates.
    

    converted_amount = amount_in_usd * exchange_rates[to_currency]      # Convert the amount from USD to the target currency
    return converted_amount

def main():
    print("Currency Converter")
    
    from_currency = input("Enter the source currency code : ").upper()
    to_currency = input("Enter the target currency code : ").upper()
    amount = float(input("Enter the amount to convert: "))
    
    converted_amount = convert_currency(amount, from_currency, to_currency, exchange_rates)
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    main()
