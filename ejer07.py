"""
Programa que nos permita calcular la cuota de una hipoteca y su tabla de amortización después de que se pida al usuario/a:

Importe del préstamo.
La tasa de interés anual.
Y el plazo de pago en años.
"""

print("Programa que nos permita calcular la cuota de una hipoteca y su tabla de amortización")
print("\n")

loan_amount = float(input("Introduce el importe del préstamo (€): "))
annual_interest_rate = float(input("Introduce la tasa de interés anual (%): "))
years = int(input("Introduce el plazo de pago en años: "))

if loan_amount <= 0 or annual_interest_rate <= 0 or years <= 0:
    print("Error. Debes introducir valores positivos")
else:
    monthly_interest = annual_interest_rate / 12 / 100
    num_payments = years * 12

    if monthly_interest == 0:
        monthly_payment = loan_amount / num_payments
    else:
        monthly_payment = loan_amount * monthly_interest * (1 + monthly_interest) ** num_payments / ((1 + monthly_interest) ** num_payments - 1)

    print("La cuota mensual es de: ", monthly_payment)

    print("Mes", "Cuota", "Interés", "Amortización", "Saldo")

    balance = loan_amount

    for month in range(1, num_payments + 1):
        interest = balance * monthly_interest
        principal = monthly_payment - interest
        balance -= principal
        print(month, monthly_payment, interest, principal, balance)

        if balance <= 0:
            balance = 0
            print(f"{num_payments}\t{monthly_payment}\t{interest}\t{principal}\t{balance}")
