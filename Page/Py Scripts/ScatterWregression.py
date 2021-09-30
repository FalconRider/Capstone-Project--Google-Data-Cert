import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('MM300ADJ2.csv')
sns.regplot(x="Stream length",
            y="Avg viewers", 
            data=df);
#sns.scatterplot(data = df, x = "Stream length", y = "Avg viewers")
plt.title("Miss M Streams", fontsize =30)
plt.show()

