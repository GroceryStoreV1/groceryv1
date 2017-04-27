from django.http import HttpResponse,HttpResponseRedirect

from django.template import loader,RequestContext
from django.http import Http404
from django.shortcuts import render,get_object_or_404,render_to_response
from django.utils import timezone
from django.core.urlresolvers import reverse
import datetime 
import xlrd
price = 2
def index(request):

	# today = datetime.datetime.now().date()
	# daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
   	return render(request, "grocery/index.html")
   # template = loader.get_template('grocery/index.html')
   # return render(request, 'grocery/index.html', {"today" : today, "days_of_week" : daysOfWeek})

def vegetables(request):
	price = xlsFile() 
	return render(request, 'grocery/vegetables.html',{'vegPrice':price})

def products(request):
	return render(request, 'grocery/products.html')

def drinks(request):
	return render(request, 'grocery/drinks.html')

def kitchen(request):
	return render(request, 'grocery/kitchen.html')

def shortCodes(request):
	return render(request, 'grocery/short-codes.html')

def frozen(request):
	return render(request, 'grocery/frozen.html')

def pet(request):
	return render(request, 'grocery/pet.html')

def bread(request):
	return render(request, 'grocery/bread.html')

def household(request):
	return render(request, 'grocery/household.html')

def xlsFile():
	workbook = xlrd.open_workbook('sample.xls')
	worksheet = workbook.sheet_by_name('Users')
	num_rows = worksheet.nrows 
	num_cells = worksheet.ncols 

	worksheet_Orders = workbook.sheet_by_name('Product')
	orders_rows = worksheet_Orders.nrows
	orders_cells = worksheet_Orders.ncols 

	# worksheet_Orders = workbook.sheet_by_name('Orders')
	# orders_rows = worksheet_Orders.nrows
	# orders_cells = worksheet_Orders.ncols 

	orders = []
	ordersName = []
	ordersDist = {}
	finalOrder = []

	for i in range(0,13):
		orders.append(worksheet_Orders.cell(i,7).value)
		ordersName.append(worksheet_Orders.cell(i,3).value)
	print ordersName

	for j in range(1,13):
		price_tag = 'vegPrice'+str(j)
		print 'price_tag: ' + price_tag
		ordersDist[price_tag] = orders[j]
		print 'orders merge: ' + str(orders[j])

	finalOrder.append(ordersDist)
	# return orders
	print 'rows: ' +  str(num_rows), 'cells: ' + str(num_cells)
	store = []
	storeDict = {}
	for i in range(num_rows):
	# for j in range(num_cells):
		store.append(worksheet.cell(i,2).value)	

	print 'store value: ' + str(store)
	for x in range(1,13):
		name = 'vegPrice'+str(x)
		print 'name: ' + name
		storeDict[name]=store[x]
		print 'store merge: ' + str(store[x])

	finalStore = []
	finalStore.append(storeDict)
	return finalOrder

	# global price
	# price = worksheet.cell(5,2).value
	# print price
	# return price