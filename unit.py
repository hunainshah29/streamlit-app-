import streamlit as st

def convert_units(value, from_unit, to_unit):
    conversions = {
        "Length": {"Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701},
        "Weight": {"Kilogram": 1, "Gram": 1000, "Pound": 2.20462, "Ounce": 35.274},
        "Temperature": {"Celsius": 1, "Fahrenheit": lambda c: (c * 9/5) + 32, "Kelvin": lambda c: c + 273.15}
    }
    
    for category, units in conversions.items():
        if from_unit in units and to_unit in units:
            if category == "Temperature":
                if callable(units[to_unit]):
                    return units[to_unit](value)
                elif callable(units[from_unit]):
                    return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 273.15)
            else:
                return value * (units[to_unit] / units[from_unit])
    return None

st.title("Unit Converter by Hunain Shah")

unit_type = st.selectbox("Select Unit Type", ["Length", "Weight", "Temperature"])

if unit_type:
    units = list({
        "Length": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"],
        "Weight": ["Kilogram", "Gram", "Pound", "Ounce"],
        "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
    }[unit_type])
    
    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    value = st.number_input("Enter Value", value=0.0, step=0.1)
    
    if st.button("Convert"):
        result = convert_units(value, from_unit, to_unit)
        if result is not None:
            st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
        else:
            st.error("Invalid conversion")
