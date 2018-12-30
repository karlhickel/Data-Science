
# Import the `pandas` library as `pd`
import pandas as pd
pd.options.display.max_columns = 13
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()




# Load in the data with `read_csv()`
digits = pd.read_csv("~/Desktop/gdp.csv")

# Print out `digits`


print(digits)
print(digits.describe())
print(len(digits))
columns =digits.iloc[52:59,1:3]
print(columns)
#plt.plot(columns)


objects = ('New England', 'Mideast', 'Great Lakes', 'Plains', 'Southeast', 'Southwest','Rocky Mountain')
y_pos = np.arange(len(objects))
performance = [56689,57659,46076,48092,40543,48205,45634]
 
plt.bar(y_pos, performance, align='center', alpha=1)
plt.xticks(y_pos)
plt.ylabel('GDP')
plt.title('GDP Per Capita per region')
 
plt.show()





