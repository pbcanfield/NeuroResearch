import matplotlib.pyplot as plt

x_data = None
with open('hz_data.csv', 'r') as file:
    x_data = [(float(data)/10.0) for data in file.readline().split(',')]

    file.close()

print(x_data)

y_burst = []
file = open('y_data_burst.csv','r')
for value in file:
    y_burst.append(float(value) * 1e3)
file.close()

y_noburst = []
file = open('y_data_noburst.csv','r')
for value in file:
    y_noburst.append(float(value) * 1e3)
file.close()

cutoff = 130
x_data = x_data[:cutoff]
y_burst = y_burst[:cutoff]
y_noburst = y_noburst[:cutoff]

plt.figure(figsize=(5.5,5))
for label in plt.gca().get_yticklabels():
    label.set_fontsize(12)
for label in plt.gca().get_xticklabels():
    label.set_fontsize(12)
plt.plot(x_data,y_burst, label='CA3 Tonic Cell')
plt.plot(x_data,y_noburst, label='CA3 Adapting Cell')
plt.ylabel("(spk/sec)$^2$/Hz", fontsize=16)
plt.xlabel("Hz", fontsize = 16)
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0),useMathText=True)
plt.legend()
plt.tight_layout()

plt.show() 