from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=video%20cards'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div",{"class":"item-container"})


filename = "productos.csv"
f = open(filename, "w")

headers = "brand| product_name\n"

f.write(headers)


i=0
for container in containers:
	brand = container.findAll("div",{"class":"item-branding"})
	title_container = container.findAll("a",{"class":"item-title"})
	product_name = title_container[0].text.strip()

	if brand:
		brand = brand[0].a.img['title']
	else:
		brand=product_name.split(' ')[0]

	print("brand: " + str(i) + ": " + brand)
	print("product_name: " + str(i) + "i " + product_name)

	f.write(brand + "|" + product_name +"\n")
	i=i+1

f.close()