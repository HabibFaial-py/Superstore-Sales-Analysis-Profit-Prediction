# Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from sklearn.linear_model import LinearRegression
import matplotlib.dates as mdates
import plotly.express as px

# Upload CSV
df = pd.read_csv("Sample - Superstore.csv", encoding='latin1') # load csv
df.head() # first 5 lines
df.info() # datatypes
df.describe() # basic stats for numeric columns
df.isnull().sum() # look out for missing values

# Clean Data
df.dropna(inplace=True) #drop missing values
df.drop_duplicates(inplace = True) # remove duplicat
df = df.groupby("Order ID" , as_index = False).agg({  #Separate all Products with same Order ID
     "Order Date": "first",
    "Ship Date": "first",
    "Ship Mode": "first",
    "Customer ID": "first",
    "Segment": "first",
    "Country": "first",
    "City": "first",
    "State": "first",
    "Postal Code": "first",
    "Region": "first",
    "Sales": "sum",
    "Quantity": "sum",
    "Discount": "mean",
    "Profit": "sum"
})
df = df[df["Ship Date"] >= df["Order Date"]] # remove orders with order date greater that ship date
df = df[df["Quantity"] > 0 ] # remove data with 0 or less quantity
df = df[(df["Discount"] >= 0) & (df["Discount"] <= 1)] #  remove data with discount greater than 1 or less than 0
df.info() # display
df.to_csv("cleaned_superstore.csv", index=False) # create clean csv
print("This is a Sales and Order Line Chart")
# Analysis
df = pd.read_csv("cleaned_superstore.csv") # load new csv
# (a) Sales and Order Date
sales_trend = df.groupby("Order Date")["Sales"].sum().reset_index() # create data 
plt.figure(figsize=(30,12)) # create size of chart
plt.plot(sales_trend["Order Date"] , sales_trend["Sales"] ,marker = "o" ,linewidth = 1) # make line chart
plt.title("Sales vs Order Date" , fontsize = 14) # title
plt.xlabel("Order Date") # xlabel
plt.ylabel("Sales") # ylabel
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())     # show monthly ticks
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m")) # show date form
plt.xticks(rotation = 45) # rotate 
plt.grid(alpha = 0.3) # transperancy
plt.show() # dispaly
print("This is a Saegment and Sales Line Chart")
# (b) Segment and Sales
sales_trend = df.groupby("Segment")["Profit"].sum().reset_index() # create data
plt.figure(figsize=(30,12)) # create size of chart
plt.plot(sales_trend["Segment"] , sales_trend["Profit"] ,marker = "o" ,linewidth = 1) # create line chart
plt.title("Segment vs Profit" , fontsize = 14) # title
plt.xlabel("Segment") # xlabel
plt.ylabel("Profit") # ylabel
plt.xticks(rotation = 45) # rotate
plt.grid(alpha = 0.3) # transpearncy
plt.show() # display
print("This is a Sagment and Sales Bar Chart")
# (c) Segment and Sales
plt.figure(figsize=(10,5)) # create size of chart
sns.barplot(x="Segment",y="Sales" , data = df ,palette = "magma") # plot the top 10 values 
plt.xticks(rotation = 45) # rotate xticks by 45 degrees
plt.title("Sales vs Segment") # display title of chart
plt.show() # discplay chart
print("This is a Discount and Profit ScatterPlot")
#(d) Discount and Profit
plt.figure(figsize = (7,20)) # create size of chart
sns.scatterplot(data = df , x="Discount" , y = "Profit" , alpha = 0.5, marker = "o" , palette = "magma") # create a scatterplt
plt.title("Discount / Profit") # title 
plt.ylim(0,800) # y axis coordinates
plt.show() # display
print('This is a sales piechart , for regions')
#(e) 
plt.figure(figsize = (10,10)) # size
sales_region = df.groupby("Region")["Sales"].sum() # create data
palettefinal = sns.color_palette("plasma" , len(sales_region)) # create piecharet color
plt.pie(sales_region, labels = sales_region.index , autopct="%1.1f%%", startangle=90 , colors=palettefinal)# create piecharet
plt.show() # display
print("This is a ChoroPleth Chart showing the sales across USA")
#(f) ChoroPeth Chart
name_to_code = {
    "Alabama":"AL","Alaska":"AK","Arizona":"AZ","Arkansas":"AR","California":"CA",
    "Colorado":"CO","Connecticut":"CT","Delaware":"DE","District of Columbia":"DC",
    "Florida":"FL","Georgia":"GA","Hawaii":"HI","Idaho":"ID","Illinois":"IL",
    "Indiana":"IN","Iowa":"IA","Kansas":"KS","Kentucky":"KY","Louisiana":"LA",
    "Maine":"ME","Maryland":"MD","Massachusetts":"MA","Michigan":"MI","Minnesota":"MN",
    "Mississippi":"MS","Missouri":"MO","Montana":"MT","Nebraska":"NE","Nevada":"NV",
    "New Hampshire":"NH","New Jersey":"NJ","New Mexico":"NM","New York":"NY",
    "North Carolina":"NC","North Dakota":"ND","Ohio":"OH","Oklahoma":"OK","Oregon":"OR",
    "Pennsylvania":"PA","Rhode Island":"RI","South Carolina":"SC","South Dakota":"SD",
    "Tennessee":"TN","Texas":"TX","Utah":"UT","Vermont":"VT","Virginia":"VA",
    "Washington":"WA","West Virginia":"WV","Wisconsin":"WI","Wyoming":"WY"}
state_sales = df.groupby("State")["Sales"].sum().reset_index() # create Data
state_sales["state_code"] = state_sales["State"].map(name_to_code)
fig = px.choropleth( # Add Data
    state_sales,
    locations = "State",
    locationmode = "USA-states",
    color = "Sales",
    scope = "usa",
    color_continuous_scale = "magma",
    range_color=(0, 2500)
)
state_sales["state_code"] = state_sales["state_code"].str.upper().str.strip()
fig.update_layout(title_text = 'Total Sales by State') # title
fig.show() # display
print("Shows the prediction of profit according to previous results")
# ML Addition
X = df[["Sales"]] # set X
y = df[["Profit"]] # set Y

model = LinearRegression() # Load model
model.fit(X,y) # train model
df["Predicted_Profit"] = model.predict(X) 
print(df[["Sales", "Profit", "Predicted_Profit"]].head()) #show()
print("ThankYou.")

















