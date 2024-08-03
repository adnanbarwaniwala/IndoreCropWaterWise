possible_weather_factor_choices = [sorted(['Mean Temperature (C)', 'Maximum Temperature (C)', 'Minimum Temperature (C)']),
                                   sorted(['Mean Temperature (C)', 'Maximum Temperature (C)', 'Minimum Temperature (C)',
                                           'Wind Speed (m/s)']),
                                   sorted(['Mean Temperature (C)', 'Maximum Temperature (C)', 'Minimum Temperature (C)',
                                           'Wind Speed (m/s)',
                                           'Relative Humidity (%)', 'Surface Pressure (kPa)'])]

factors_comb_mapped_to_model_and_type = {
    0: ('lgbm', 'saved_models/lgbm_temp.pkl'),
    1: ('nn', 'saved_models/nn_ws.keras'),
    2: ('nn', 'saved_models/nn_all.keras')
}

crop_type_and_stage_to_kc = {
    'Chickpeas / Gram': {'Initial': 0.4, 'Mid-Season': 1.0, 'Late Season': 0.35},
    'Cotton': {'Initial': 0.35, 'Mid-Season': 1.15, 'Late Season': 0.5},
    'Field Corn (Maize)': {'Initial': 0.3, 'Mid-Season': 1.20, 'Late Season': 0.35},
    'Sweet Corn (Maize)': {'Initial': 0.3, 'Mid-Season': 1.15, 'Late Season': 0.3},
    'Soybean': {'Initial': 0.4, 'Mid-Season': 1.15, 'Late Season': 0.5},
    'Winter Wheat': {'Initial': 0.3, 'Mid-Season': 1.15, 'Late Season': 0.4}
}

irrigation_type_to_efficiency = {
    'Drip': 0.9,
    'Sprinkler': 0.75,
    'Surface': 0.6
}


