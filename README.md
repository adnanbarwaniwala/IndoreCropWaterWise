# IndoreCropWaterWise (ICWW)🌾💧

**IndoreCropWaterWise** is an advanced AI-powered tool designed to calculate irrigation requirements (IR) for different types of crops at different stages of growth in Indore by predicting their evapotranspiration (ET) rates. By utilizing complex machine learning models like Light Gradient Boosting Machines (LGBM) and Neural Networks, this project accurately predicts water requirements for crops, aiding farmers and agricultural planners in optimizing irrigation and water management.

## Project Structure

- **data**: Contains the dataset `indore_weather_with_et0.csv` with historical weather data used for training and prediction.
- **pages**: Includes Streamlit app pages, such as `2_🌿_Calculate it Yourself!!`, for an interactive user interface.
- **saved_models**: Stores trained models:
  - `lgbm_temp.pkl`: LGBM model for ET predictions using temperature data only.
  - `nn_all.keras`: Neural Network model for ET prediction using all the available factors.
  - `nn_ws.keras`: Neural Network model for ET prediction using temperature and wind speed data. 
- **helper.py**: Consists of variables used in the main file. Used for cleaner code.

## Features

### 🚀 Predict ET for Your Crops
IndoreCropWaterWise offers a user-friendly interface where you can input current weather conditions incluidng forecasted precipitation and select crop type, its growth stage irrigation type used to receive precise IR predictions. The available crop types include:
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

The available irrigation types are:
- Drip
- Sprinkler
- Surface

### 🌦️ Weather Factor Combinations
You can choose from the following weather factor combinations based on data availability:
1. **Mean Temperature (C), Maximum Temperature (C), and Minimum Temperature (C)**
   - *Moderate Accuracy*
     
2. **Mean Temperature (C), Maximum Temperature (C), Minimum Temperature (C) and Wind Speed (m/s)**
   - *High Accuracy* 
     
3. **Mean Temperature (C), Maximum Temperature (C), Minimum Temperature (C), Wind Speed (m/s), Relative Humidity (%) and Surface Pressure (kPa)**
   - *Very High Accuracy* 


### 📊 Trained Models
The project includes 3 models trained on over 37 years of weather data:
- **LGBM**: Trained with temperature data, providing moderately accuracte ET predictions.
- **Neural Networks**:
  - One model is trained on temperature and wind speed data for high accuracy ET predictions.
  - The other model is trained on many weather factors including temperature, wind speed, humidity and pressure for very accurate ET predictions.

## Calculating IR
The predicted ET is run through a series of formulas to calculate a quantity called the *Gross Irrigation Requirement (GIR)* which has the units *mm of water per unit area per day.*

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* **FAO**: For providing crop coefficient values used in ET calculations.
  - [FAO Crop Coefficients (Kc) Values](https://www.fao.org/4/X0490E/x0490e0b.htm#length%20of%20growth%20stages)
* **NASA POWER**: For providing historical weather data for the Indore region.
  - [NASA POWER Data Access Viewer](https://power.larc.nasa.gov/data-access-viewer/)
## Contact

For questions or suggestions, please open an issue or contact me directly:

- **Email**: adnanbarwaniwala7@gmail.com

## 🙏 Thank You

Thank you for spending time on my repo. Hope you enjoyed it!
