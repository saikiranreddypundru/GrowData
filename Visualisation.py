#Importing the Libraries.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

#Loading the data into a data frame.
df = pd.read_csv(r'./GrowLocations.csv')

#Dropping null values from the data frame.
df=df.dropna(how = 'any')

#Flip Longitude and Latitude columns as they seem to be incorrectly labelled.
df.rename(columns={'Longitude': 'Latitude', 'Latitude': 'Longitude'}, inplace=True)

#--------------------------------------------------------------------------------------------------
#Function to extract Latitude and Longitude Values from broken Serial Column values if needed.
#For the required bounding box coordinates this is not needed so commented out.
#Need to convert values to string for this method.
#df['Latitude'] = df['Latitude'].astype(str)
#df['Longitude'] = df['Longitude'].astype(str)
#
#def extract_value_from_serial_column(search_string, output_column_name):
#    for i in range(df.shape[0]):
#        if df['Serial'].iloc[i].find(search_string) != -1:
#            start = df['Serial'].iloc[i].find(search_string) + len(search_string)
#            end = start + df['Serial'].iloc[i][start:].find(",")
#            df[output_column_name].values[i] = df['Serial'].iloc[i][start:end]
#
#extract_value_from_serial_column("Longitude:", "Longitude")
#extract_value_from_serial_column("Latitude:", "Latitude")
#
#Removing potential blank cells by dropping the rows.
#empty_spaces = df[(df['Latitude'] == '')].index
#df.drop(empty_spaces , inplace=True)
#--------------------------------------------------------------------------------------------------

#Switch to numeric columns and remove values outside of bounding box of interest.
#Note this also excludes some unrealistically large values present in the dataset, i.e. greater than 90.
df[['Latitude', 'Longitude']] = df[['Latitude', 'Longitude']].apply(pd.to_numeric)
new_df=df[['Latitude', 'Longitude']].query('Latitude >= 50.681 and Latitude <= 57.985').query('Longitude >= -10.592 and Longitude <= 1.6848')

#Create Figure.
#Adapted from: https://www.tutorialspoint.com/drawing-circles-on-an-image-with-matplotlib-and-numpy
plt.rcParams["figure.figsize"] = [4.00, 4.00]
plt.rcParams["figure.autolayout"] = True

#Load image.
img = plt.imread(r'./map7.png')

#Set figure and axis properties.
fig, ax = plt.subplots(1)
ax.imshow(img, extent=[-10.592,1.6848,50.681,57.985])
plt.yticks(np.arange(51, 58, 1))

#Get locations as float.
x = new_df['Longitude'].to_numpy().astype(np.float)
y = new_df['Latitude'].to_numpy().astype(np.float)

#Draw circles for each location.
for xx, yy in zip(x, y):
   circ = Circle((xx, yy), 0.1, color='blue')
   ax.add_patch(circ)

#Show and save plot.
plt.title("Plotting the Grow data")
plt.savefig("output_visualisation.jpeg")
plt.show()





