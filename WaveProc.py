import matplotlib.pyplot as plt
import sys
import pandas as pd

file_path=sys.argv[1]
data = pd.read_csv(file_path,skiprows=range(50),header=None,names=["datapoints"],encoding="utf-8")
print(data['datapoints'][:10])
plt.plot(data['datapoints'])
plt.title("Wave")
plt.xlabel("index")
plt.ylabel("Amplitude")
plt.savefig("test.png")
plt.show()
#you can deal with data['datapoints']
#calculate baseline
#integrate the area of every wave