while True:

    зарплата = float(input("Введіть зарплату за місяць: "))
    кредитний_платіж = float(input("Введіть суму місячного кредитного платежу: "))
    заборгованість = float(input("Введіть заборгованість за комунальні послуги: "))


    залишок = зарплата - кредитний_платіж - заборгованість


    print(f"Залишок грошей після виплат: {залишок}")

    продовжити = input("Бажаєте ввести нові числа? (так/ні): ")
    if продовжити.lower() != 'так':
        break
