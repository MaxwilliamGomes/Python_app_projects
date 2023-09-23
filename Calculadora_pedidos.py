Calculadora de pagamentos
A ideia aqui é criar uma calculadora de pagamentos compartilhada.

Sabe aquele momento em que estamos numa mesa com os amigos e temos que pagar a conta, mas você só pediu uma lata de Coca-Cola?

Isso mesmo, essa calculadora vai te ajudar a pagar apenas pelo que consumiu com o percentual da gorjeta referente ao que consumiu.





print("Welcome to tip calculator.")

value = float(input("Was a total bill? $ "))
descont = int(input("What percentage tip would you like to give? 10,12 or 15? "))/100
people = int(input("How many peopple to split to bill? "))

pay = float((value / people) * descont)
pay_total = round(pay + value/(people), 2)
print(F"Each person should pay : ${pay_total} ")
