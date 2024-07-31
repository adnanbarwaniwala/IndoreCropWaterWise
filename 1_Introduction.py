import streamlit as st

st.set_page_config(
    page_title='IndoreCropWaterWise',
    page_icon=':droplet:'
)

# Title and Project Introduction
st.title("IndoreCropWaterWise (ICWW) 🌾💧 - An Intro")
st.subheader("A Smart Solution for Predicting Crop Evapotranspiration in Indore")

st.write("""
**IndoreCropWaterWise (ICWW)** is a cutting-edge project designed to predict evapotranspiration (ET) 
for various crops specifically in the Indore region. Using advanced AI models like **Light Gradient Boosting Machines (LGBM)** 
and **Artificial Neural Networks (ANN)**, ICWW provides accurate ET predictions based on vast amounts of training data.

To get started, you will need to enter today's values for certain meteorological data and select the crop type and its growth stage.
Here are the steps you need to follow:
""")

# List of weather factor combinations
st.subheader("🔄 Weather Factor Combinations")
st.write("Choose from 3 possible combinations of weather factors:")
st.markdown("""
1. **Mean Temperature (C), Maximum Temperature (C), and Minimum Temperature (C):**
   - *Moderate Accuracy*
   
2. **Mean Temperature (C), Maximum Temperature (C), Minimum Temperature (C) and Wind Speed (m/s):**
   - *High Accuracy*
   
3. **Mean Temperature (C), Maximum Temperature (C), Minimum Temperature (C), Wind Speed (m/s), Relative Humidity (%) and Surface Pressure (kPa):**
   - *Very High Accuracy*

*Note: If you choose a different combination, you'll get an error. The order of factors is unimportant.*
""")

# List of crop types
st.subheader("🌱 Crop Types Available")
st.write("You can choose from 6 possible crop types:")
st.markdown("""
1. **Chickpeas / Gram**
2. **Corn / Maize**
3. **Dry Onions**
4. **Green Onions**
5. **Soybean**
6. **Wheat**
""")

# List of growth stages
st.subheader("🌿 Growth Stages")
st.write("Select the growth stage of your crop:")
st.markdown("""
1. **Initial**
2. **Mid-Season**
3. **Late Season**
""")

# Instructions for data input
st.subheader("📝 How to Enter Data")
st.write("""
After selecting the relevant information, enter today's values for the chosen weather factors and then hit **CALCULATE!!** 
For today's weather data about Indore, you can use the following website of NASA:
""")
st.markdown("[NASA POWER Data Access Viewer](https://power.larc.nasa.gov/data-access-viewer/)")

# Training data source
st.write("The training data for the models has also been acquired from this source.")

# Kc values and crop information
st.subheader("🔍 Important Information")
st.write("""
The Kc values used to adjust the ET predicted by the models for the selected crops are average agreed-on values taken from the 
following FAO website:
""")
st.markdown("[FAO Crop Coefficients (Kc) Values](https://www.fao.org/4/X0490E/x0490e0b.htm#length%20of%20growth%20stages)")

st.write("The crop options available are based on the most common crop types grown in Indore.")

# Thank you message
st.subheader("🙏 Thank You!")
st.write("Thank you for trying out **IndoreCropWaterWise**! We hope this tool helps you optimize water usage for your crops.")