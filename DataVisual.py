import plotly.express as px
import pandas as pd

df = pd.read_csv("data.csv")
# figure = px.line(df, x="Year", y="Per capita income", color="Country", title='Capita Income')

figure = px.scatter(df, x="Population", y='Per capita', size="Percentage", color='Country', size_max=60)

figure.show()