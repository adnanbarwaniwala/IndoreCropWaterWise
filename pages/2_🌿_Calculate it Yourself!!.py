import numpy as np
import streamlit as st
from helper import possible_weather_factor_choices

st.set_page_config(
    page_title='IndoreCropWaterWise',
    page_icon=':droplet:',
    layout='wide'
)

# CSS styling for better visuals
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: None;
        border-radius: 10px;
        font-size: 18px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
    """, unsafe_allow_html=True)


def set_ok_button_true():
    st.session_state.ok_button = True


# Loads the best configured model for a particular combination of weather factors
def best_model_for_factors_comb(idx):
    from helper import factors_comb_mapped_to_model_and_type
    model_type, model_path = factors_comb_mapped_to_model_and_type[idx]
    if model_type == 'lgbm':
        import joblib
        model = joblib.load(model_path)
    else:
        from tensorflow.keras.models import load_model
        model = load_model(model_path)
    return model_type, model


# ETc is evapotranspiration adjusted for crops.
# It calculates the ETc using the predicted evapotranspiration from the model, the selected crop type and growth stage.
# Kc is a factor used to adjust the predicted evapotranspiration for a specific crop, taking into account its growth
# stage as well.
def calculating_ETc(crop_choice, growth_stage, ET0):
    from helper import crop_type_and_stage_to_kc
    Kc = crop_type_and_stage_to_kc[crop_choice][growth_stage]
    return ET0 * Kc


st.title('Crop Water Requirements 🌱')

col1, buff, col2 = st.columns([1, 0.1, 1])

with col1:
    st.subheader("🌾 **Select Your Crop and Growth Stage**")
    crop_types = ['Chickpeas / Gram', 'Corn / Maize', 'Dry Onions', 'Green Onions', 'Soybean', 'Wheat']
    crop_choice = st.selectbox('Crop Type:', crop_types, help="Select the crop type you're interested in.")

    growth_stages = ['Initial', 'Mid-Season', 'Late Season']
    growth_stage = st.selectbox('Growth Stage of Crop:', growth_stages,
                                help="Choose the current growth stage of your crop.")

with col2:
    st.subheader("☁️ **Select Weather Factors**")
    weather_factors = ['Mean Temperature (C)', 'Minimum Temperature (C)', 'Maximum Temperature (C)', 'Wind Speed (m/s)',
                       'Relative Humidity (%)', 'Surface Pressure (kPa)']
    weather_factor_choices = st.multiselect('Weather Factors:', weather_factors,
                                            help="Choose the weather factors available for today.")

    # Keeps a track of the state of the OK button: whether it's been clicked or not.
    if 'ok_button' not in st.session_state:
        st.session_state.ok_button = False

    ok = st.button('OK', on_click=set_ok_button_true)
    if st.session_state.ok_button:
        if sorted(weather_factor_choices) not in possible_weather_factor_choices:
            st.error("🚫 Please choose a valid combination of weather factors!")
        else:
            model_inputs = []
            mean_temp = st.number_input("🌡️ Enter the Mean Temperature (C):", on_change=set_ok_button_true)
            model_inputs.append(mean_temp)

            max_temp = st.number_input("🌞 Enter the Maximum Temperature (C):", on_change=set_ok_button_true)
            model_inputs.append(max_temp)

            min_temp = st.number_input("🌙 Enter the Minimum Temperature (C):", on_change=set_ok_button_true)
            model_inputs.append(min_temp)

            if 'Wind Speed (m/s)' in weather_factor_choices:
                wind_speed = st.number_input("🌬️ Enter the Wind Speed (m/s):", on_change=set_ok_button_true)
                model_inputs.append(wind_speed)

            if 'Relative Humidity (%)' in weather_factor_choices:
                relative_humidity = st.number_input("💧 Enter the Relative Humidity (%):", on_change=set_ok_button_true)
                model_inputs.append(relative_humidity)

            if 'Surface Pressure (kPa)' in weather_factor_choices:
                surface_pressure = st.number_input("🌀 Enter the Surface Pressure (kPa):", on_change=set_ok_button_true)
                model_inputs.append(surface_pressure)

            calculate = st.button('CALCULATE')
            if calculate:
                with st.spinner('Calculating 🔄'):
                    model_type, model = best_model_for_factors_comb(
                        # Returns the index of the list of chosen weather factors from the list of possible weather
                        # factor combinations.
                        possible_weather_factor_choices.index(sorted(weather_factor_choices))
                    )

                    # ET0 is the reference evapotranspiration.
                    predicted_et0 = model.predict(np.array([model_inputs]))

                    # Some models output a 1D array while some output a 2D array. Hence, this check is necessary.
                    if len(predicted_et0.shape) == 1:
                        ETc = calculating_ETc(crop_choice, growth_stage, predicted_et0[0])
                    else:
                        ETc = calculating_ETc(crop_choice, growth_stage, predicted_et0[0, 0])
                    st.success(f"✅ The predicted ET for your crop: **{ETc:.2f} mm**")
                    st.balloons()
