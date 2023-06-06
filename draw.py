import os
from collections import defaultdict
import matplotlib.pyplot as plt

# path = "./expr/predator-prey"
path = "./expr/traffic-junction"


data = {}
for filename in os.listdir(path):
    print(filename)
    modelname = filename.split('-')[0]
    data[modelname] = defaultdict(list)
    with open(os.path.join(path, filename), 'r') as f:
        for line in f.readlines():
            # if line.startswith('Success'):
            #     data[modelname]['success'].append(float(line.split(': ')[-1]))
            if line.startswith('Steps-taken'):
                data[modelname]['Steps-taken'].append(float(line.split(': ')[-1]))
            
    print(data[modelname])

x = list(range(200))
for modelname in data:
    # plt.plot(x, data[modelname]['success'], label=modelname)
    plt.plot(x, data[modelname]['Steps-taken'], label=modelname)
    
# plt.ylabel('Success rate')
plt.ylabel('Steps-taken')

plt.xlabel('Epoch')
plt.legend(loc='best')
plt.show()

#