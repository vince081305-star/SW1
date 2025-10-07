def convert_currency(dollars):
    # Conversion rates (can be updated with real-time API or any other source)
    INR_rate = 83   # 1 USD to INR
    GBP_rate = 0.83 # 1 USD to GBP
    CNY_rate = 7.27 # 1 USD to CNY

    # Conversion calculations
    INR = dollars * INR_rate
    GBP = dollars * GBP_rate
    CNY = dollars * CNY_rate
    
    # Return multiple values
    return INR, GBP, CNY

def display_conversion_table(dollars, INR, GBP, CNY):
    print(f"\nDollar ($)      Indian Rupee (R)    British Pound (Pound)     China (Y)")
    print(f"{dollars:<10}    {INR:<18}   {GBP:<20}   {CNY:<10}")

def main():
    while True:
        # Prompt for user input
        user_input = input("Enter dollar ($) (* to exit): ")
        
        if user_input == '*':
            print("Bye")
            break
        
        try:
            # Convert the input string to a list of dollar values
            dollar_values = list(map(int, user_input.split('@')))
            
            # Display table for each dollar value
            for dollars in dollar_values:
                INR, GBP, CNY = convert_currency(dollars)
                display_conversion_table(dollars, INR, GBP, CNY)
        
        except ValueError:
            print("Invalid input. Please enter numbers separated by '@'.")

if __name__ == "__main__":
    main()
