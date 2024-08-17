# Compund interest

def compound_interest(principal, rate, time):
    return principal * (1 + rate / 100) ** time

principal = float(1000)
rate = float(5)
time = float(5)

print("Compound interest is: ", compound_interest(principal, rate, time))
