import datetime
import matplotlib.pyplot as plt
from matplotlib.finance import quotes_historical_yahoo_ochl
from matplotlib.dates import MonthLocator, DateFormatter

ticker = 'AAPL'
begdate = datetime.date(2012, 1, 2)
enddate = datetime.date(2013, 12, 5)
months = MonthLocator(range(1, 13), bymonthday=1, interval=3) # every 3rd month
monthsFmt = DateFormatter("%b '%Y")
x = quotes_historical_yahoo_ochl(ticker, begdate, enddate)

if len(x) == 0:
    print('Found no quotes')
    raise SystemExit

dates = [q[0] for q in x]
closes = [q[4] for q in x]
fig, ax = plt.subplots()
ax.plot_date(dates, closes, '-')
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(monthsFmt)
ax.xaxis.set_minor_locator(mondays)
ax.autoscale_view()
ax.grid(True)
fig.autofmt_xdate()