# -API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: SIMRAN AYUBKHAN PATHAN

*INTERN ID*: CT08KSV

*DOMAIN*: PYTHON 

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

*CODE EXPLANATION *:
This Python script fetches weather forecast data from the Weatherbit API and visualizes it using Matplotlib and Seaborn. Below are the key components of the code:

API Request & Data Retrieval
The script starts by importing necessary libraries: requests (for API requests), pandas (for data manipulation), and matplotlib.pyplot & seaborn (for data visualization).
The user is prompted to enter the city name.
The script then makes an API request to Weatherbit using the provided API key and retrieves weather data for the specified city in India.
If the API request is successful, the data is stored in JSON format; otherwise, an error message is displayed.

Data Processing & Preparation
The weather forecast data is extracted and stored in a Pandas DataFrame for structured analysis.
The datetime column is converted into a Pandas datetime format and set as the index.
The script selects key weather parameters: temperature (avg, max, min), precipitation, and wind speed.

Data Visualization
First Subplot: A line graph displays average daily temperature. The minimum and maximum temperature range is shaded in light blue.
Second Subplot: A bar chart represents daily precipitation, while a line graph overlays wind speed data.
Proper labels, legends, and axis rotations ensure clarity in visualization.

Final Display
The script uses plt.tight_layout() to optimize spacing and plt.show() to display the final weather dashboard


*OUTPUT*

![Image](https://github.com/user-attachments/assets/51f9cdd5-6fe8-49ac-9558-18ba7e771c56)

