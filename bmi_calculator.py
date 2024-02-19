from user_preferences import get_valid_age
from user_preferences import get_valid_name
from user_preferences import get_valid_surname
from user_preferences import feet_to_meters
from user_preferences import stones_to_kilos
from user_preferences import pounds_to_kilos
from user_preferences import inches_to_meters
from user_preferences import calculate_bmi
from user_preferences import get_valid_email
from user_preferences import get_valid_address
import time  # Used to create a 5 seconds delay to return final BMI results.

print('Welcome to BMI Calculator')

print('\nUse this service to:')
print('- Check the BMI of an adult aged 18 and over')
print('- Get information about what to do next')

print('\nYou should not use this tool to diagnose any symptoms. '
      'If you are worried about your weight, contact your local pharmacist or GP surgery.')
print('\nWho should not use this tool if:')
print('- You are under 18 years old')
print('- Are pregnant')
print('- Have been diagnosed with an eating disorder, or think you may have one')
print('- Have a condition that affects your height')
print('For more info, visit https://www.nhs.uk/ ')
print()
fileobject = open("bmi_user.csv", "a")
name = get_valid_name()
surname = get_valid_surname()
age = get_valid_age()
email = get_valid_email()
address = get_valid_address()
print('\nPlease confirm the below is correct')

while True:
    reg_confirmation = input(f'{name} {surname}, {age} years old\nE-mail: {email} \nAddress: {address}\n(Y/N): ')

    if reg_confirmation.capitalize() == 'Y':
        print(f'\nThanks for confirming your details {name} {surname}')
        break
    elif reg_confirmation.capitalize() == 'N':
        print('\nPlease, re-enter details')
        name = get_valid_name()
        surname = get_valid_surname()
        age = get_valid_age()
        email = get_valid_email()
        address = get_valid_address()

        print('Please confirm the below is correct')
    else:
        print('Invalid input. Please enter Y or N.')

while True:
    print('\nPREFERENCES')
    print('\nHow would you like to insert units:')
    print('*  Units Settings')
    print('1. Stones/Feet')
    print('2. Pounds/Inches')
    print('3. Kilos/Meters')

    preferences = input('Enter 1, 2 or 3 (insert "exit" to quit): ')

    if preferences.lower() == 'exit':
        print("Exiting application. Goodbye!")
        exit()
    elif preferences == '1':
        print('\nYou selected 1.Stones/Feet')

    elif preferences == '2':
        print('\nYou selected 2.Pounds/Inches')

    elif preferences == '3':
        print('\nYou selected 3.Kilos/Meters')

    preferences_confirmation = input('Confirm your selection (Y/N): ')
    if preferences_confirmation.upper() == 'Y':
        break
    else:
        print('\nInvalid input. Please enter 1, 2, 3 or "exit".')

print()

if preferences == '1':
    stk = stones_to_kilos()
    print(f'({stk:.2f} in Kilos)')
    ftm = feet_to_meters()
    print(f'({ftm:.2f} in Meters)')
    bmi = calculate_bmi(stk, ftm)
    print()
    print("Calculating BMI...")
    time.sleep(5)
    if 0 < bmi < 18.5:
        print(f'\nYour BMI is {bmi:.1f}, you are Underweight')
        print('For more info about BMI, visit https://www.nhs.uk/ ')
    elif 18.5 <= bmi <= 24.9:
        print(f'\nYour BMI is {bmi:.1f}, you are on Normal (Healthy weight)')
    elif 25 <= bmi < 29.9:
        print(f'\nYour BMI is {bmi:.1f}, you are Overweight')
        print('For more info about BMI, visit https://www.nhs.uk/ ')
    else:
        print(f'\nYour BMI is {bmi:.1f}, you are Obese')
        print('For more info about BMI, visit https://www.nhs.uk/ ')
    pass
elif preferences == '2':
    ptk = pounds_to_kilos()
    print(f'({ptk:.2f} in Kilos)')
    itm = inches_to_meters()
    print(f'({itm:.2f} in Meters)')
    bmi = calculate_bmi(ptk, itm)
    print()
    print("Calculating BMI...")
    time.sleep(5)
    if 0 < bmi < 18.5:
        print(f'\nYour BMI is {bmi:.1f}, you are Underweight')
        print('For more info about BMI, visit https://www.nhs.uk/ ')
    elif 18.5 <= bmi <= 24.9:
        print(f'\nYour BMI is {bmi:.1f}, you are on Normal (Healthy weight)')
    elif 25 <= bmi < 29.9:
        print(f'\nYour BMI is {bmi:.1f}, you are Overweight')
        print('For more info about BMI, visit https://www.nhs.uk/ ')
    else:
        print(f'\nYour BMI is {bmi:.1f}, you are Obese')
        print('For more info about BMI, visit https://www.nhs.uk/ ')
    pass

else:
    kg = input("Enter your weight in Kilos: ")
    kg = kg.replace(',', '.').replace(' ', '.')
    kg = float(kg)
    print(f'{kg / 6.35029:.2f} in Stones and {kg * 2.2:.2f} in Pounds.')
    mt = input("Enter your height in Meters: ")
    mt = mt.replace(',', '.').replace(' ', '.')
    mt = float(mt)
    print(f'{mt * 3.28:.2f} in Feet and {mt * 39.37:.2f} in Inches.')
    bmi = calculate_bmi(kg, mt)
    print()
    print("Calculating BMI...")
    time.sleep(5)
    if 0 < bmi < 18.5:
        print(f'\nYour BMI is {bmi:.1f}, you are Underweight')
        print('For more info about BMI, visit https://www.nhs.uk/ ')
    elif 18.5 <= bmi <= 24.9:
        print(f'\nYour BMI is {bmi:.1f}, you are on Normal (Healthy weight)')
    elif 25 <= bmi < 29.9:
        print(f'\nYour BMI is {bmi:.1f}, you are Overweight')
        print('For more info about BMI, visit https://www.nhs.uk/ ')
    else:
        print(f'\nYour BMI is {bmi:.1f}, you are Obese')
        print('For more info about BMI, visit https://www.nhs.uk/ ')
    pass

fileobject.write(f'\n{name}, {surname}, {age}, {email}, {preferences}, {bmi:.2f}, {address}')

fileobject.close()
