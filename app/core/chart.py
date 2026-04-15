# chart.py
# This module contains functions to generate charts from query results.
# Purpose: This module abstracts the chart generation logic, allowing for easy updates to the visualization approach
# without affecting the main application flow. It uses matplotlib to create charts and returns them as base64-encoded images for easy embedding in web responses.


import matplotlib.pyplot as plt
import io
import base64


# Function to generate a bar chart from query results if numeric data is present.
def generate_chart(data: list):
    if not data:
        return None
    
    # Extract keys from the first row of data to determine which columns to use for x and y axes.
    keys = list(data[0].keys())

    if len(keys) < 2:
        return None

    x_key = keys[0]
    y_key = keys[1]


    # Attempt to extract x and y values for chart generation. If data is not suitable for charting (e.g., non-numeric y values), return None.
    try:
        x = [str(row[x_key]) for row in data]
        y = [float(row[y_key]) for row in data]
    except:
        return None


    # Generate a bar chart using matplotlib and save it to a buffer as a PNG image, then encode it in base64 for embedding in web responses.
    plt.figure()
    plt.bar(x, y)
    plt.xticks(rotation=45)

    buffer = io.BytesIO()
    plt.savefig(buffer, format="png", bbox_inches="tight")
    plt.close()

    buffer.seek(0) 

    image_base64 = base64.b64encode(buffer.read()).decode("utf-8")

    return f"data:image/png;base64,{image_base64}"