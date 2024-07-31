possible_weather_factor_choices = [sorted(['Mean Temperature (C)', 'Maximum Temperature (C)', 'Minimum Temperature (C)']),
                                   sorted(['Mean Temperature (C)', 'Maximum Temperature (C)', 'Minimum Temperature (C)',
                                           'Wind Speed (m/s)']),
                                   sorted(['Mean Temperature (C)', 'Maximum Temperature (C)', 'Minimum Temperature (C)',
                                           'Wind Speed (m/s)',
                                           'Relative Humidity (%)', 'Surface Pressure (kPa)'])]

factors_comb_mapped_to_model_and_type = {
    0: ('nn', 'saved_models/nn_temp.keras'),
    1: ('lgbm', 'saved_models/lgbm_ws.pkl'),
    2: ('nn', 'saved_models/nn_all.keras')
}

crop_type_and_stage_to_kc = {
    'Chickpeas / Gram': {'Initial': 0.4, 'Mid-Season': 0.8, 'Late Season': 0.35},
    'Corn / Maize': {'Initial': 0.3, 'Mid-Season': 1.2, 'Late Season': 0.6},
    'Dry Onions': {'Initial': 0.7, 'Mid-Season': 1.05, 'Late Season': 0.75},
    'Green Onions': {'Initial': 0.7, 'Mid-Season': 1.0, 'Late Season': 1.0},
    'Soybean': {'Initial': 0.4, 'Mid-Season': 1.15, 'Late Season': 0.5},
    'Wheat': {'Initial': 0.7, 'Mid-Season': 1.15, 'Late Season': 0.4}
}

# intro_string = """IndoreCropWaterWise (ICWW) is a project developed to predict the evapotranspiration (ET) for different
# types crops, specifically for Indore. To predict the ET, it makes use of AI models like Light Gradient Boosting Machines
# and Artificial Neural Networks that have been trained on vast amounts of data in the same. To calculate the ET, you'll
# need to enter today's values for certain meteorological data and select the crop type and its growth stage. You can
# choose from 5 possible combinations of weather factors:
#     1. Mean Temperature (C), Maximum Temperature (C) and Minimum Temperature (C)
#     2. Mean Temperature (C), Maximum Temperature (C), Minimum Temperature (C), and Surface Pressure (kPa)
#     3. Mean Temperature (C), Maximum Temperature (C), Minimum Temperature (C) and Relative Humidity (%)
#     4. Mean Temperature (C), Maximum Temperature (C), Minimum Temperature (C) and Wind Speed (m/s)
#     5. Mean Temperature (C), Maximum Temperature (C), Minimum Temperature (C), Wind Speed (m/s),
#        Relative Humidity (%) and Surface Pressure (kPa)
#
#     Note: If you'll choose a different combination, you'll get an error. The order of factors is unimportant.
#
# You can choose from 6 possible crop types:
#     1. Chickpeas / Gram
#     2. Corn / Maize
#     3. Dry Onions
#     4. Green Onions
#     5. Soybean
#     6. Wheat
#
# You can choose from 3 possible growth stages for your crop:
#     1. Initial
#     2. Mid-Season
#     3. Late Season
#
# After selecting the relevant information, you'll need to enter today's values for the chosen weather factors and then
# hit CALCULATE!! For today's weather data about Indore, you can use the following website of NASA:
#     https://power.larc.nasa.gov/data-access-viewer/
#
# The training data for the models has also been acquired from here.
#
# Another important thing to note is that the Kc values used to adjust the ET predicted by the models for the selected
# crops are average agreed on values taken from the following FAO website:
#     https://www.fao.org/4/X0490E/x0490e0b.htm#length%20of%20growth%20stages
#
# Additionally, the crop options available are based on the most common crop types grown in Indore.
#
# Thank you for trying out my project!!
# """


