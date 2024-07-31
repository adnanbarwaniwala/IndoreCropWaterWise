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

The available growth stages include:
- Intial
- Mid-Season
- Late-Season


### 🌦️ Weather Factor Combinations
You can choose from the following weather factor combinations based on data availability:
1. **Mean Temperature (C), Maximum Temperature (C), and Minimum Temperature (C)**
   - *Moderate Accuracy*
     
2. **Mean Temperature (C), Maximum Temperature (C), Minimum Temperature (C) and Wind Speed (m/s)**
   - *High Accuracy* 
     
3. **Mean Temperature (C), Maximum Temperature (C), Minimum Temperature (C), Wind Speed (m/s), Relative Humidity (%) and Surface Pressure (kPa)**
   - *Very High Accuracy* 


### 📊 Trained Models
The project includes 3 trained models trained with over 37 years of weather data:
- **LGBM**: Trained with weather data including temperature and wind speed, providing high accuracy in ET prediction.
- **Neural Networks**:
  - One model is trained only on temperature data for ET predictions
  - The other model is trained on many weather factors like temperature, wind speed, humidity and pressure for very accurate ET predictions.

## Contact

For questions or suggestions, please open an issue or contact me directly:

- **Email**: adnanbarwaniwala7@gmail.com
