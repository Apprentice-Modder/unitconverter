# Available conversion_factors
conversion_factors = {
    "mph_to_kmph": 1.60943,
    "feet_to_meters": 0.3048,
    "inches_to_centimeters": 2.54,
    "feet_to_inches": 12,
    "yard_to_feet": 3,
    "mile_to_feet": 5280,
    "meter_to_centimeters": 100,
}

def convert_units(value, source_unit, target_unit, conversion_factor):
    converted_value = value * conversion_factor
    return converted_value, source_unit, target_unit

def main():
    while True:
        try:
            # Display all converion factors for the user
            print("\nAvailable conversion options:")
            for conversion_key in conversion_factors.keys():
                print(conversion_key)

            
            print("Enter the source unit (e.g., 'mph, 'feet', 'mile'): ")
            source_unit = input()
            

            # Prompt the user to enter the numerical value
            value = float(input("\nEnter the numerical value of source unit to convert: "))

            # Prompt the user to enter the conversion they want
            
            target_unit = input("\nEnter your designated unit: ")

            conversion_key = f"{source_unit}_to_{target_unit}"
            if conversion_key in conversion_factors:
                conversion_factor = conversion_factors[conversion_key]
                converted_value, _, _ = convert_units(value, source_unit, target_unit, conversion_factor)
                print(f"{value:.2f} {source_unit} is equal to {converted_value: .2f} {target_unit}.")
            else:
                print("This conversion has not been implemented yet. Doo-doo head.")
        except ValueError:
            print("Invalid input. Put numbers, not letters.")

        again = input("\nDo you want to perform another conversion? (y/n): ")
        if again.lower() != "y":
            break # Break the loop if the user enters anything other than "y"





if __name__ == "__main__":
    main()