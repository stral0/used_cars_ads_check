from bs4 import BeautifulSoup as BS
from bs4 import NavigableString, Comment

import urllib.request as urllib2 #using urllib.request bc this script is originally written for python2, and this is the way to run it with python3
from urllib.request import URLError

from time import sleep
from tqdm import tqdm

class Car:
  def __init__(self, url, brand, model, productionYear = -1, fuel = 'Unknown', power = 'Unknown', mileage_in_km = -1):
    self.url = url
    self.brand = brand
    self.model = model
    self.productionYear = productionYear
    self.fuel = fuel
    self.power = power
    self.mileage_in_km = mileage_in_km

  def __str__(self):

    return (self.getBrand() + ' ' + self.getModel() + ', ' + str(self.getProductionYear()) + ' -- ' + str(self.getMileage()) + 'km')

  def getUrl(self):
    return self.url

  def setUrl(self, url):
    self.url = url

  def getBrand(self):
    return self.brand

  def setBrand(self, brand):
    self.brand = brand

  def getModel(self):
    return self.model

  def setModel(self, model):
    self.model = model

  def getProductionYear(self):
    return self.productionYear

  def setProductionYear(self, productionYear):
    self.productionYear = productionYear

  def getFuel(self):
    return self.fuel

  def setFuel(self, fuel):
    self.fuel = fuel

  def getPower(self):
    return self.power

  def setPower(self, power):
    self.power = power


  def getMileageInKM(self):
    return self.mileage_in_km

  def setMileageInKM(self, mileage_in_km):
    self.mileage_in_km = mileage_in_km

def save_to_file(data, file_name='cars.pkl'): #kola.pkl

  import pickle
  f = open(file_name, 'wb')
  pickle.dump(data, f)
  f.close()

def read_cars_array_from_file(file_name='cars_1.pkl'):
  import pickle
  data = {}

  try:
    f = open(file_name, 'rb')
  except Exception as e:
    print ('Could not find the ' + file_name + '. Returning empty dict.')
    return {}

  data = pickle.load(f)
  f.close()
  return data

def missing_values_to_None(car_dict):

  params = ['url', 'brand', 'model', 'productionDate', 'fuelType', 'vehicleEngine', 'mileageFromOdometer']

  for p in params:
    if p not in car_dict:
      car_dict[p] = None

  return car_dict

def go_thru_all_ads():
  num_of_pages = 2690
  for page_num in tqdm(range(1, num_of_pages + 1)):
    all_cars = []

    soup = BS(urllib2.urlopen('https://www.polovniautomobili.com/auto-oglasi/pretraga?page=' + str(page_num) + '&sort=basic&city_distance=0&showOldNew=all&without_price=1'), features="html.parser")
    cars = soup.findAll('script', {'type':'application/ld+json'})

    for car_ in cars:
      car = str(car_)
      car_dict = {}
      if '"@type":"Car",' in car:

        for line in car.split('\n'):
          if ':' in line:
            splited = line.split(':')
            if 'url' not in splited[0]:
              car_dict[splited[0].replace('"', '').replace('@', '').strip()] = splited[1].replace('"', '').replace(',', '').strip()
            else:
              car_dict['url'] = line[line.index(':')+1:].replace('"', '').replace(',', '').strip()

        car_dict = missing_values_to_None(car_dict)    
        currAuto = Car(car_dict['url'], car_dict['brand'], car_dict['model'], int(car_dict['productionDate']), car_dict['fuelType'], car_dict['vehicleEngine'], int(car_dict['mileageFromOdometer'].replace('.', '').replace(' KMT','')))

        all_cars.append(currAuto)

    #saving each 25 car ads into separate file. Later we will merge all of those in one dict.
    save_to_file(all_cars, 'cars/car_' + str(page_num) + '.pkl')

def load_all_setsOf25_and_merge_and_save():

  num_of_pages = 2690
  all_cars = []
  for page_num in range(1, num_of_pages + 1):
    list_ = read_cars_array_from_file('cars/car_' + str(page_num) + '.pkl')
    all_cars = all_cars + list_

  save_to_file(all_cars, 'cars/allCars_Array.pkl')


def loadCars():

  all_cars = read_cars_array_from_file('cars/allCars_Array.pkl')

  all_cars = sorted(all_cars, key = lambda x: x.getMileageInKM(), reverse = True)

  return all_cars

def drawHistogram(all_cars, label = '', lower = 0, upper = 100):
  
  import matplotlib.pyplot as plt
  kilometraze = list(map(lambda x: x.getMileageInKM(), all_cars))

  plt.hist(kilometraze, bins = (range(10000, 400000, 10000)), rwidth = 0.8)
  plt.ylabel('Num of vehicles')
  plt.xlabel('Mileage in kms')
  plt.title(label)
  plt.axis([10000, 400000, lower, upper])
  plt.grid(True)
  plt.show()

def draw_brands(all_cars):

  import matplotlib.pyplot as plt
  brands = list(map(lambda x: x.getBrand(), all_cars))

  frequency = []

  for f in (list(set(frequency))):
    frequency.append((f, brands.count(f))) 

  frequencySorted = sorted(frequency, key = lambda u: u[1])

  top5 = (list(map(lambda x: x[0], ucestalostSorted[-5:])))

  filtered = list(filter(lambda x : False if x not in top5 else True, brands))

  plt.hist(filtered, histtype='bar', rwidth = 0.85)
  plt.xticks(range(5))
  plt.show()


def vehiclesByDecades(cars):
  
  till2000 = list(filter(lambda x : True if x.getProductionYear() <= 2000 else False, cars))
  firstDecade = list(filter(lambda x : True if x.getProductionYear() > 2000 and x.getProductionYear() <= 2010 else False, cars))
  secondeDecade = list(filter(lambda x : True if x.getProductionYear() > 2010 else False, cars))

  drawHistogram(till2000, label = 'Number of vehicles made before 2000 ordered by Mileage:', lower = 0, upper = 400)
  drawHistogram(firstDecade, label = 'Number of vehicles made between 2001 and 2010 ordered by Mileage:', lower = 0, upper = 5000)
  drawHistogram(secondeDecade, label = 'Number of vehicles made in 2011 or later ordered by Mileage:', lower = 0, upper = 2000)



if __name__ == '__main__':
	
  # go_thru_all_ads()
  # load_all_setsOf25_and_merge_and_save()
  cars = loadCars()
  vehiclesByDecades(cars)