def print_menu():
    print('WELCOME!!!\nI\'M GLAD TO SEE THAT YOU ARE INTERESTED IN MY OWN LIBRARY IN STATISTICS')
    print('Here you can test the library with my ready made tests and compare the results between my and build-in implementation.\n')
    print(
        'Choose the test case! \
        \n\t0 -> EXIT \
        \n\t1 -> Bootstrapping \
        \n\t2 -> Descriptive Statistics \
        \n\t3 -> Hypothesis Testing \
        \n\t4 -> Linear Models \
        \n\t5 -> Univariate Calculus'
    )
choice = None
while True:
    print_menu()
    choice = input('\nOption: ')
    if choice not in ['0', '1', '2', '3', '4', '5']:
        print('\nInvalid Input\n')
        input('\nPress ENTER to continue!\n')
        continue
    match (choice):
        case '0':
            print('\nSee you next time!\n')
            break
        case '1':
            print()
            import tests.test_bootstrapping
            input('\nPress ENTER to continue!\n')
        case '2':
            print()
            import tests.test_descriptive_statistics
            input('\nPress ENTER to continue!\n')
        case '3':
            print()
            import tests.test_hypothesis_testing
            input('\nPress ENTER to continue!\n')
        case '4':
            print()
            import tests.test_linear_models
            input('\nPress ENTER to continue!\n')
        case '5':
            print()
            import tests.test_univariate_calculus
            input('\nPress ENTER to continue!\n')
