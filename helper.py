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
    'Chickpeas / Gram': {'Initial': 0.4, 'Mid-Season': 0.8, 'Late Season': 0.35},
    'Corn / Maize': {'Initial': 0.3, 'Mid-Season': 1.2, 'Late Season': 0.6},
    'Dry Onions': {'Initial': 0.7, 'Mid-Season': 1.05, 'Late Season': 0.75},
    'Green Onions': {'Initial': 0.7, 'Mid-Season': 1.0, 'Late Season': 1.0},
    'Soybean': {'Initial': 0.4, 'Mid-Season': 1.15, 'Late Season': 0.5},
    'Wheat': {'Initial': 0.7, 'Mid-Season': 1.15, 'Late Season': 0.4}
}
