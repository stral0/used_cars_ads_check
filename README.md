# babydontlie
Analysis of the Serbian biggest advertising platform for used vehicles (www.polovniautomobili.com) and trying to see if those mileages shown there are trustworthy. 

# Libraries used:
1. BeautifulSoup for parsing the html pages.
2. MatplotLib for visualization of the results.
3. Other python3 libraries.

# Data
The data used is obtained by this same script, using the function go_thru_all_ads().
It was ran on Monday, 28/DEC/2020, and it saved all 67250 active vehicle ads it found on the website.
The only preprocessing done is saving basic cars' parameters as appropriate data types and deleting unit labels. Also, I removed all of the vehicles with mileage bigger than 400.000 (less than 10 of the vehicles). 
 
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

Almost all of them had similar results, which show us that this parameter is not trustworthy.

![do2000](https://user-images.githubusercontent.com/18012692/112129578-d8623680-8bc7-11eb-9720-c60f3f2f1998.PNG)

![2001-2010](https://user-images.githubusercontent.com/18012692/112129600-dc8e5400-8bc7-11eb-9e3e-38efb4bb581e.PNG)

![2011-2020](https://user-images.githubusercontent.com/18012692/112129609-df894480-8bc7-11eb-9bc8-cc3b7327afb2.PNG)

