# IndoreCropWaterWise 🌾💧

**IndoreCropWaterWise** is an advanced AI-powered tool designed to predict the evapotranspiration (ET) of various crops specifically in the Indore region. By utilizing machine learning models, including Light Gradient Boosting Machines (LGBM) and Neural Networks, this project offers precise water requirements for crops, aiding farmers and agricultural planners in optimizing irrigation and water management.

## Project Structure

- **data**: Contains the dataset `final indore weather data.csv` with historical weather data used for training and prediction.
- **pages**: Includes Streamlit app pages, such as `2_🌿_Calculate it Yourself!!`, for an interactive user interface.
- **saved_models**: Stores trained models:
  - `lgbm_ws.pkl`: LGBM model for ET predictions using the temperature data and windspeed.
  - `nn_all.keras`: Neural Network model for ET prediction using all the available factors.
  - `nn_temp.keras`: Neural Network model for ET prediction using the temperature data only. 
- **helper.py**: Consists of variables used in the main file. Used for cleaner code.

## Features

### 🚀 Predict ET for Your Crops
IndoreCropWaterWise offers a user-friendly interface where you can input current weather conditions and select crop type and growth stage to receive precise ET predictions. The available crop types include:
- Chickpeas / Gram
- Corn / Maize
- Dry Onions
- Green Onions
- Soybean
- Wheat

### 🌦️ Weather Factor Combinations
Choose from the following weather factor combinations for accurate ET prediction:
1. **Mean Temperature (C), Maximum Temperature (C), and Minimum Temperature (C)**
   - (Accuracy: Moderate)
   
2. **Mean Temperature (C), Maximum Temperature (C), Minimum Temperature (C) and Wind Speed (m/s)**
   - (Accuracy: High)
   
3. **Mean Temperature (C), Maximum Temperature (C), Minimum Temperature (C), Wind Speed (m/s), Relative Humidity (%) and Surface Pressure (kPa)**
   - (Accuracy: Very High)

**Note:** If you choose a different combination of weather factors, you'll get an error. The order of factors is unimportant.

### 📊 Trained Models
The project includes trained models to provide accurate ET predictions:
- **LGBM**: Trained with weather data, providing high accuracy in ET prediction.
- **Neural Networks**: Offers robust predictions using a range of meteorological factors.

## Getting Started

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/IndoreCropWaterWise.git
