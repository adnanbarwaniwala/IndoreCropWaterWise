import streamlit as st

st.set_page_config(
    page_title='IndoreCropWaterWise',
    page_icon=':droplet:'
)

# Title and Project Introduction
st.title("IndoreCropWaterWise (ICWW) 🌾💧 - An Intro")
st.subheader("A Smart Solution for Predicting Irrigation Requirements in Indore")

st.markdown("""
**IndoreCropWaterWise (ICWW)** is a cutting-edge project designed to predict irrigation requirements (IR) 
for various crops specifically in the Indore region. Using advanced AI models like **Light Gradient Boosting Machines (LGBM)** 
and **Artificial Neural Networks (ANN)**, ICWW produces accurate evapotranspiration (ET) predictions based on vast amounts of 
training data which are then used to predict the IR. The predicted IR is in *mm of water per unit field area per day*.

To get started, you will need to enter today's values for certain meteorological data including estimated rain, select the crop 
type and its growth stage and select your irrigation type.
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
2. **Cotton**
3. **Field Corn (Maize)**
4. **Soybean**
5. **Sweet Corn (Maize)**
6. **Winter Wheat**
""")

# List of growth stages
st.subheader("🌿 Growth Stages")
st.write("Select the growth stage of your crop:")
st.markdown("""
1. **Initial**
2. **Mid-Season**
3. **Late Season**
""")

st.subheader("🚰 Drip Type and Precipitation")
st.write("You can choose from 3 possible irrigation systems:")
st.markdown("""
1. **Drip**
2. **Sprinkler**
3. **Surface**
""")
st.write("Next, you'll have to enter the forecasted rain for today.")

# Instructions for data input
st.subheader("📝 How to Enter Data")
st.write("""
After selecting the relevant information, enter today's values for the chosen weather factors and then hit **CALCULATE!!**
""")

# Kc values and crop information
st.subheader("🔍 Important Information")
st.write("""
The Kc values used to adjust the ET predicted by the models for the selected crops are standard values taken from the 
following FAO website:
""")
st.markdown("[FAO Crop Coefficients (Kc) Values](https://www.fao.org/4/X0490E/x0490e0b.htm#length%20of%20growth%20stages)")

st.write("The crop options available are based on the most common crop types grown in Indore.")

# Thank you message
st.subheader("🙏 Thank You!")
st.write("Thank you for trying out **IndoreCropWaterWise**! We hope this tool helps you optimize water usage for your crops.")
