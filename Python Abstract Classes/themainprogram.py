from fulltimeemployee import FulltimeEmployee
from hourlyemployee import HourlyEmployee
from payroll import Payroll

payroll = Payroll()

payroll.add(FulltimeEmployee("Yanfie", "Nam", 9000))
payroll.add(FulltimeEmployee("Eula", "Lawrence", 5500))
payroll.add(HourlyEmployee("Jean", "Gunnhildr", 400, 60))
payroll.add(HourlyEmployee("Ningguang", "Lim", 350, 200))
payroll.add(HourlyEmployee("Lisa", "Minci", 100, 250))

payroll.print()