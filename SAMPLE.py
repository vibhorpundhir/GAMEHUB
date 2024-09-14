import random
from time import sleep

printertimer = ["\n\n\nLOADING THE PROGRAM\n", "🚨 🚨 🚨 🚨 🚨 🚨 🚨 🚨 🚨 🚨\n", "3\n",
                "🚨 🚨 🚨 🚨 🚨 🚨 🚨 🚨 🚨 🚨\n", "2\n", "🚨 🚨 🚨 🚨 🚨 🚨 🚨 🚨 🚨 🚨\n", "1\n", "🚨 🚨 🚨 🚨 🚨 🚨 🚨 🚨 🚨 🚨\n\n"]
for mess in printertimer:
    print(mess)
    sleep(0.2)


def calculator():
    import math
    print(
        "🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮 WELCOME TO THE CALCULATOR PROGRAM 🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮\n\n")
    print('''Available Operations
1. Add
2. Subtract
3. Divide
4. Multiply

Adv Extras
 5. Square Root
 6. Square
 7. Cube\n\n''')
    while True:
        calc_input = int(input("Enter your selection >>> "))
        if calc_input in (1, 2, 3, 4, 5, 6, 7):
            if calc_input == 1:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                addn = x + y
                print(f'The sum is : {addn}')
            elif calc_input == 2:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                subn = x - y
                print(f'The difference is : {subn}')
            elif calc_input == 3:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                divn = x / y
                divq = x % y
                print(f'\nThe remainder is : {divn}\nThe quotient is : {divq}')
            elif calc_input == 4:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                muln = x * y
                print(f'The product is : {muln}')
            elif calc_input == 5:
                x = float(input("Enter the number: "))
                sqrn = math.sqrt(x)
                print(f'The square root is : {sqrn}')
            elif calc_input == 6:
                x = float(input("Enter the number: "))
                sqn = x * x
                print(f'The square is : {sqn}')
            elif calc_input == 7:
                x = float(input("Enter the number: "))
                cn = x * x * x
                print(f'The cube is : {cn}')
            repeat = input("\nCalculate again? (y/n): ")
            if repeat == "n" or repeat == 'no' or repeat == 'NO' or repeat == 'N':
                print(
                    "\n🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮 END OF PROGRAM 🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮🧮\n\n")
                break
        else:
            break


def winsim():
    import maskpass
    import datetime
    from time import sleep
    print(
        '''++++++++++++++++++++++++++++++++++++++++++ WELCOME TO WINDOWS 11 LOGIN SIMULATOR ++++++++++++++++++++++++++++++++++++++++++\n''')
    password = 'billygates'
    tries = ""
    counter = 0
    count = 2
    limit = 3
    out = False
    print("Enter the correct password to Login [3 Tries Left] ")
    while tries != password and not (out):
        if counter < limit:
            tries = maskpass.askpass(
                prompt="Enter the secure password >>> ", mask="👾")
            if password != tries:
                print('\nYou have entered a wrong password')
                print(
                    f'Enter the correct password to Login [{count} Tries Left]\n')
            counter = counter + 1
            count = count - 1
        else:
            out = True
    if out:
        print("========== You have run out of tries ==========\n")
    else:
        print("Correct Password entered\n")
        printertimer = ["Now Logging in......", "Windows Login succesful\n"]
        for mess in printertimer:
            print(mess)
            sleep(2)
    now = datetime.datetime.now()
    print(now.strftime("Login Acitivity Detected on : %Y-%m-%d at %H:%M:%S\n"))
    print(
        '''++++++++++++++++++++++++++++++++++++++++++ END OF THE SIM +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n''')
    return


