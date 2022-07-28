from bs4 import BeautifulSoup
import requests
import openpyxl

url = 'https://jiji.com.gh/search?query=iphone5'
page = requests.get(url)
#print(page.text)
#print(page.ok)

soup = BeautifulSoup(page.content, 'html.parser')

# # title of the product
# content = soup.find_all('p', class_='product__description')
# #print(content)
# iphones = list()

# for item in content:
#     phone_name = item.text
#     iphones.append((phone_name))
# print(iphones)

#prices of the product
content = soup.find_all('div', class_='b-list-advert__block')
print(content)
# iphones = list()

# for item in content:
#     phone_name = item.h3.div.text
#     # phone_price= item.span.text
#     # phone_location= item.text
#     # phone_condition= item.span.text
#     iphones.append((phone_name)) 
# print(iphones)

# #location of the product
# content = soup.find_all('p', class_='product__location')
# #print(content)
# iphones = list()

# for item in content:
#     phone_location= item.text
#     iphones.append((phone_location)) 
# print(iphones)

# #condition of the product
# content = soup.find_all('div', class_='product__tags flex wrap')
# iphones = list()

# for item in content:
#     phone_condition= item.span.text 
#     iphones.append((phone_condition)) 
# print(iphones)

# wb = openpyxl.Workbook()
# sheet = wb.active
# sheet.title = 'Tonaton Electronics'
# sheet['A1'] = 'Names of Iphones in Stock'
# sheet['B1'] = 'Prices'
# sheet['C1'] = 'Location'
# sheet['D1'] = 'Current Condition'

# for  mobile_phones in iphones:
#     sheet.append(mobile_phones)

# wb.save('web_scrapping_from_tonaton_Ghana.xlsx')
