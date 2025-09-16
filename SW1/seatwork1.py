def convert_dollar(dollars):
    peso = round(dollars * 57.17 , 2)
    yen = round(dollars * 146.67, 2)
    return dollars, peso, yen
dollar_amount = [59, 200, 500]
for amount in dollar_amount:
    usd, php, jpy = (convert_dollar(amount))
    print(f"${usd} = Php {float(php)}, JPY {float(jpy)}")