def celsius_to_kelvin(celsius):
    """
    Function to return Kelvin degrees from Celsius input
    """
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def celsius_to_fahrenheit(celsius):
    return celsius * 9./5 + 32

def mean_temperature(data):
    """
    Get the mean temperature.
    
    Args:
        data (pandas.DataFrame): A pandas dataframe with air temperature measurements.

    Returns:
        The mean air temperature (float)
    """
    temperatures = data['Air temerature (degC)']
    return sum(temperatures)/len(temperatures)

