import re  # Used to control email and postcode parameters (Got both on google.com)


def get_valid_name():
    """Parameters for a valid name input"""
    while True:
        name = input("Enter your name: ").capitalize()
        if name.isalpha():
            return name
        else:
            print("Invalid input. Please enter a valid name without numbers or special characters.")


def get_valid_surname():
    """Parameters for a valid surname input"""
    while True:
        surname = input("Enter your Surname: ").capitalize()
        if surname.isalpha():
            return surname
        else:
            print("Invalid input. Please enter a valid surname without numbers or special characters.")


# age
def get_valid_age():
    """Parameters for a valid age input"""
    while True:
        age_input = input("Enter your age: ")
        try:
            age = int(age_input)
            if age >= 18:
                return age
            else:
                print(
                    "You must be at least 18 years old to use this service. \nIf you or your child are aged between 2 "
                    "and 17, visit https://www.nhs.uk/ for guidance.")
                exit()
        except ValueError:
            print("Invalid input. Please enter a valid number for age.")


def get_valid_email():
    """Parameters for a valid email input"""
    while True:
        email = input("Enter your email address: ").lower()

        email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')  # found on Google

        if email_pattern.match(email):
            return email
        else:
            print("Invalid input. Please enter a valid email address.")


def get_valid_address():
    """Parameters for a valid address input"""
    while True:
        postcode = input("Enter your postcode (with space): ").strip().upper()

        postcode_pattern = re.compile(r'^[A-Z]{1,2}[0-9R][0-9A-Z]? [0-9][ABD-HJLNP-UW-Z]{2}$')  # found on Google

        if postcode_pattern.match(postcode):
            return postcode
        else:
            print("Invalid input. Please enter a valid address with a valid postal code.")


def pounds_to_kilos():
    """Parameters for a valid pounds input and conversion to kilos"""
    while True:
        input_pounds = input("Enter your weight in pounds: ")
        input_pounds = input_pounds.replace(',', '.').replace(' ', '.')
        input_pounds = float(input_pounds)
        try:
            ptk = input_pounds / 2.20462
            return ptk
        except ZeroDivisionError:
            print("Error: Weight should be greater than zero.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


def stones_to_kilos():
    """Parameters for a valid stones input and conversion to kilos"""
    while True:
        input_stones = input("Enter your weight in stones: ")
        input_stones = input_stones.replace(',', '.').replace(' ', '.')
        input_stones = float(input_stones)
        try:
            stk = input_stones * 6.35029
            return stk
        except input_stones == 0:
            print("Error: Weight should be greater than zero.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


def inches_to_meters():
    """Parameters for a valid inches input and conversion to metres"""
    while True:
        input_inches = input("Enter your height in inches: ")
        input_inches = input_inches.replace(',', '.').replace(' ', '.')
        input_inches = float(input_inches)
        try:
            itm = input_inches * 0.0254
            return itm
        except input_inches <= 0:
            print("Error: Height should be greater than zero.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


def feet_to_meters():
    """Parameters for a valid feet input and conversion to metres"""
    while True:
        input_feet = input("Enter your height in feet: ")
        input_feet = input_feet.replace(',', '.').replace(' ', '.')
        input_feet = float(input_feet)
        try:
            ftm = input_feet * 0.3048
            return ftm
        except input_feet == 0:
            print("Error: Height should be greater than zero.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


def calculate_bmi(weight, height):
    """Function to calculate BMI"""
    try:
        bmi = weight / (height ** 2)
        return bmi
    except ZeroDivisionError:
        print("Error: Weight should be greater than zero.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
