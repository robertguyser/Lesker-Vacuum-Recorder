import numpy as np
import matplotlib.pyplot as plt
from matplotlib import lines


with open('VacuumChar-4-19-2017.csv') as f:
    data = f.readlines()

print data
print len(data)

times = np.arange(0,len(data),1)  # [{1,2,3,4,...}]

print times
fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.set_title("Vacuum System Performance",fontsize=20)
ax1.set_xlabel('Time(seconds)',fontsize=17)
ax1.set_ylabel('Vacuum(Torr)',fontsize=17)

#ax1.semilogy(times,data, c='r', label='Vacuum Torr',linewidth=3.3)
ax1.loglog(times,data, c='r', label='Vacuum Torr(log-log)',linewidth=3.3)


ax1.annotate('Vacuum Off: '+str(data[315]) + ' Torr(~94mTorr)', xy=(500, 0.15),size=17, xytext=(600, 0.15),
            arrowprops=dict(arrowstyle="fancy",facecolor='black'),
            )

ax1.annotate('Vacuum On', xy=(8, 820),size=17, xytext=(12, 775),
            arrowprops=dict(arrowstyle="fancy",facecolor='black'),
            )
ax1.plot(1500, .06, label='Old Vac', marker='o')


plt.xlim(1,5E4)
leg = ax1.legend()

plt.show()