def drive():
    import random
    print(
        '''🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗 WELCOME DRIVING AUTHENTICATOR 🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗\n''')
    age = abs(int(input("Enter your age >>> ")))
    if age <= 17:
        print("\nYou are restricted from driving a vehicle\n\n")
    elif age > 17:
        lis = input("Do you have a driving license ? [YES/NO] >>>  ")
        if lis == 'YES' or lis == "Yes" or lis == "yes":
            print("You are allowed to drive")
            hash = random.getrandbits(128)
            print(f"Authentication Key validated : %032x\n" % hash)
            print("KEY ACCEPTED")
        else:
            print("\nYou are restricted from driving a vehicle\n\n")
    else:
        print("Invalid Input || Program Exiting\n\n\n")
    print(
        '''🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗 END OF THE DRIVING AUTHENTICATOR 🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗🚗\n''')


def temp():
    print(
        '🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️  TEMPRATURE CONVERTER 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️')

    print('''\nThis program support interconversions of tempratures\n
1. Celsius [c]
2. Fahrenheit [f]
3. Kelvin [k]
4. Rankine [r]\n''')
    while True:
        ini = input("Convert from >>> ")
        fin = input("Convert to >>> ")
        initemp = float(input("Enter the value >>> "))
        if ini == 'c' and fin == 'f':
            cf = initemp * 9 / 5 + 32
            print(f"\nThe temprature in Fahrenheit is : {'%.3f' % cf} °F")
        elif ini == 'c' and fin == 'k':
            ck = initemp + 273.15
            print(f"\nThe temprature in Kelvin is : {'%.3f' % ck} °K")
        elif ini == 'c' and fin == 'r':
            cr = initemp * 9 / 5 + 491.672
            print(f"\nThe temprature in Rankine is : {'%.3f' % cr} °R")
        elif ini == 'f' and fin == 'c':
            fc = (initemp - 32) * 5 / 9
            print(f"\nThe temprature in Celsius is : {'%.3f' % fc} °C")
        elif ini == 'f' and fin == 'k':
            fk = (initemp - 32) * 5 / 9 + 273.15
            print(f"\nThe temprature in Kelvin is : {'%.3f' % fk} °K")
        elif ini == 'f' and fin == 'r':
            fr = initemp + 459.67
            print(f"\nThe temprature in Rankine is : {'%.3f' % fr} °R")
        elif ini == 'r' and fin == 'c':
            rc = (initemp - 491.67) * 5 / 9
            print(f"\nThe temprature in Celsius is : {'%.3f' % rc} °C")
        elif ini == 'r' and fin == 'k':
            rk = initemp * 5 / 9
            print(f"\nThe temprature in Kelvin is : {'%.3f' % rk} °K")
        elif ini == 'r' and fin == 'f':
            rf = initemp - 459.67
            print(f"\nThe temprature in Fahrenheit is : {'%.3f' % rf} °F")
        repeat = input("\nConvert again? (y/n): ")
        if repeat == "n" or repeat == 'no' or repeat == 'NO' or repeat == 'N':
            print(
                "\n 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️  END OF PROGRAM 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️ 🌡️\n\n")
            break


def passgen():
    import array
    import random
    print('''🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐 SECURE PASSWORD GENERATOR 🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐\n\n''')
    useri_pass = int(
        input("RANGE 12-200 CHAR\nEnter the length of the password you want >>> "))
    limit = useri_pass
    nos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
             'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
             'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
             'z']

    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
             'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
             'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
             'Z']
    spec_chars = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                  '*', '(', ')', '<']
    combined = nos + upper + lower + spec_chars
    rand_digit = random.choice(nos)
    rand_upper = random.choice(upper)
    rand_lower = random.choice(lower)
    rand_symbol = random.choice(spec_chars)
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
    for x in range(limit - 4):
        temp_pass = temp_pass + random.choice(combined)
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    password = ""
    for x in temp_pass_list:
        password = password + x
        hmm = len(password)
    print(
        f'\nSecure Password Generated is : {password} \n\nVerified {hmm} character long\n\n')
    print('''🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐 END OF PROGRAM 🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐🔐\n\n''')


