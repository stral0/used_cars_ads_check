# babydontlie
Analysis of the Serbian biggest advertising platform for used vehicles (www.polovniautomobili.com) and trying to see if those mileages shown there are trustworthy. 

# Libraries used:
1. BeautifulSoup for parsing the html pages.
2. MatplotLib for visualization of the results.
3. Other python3 libraries.

# Data
The data used is obtained by this same script, using the function go_thru_all_ads().
It was ran on Monday, 28/DEC/2020, and it saved all 67250 active vehicle ads it found on the website.
The only preprocessing done is saving basic cars' parameters as appropriate data types and deleting unit labels: 
 
Fields saved are: 
1. url of the ad
2. brand of the vehicle
3. model of the vehicle
4. production year of the vehicle
5. fuel type of the vehicle
6. power of the vehicle
7. mileage in kilometers

# Results:
We can see how most owners have listed around 180k-200k mileages, no matter the production year of their respected vehicles.

I devided the vehicles in 
### 3 categories: 
1. Made before 2000, 
2. Made between 2001 and 2010, and
3. Made in 2011 or later. 

All of them had almost the same results, which show us that this parameter is not trustworthy.
