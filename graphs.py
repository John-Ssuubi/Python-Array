import matplotlib.pyplot as k

import numpy
xcode = numpy.array([10,20,30,40,50])
yxcode = numpy.array([5,7,2,3,9])


k.xlabel('MONTHS')
k.ylabel('Students')

k.title('BAR GRAPH OF WAR IN IRAN')

k.plot(xcode, yxcode)

k.bar(xcode, yxcode)
k.pie(xcode, yxcode)
k.show()

