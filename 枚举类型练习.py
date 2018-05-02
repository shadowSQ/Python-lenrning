#枚举
from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name ,member in Month.__members__.items():
	print(name.'=>',member,',',member.value)
	#名字，成员，成员的值（默认从1开始）