def bmi():
    print(
        '''❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹 WELCOME TO THE BMI CALCULATOR ❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹\n\nALL ENTRIES TO BE MADE IN METRIC UNITS\nHeight in Cms\nWeight in Kgs''')

    bmi_h = float(input("\nEnter your height >>> "))
    bmi_w = float(input("Enter your weight >>> "))
    heighm = bmi_h / 100
    bmipre = heighm * heighm
    bmical = bmi_w / bmipre
    if bmical < 18.5:
        print(f"\nYour BMI Value is {'%.2f' % bmical} and you are Underweight")
    elif bmical >= 18.5 and bmical <= 24.9:
        print(
            f"\nYour BMI Value is {'%.2f' % bmical} and your weight is Normal")
    if bmical >= 25 and bmical <= 29.9:
        print(f"\nYour BMI Value is {'%.2f' % bmical} and you are Overweight")
    if bmical >= 30 and bmical <= 34.9:
        print(f"\nYour BMI Value is {'%.2f' % bmical} and you are Obese")
    if bmical > 35:
        print(
            f"\nYour BMI Value is {'%.2f' % bmical} and you are Extremely Obese")

    from time import sleep
    printertimer = ["\n\nRANGES", "1. Underweight = < 18.5", "2. Normal = 18.5 to 24.9",
                    "3. Overweight = 25 to 29.9", "4. Obese = 30 to 34.9", "5. Extremely Obese = 35 <\n\n"]
    for mess in printertimer:
        print(mess)
        sleep(0.4)
    print(
        '''❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹 END OF PROGRAM ❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹❤️‍🩹\n\n\n''')


def roller():
    import random
    print('''🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲 DICE ROLLER 🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲\n\n''')
    x = "y"

    while x == "y":
        no = random.randint(1, 6)

        if no == 1:
            print('''                 +=======+
                 |       |
                 |   0   |
                 |       |
                 +=======+''')
        if no == 2:
            print('''                 +=======+
                 | 0     |
                 |       |
                 |     0 |
                 +=======+''')
        if no == 3:
            print('''                 +=======+
                 | 0     |
                 |   0   |
                 |     0 |
                 +=======+''')
        if no == 4:
            print('''                 +=======+
                 | 0   0 |
                 |       |
                 | 0   0 |
                 +=======+''')
        if no == 5:
            print('''                 +=======+
                 | 0   0 |
                 |   0   |
                 | 0   0 |
                 +=======+''')
        if no == 6:
            print('''                 +=======+
                 | 0 0 0 |
                 |       |
                 | 0 0 0 |
                 +=======+''')

        x = input("\nEnter 'y' to roll again and 'n' to exit : ")
        print('''\n\n🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲 END OF PROGRAM 🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲''')
        print("\n")


print('''-------------------------------------------------------------------------------------------------------''')
print("----------------------------------------WELCOME TO UTILITY PROGRAM-------------------------------------")
print('''-------------------------------------------------------------------------------------------------------\n''')
print('''>>>MENU<<<\n\nENTER CORRESPONDING NUMBER FOR ANY ONE OF THE FOLLOWING OPTIONS\n
1. Calculator
2. Temperature Converter
3. Driving Authenticator
4. Windows Login Sim
5. BMI Calculator
6. Secure Password Generator
7. Dice Roller
8. EXIT\n''')
user_input = int(input("Enter your option here : "))
print(f'Entered Input is : {user_input}\n')
print('''\n-------------------------------------------------------------------------------------------------------''')
print("----------------------------------------CREATED BY ME------------------------------")
print('''-------------------------------------------------------------------------------------------------------\n''')
if user_input == 1:
    calculator()
elif user_input == 2:
    temp()
if user_input == 3:
    drive()
elif user_input == 4:
    winsim()
elif user_input == 5:
    bmi()
elif user_input == 6:
    passgen()
elif user_input == 7:
    roller()
elif user_input == 8:
    print("Program exiting....\n\n")
else:
    print("Invalid Input || Program Exiting\n\n\n")
