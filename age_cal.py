import datetime
current_year = datetime.datetime.now().year

the_end = False
retryagain = False

while not the_end:
    print('\n<<< WELCOME TO AGE CALCULATOR >>>')
    name = input('\nType Your Name: ')
    yob = input('Type Your Year of Birth: ')

    try:
        check_yob = int(yob)
        age = current_year - check_yob
    except:
        print('[ERROR] Please Type Numeric Numbers Only! Try Again')
        continue

    print(f'\nHello "{name}" Your Current Age is: "{age}"')

    if age < 6:
        print(f'"{name}" You Are a Little Baby')
    elif age < 13:
        print(f'"{name}" You Are a Child')
    elif age < 20:
        print(f'"{name}" You Are a Teenager')
    elif age < 31:
        print(f'"{name}" You Are Young')
    elif age < 46:
        print(f'"{name}" You Are a Grown Person')
    else:
        print(f'"{name}" You Are Elder Person')

    while not the_end:
        retry = input('\nDo You Want To Try Again ? (Y/N): ')
        if retry.lower() == 'y':
            break
        elif retry.lower() == 'n':
            print(f'\nThank You "{name}" For Using Our Software :) Have a Nice Day!')
            the_end = True
        else:
            print('\nYou Entered Wrong Command! Please Type only "Y" or "N"): ')
            continue
    continue
