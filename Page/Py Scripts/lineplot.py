import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
data = pd.read_csv("MTSUMADJ.csv")


sns.lineplot(x = "Stream length", y = "Peak viewers", data=data)
sns.set(style='dark',)
plt.title("Miss T Streams", fontsize =30)
plt.show()



  
