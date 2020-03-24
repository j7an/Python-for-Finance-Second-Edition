import scipy as sp
cashflows = [-100, 50, 40, 20, 10, 50]
x = sp.npv(0.1, cashflows)
print(round(x, 2))

payments = sp.pmt(0.0387/12, 30*12, 375000)
print(round(payments, 2))