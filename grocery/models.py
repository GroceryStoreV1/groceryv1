# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class customers(models.Model):
	CustomerId		  =  models.CharField(max_length = 30,primary_key = True)
	FirstName         =  models.CharField(max_length = 30)
	LastName          =  models.CharField(max_length = 30)
	Building          =  models.CharField(max_length = 30)
	Address1          =  models.CharField(max_length = 30)
	Address2          =  models.CharField(max_length = 30)
	City              =  models.CharField(max_length = 30)
	State             =  models.CharField(max_length = 30)
	PostalCode        =  models.IntegerField()
	Country           =  models.CharField(max_length = 30)
	Phone             =  models.CharField(max_length = 30)
	Email             =  models.CharField(max_length = 30)
	Password          =  models.CharField(max_length = 30)
	CreditCard        =  models.CharField(max_length = 30)
	CreditCardTypeId  =  models.CharField(max_length = 30)
	CardExpMo         =  models.CharField(max_length = 30)
	CardExpYr         =  models.CharField(max_length = 30)

	def __str__(self):
		return self.CustomerId + ',' + self.FirstName + ',' + self.LastName + ',' + self.Email

class suppliers(models.Model):
	SupplierID 		= models.CharField(max_length = 30,primary_key = True)
	CompanyName     = models.CharField(max_length = 30)
	ContactFName    = models.CharField(max_length = 30)
	ContactLName    = models.CharField(max_length = 30)
	ContactTitle    = models.CharField(max_length = 30)
	Address1        = models.CharField(max_length = 30)
	Address2        = models.CharField(max_length = 30)
	City            = models.CharField(max_length = 30)
	State           = models.CharField(max_length = 30)
	PostalCode      = models.IntegerField()
	Country         = models.CharField(max_length = 30)
	Phone           = models.CharField(max_length = 30)
	Fax             = models.CharField(max_length = 30)
	Email           = models.CharField(max_length = 30)
	WebSite         = models.CharField(max_length = 30)
	PaymentMethods  = models.CharField(max_length = 30)
	DiscountType    = models.CharField(max_length = 30)
	DiscountRate    = models.CharField(max_length = 30)
	TypeGoods       = models.CharField(max_length = 30)
	DiscountAvailable= models.CharField(max_length = 30)
	CurrentOrder    = models.CharField(max_length = 30)
	CustomerID      = models.ForeignKey(customers)
	SizeURL         = models.CharField(max_length = 30)
	Logo            = models.CharField(max_length = 30)
	Ranking         = models.CharField(max_length = 30)
	Note            = models.CharField(max_length = 30)

	def __str__(self):
		return self.SupplierID + ',' + self.CompanyName + ',' + self.CustomerID + ',' + self.Phone

class category(models.Model):
	CategoryId		= models.CharField(max_length = 30,primary_key = True)
	CategoryName    = models.CharField(max_length = 30)
	Description     = models.CharField(max_length = 30)
	Picture         = models.CharField(max_length = 30)
	Active          = models.CharField(max_length = 30)

	def __str__(self):
		return self.CategoryId + ',' + self.CategoryName

class products(models.Model):
	ProductID			   = models.CharField(max_length = 30,primary_key = True)
	SKU                    = models.CharField(max_length = 30)
	SupplierProductID      = models.CharField(max_length = 30)
	ProductName            = models.CharField(max_length = 30)
	ProductDescription     = models.CharField(max_length = 30)
	SupplierID             = models.ForeignKey(suppliers)
	CategoryID             = models.ForeignKey(category)
	QuantityPerUnit        = models.CharField(max_length = 30)
	UnitSize               = models.CharField(max_length = 30)
	UnitPrice              = models.CharField(max_length = 30)
	MSRP                   = models.CharField(max_length = 30)
	AvailableSize          = models.CharField(max_length = 30)
	AvailableColors        = models.CharField(max_length = 30)
	SizeID                 = models.CharField(max_length = 30)
	ColorID                = models.CharField(max_length = 30)
	Discount               = models.CharField(max_length = 30)
	UnitWeight             = models.CharField(max_length = 30)
	UnitsInStock           = models.CharField(max_length = 30)
	UnitsOnOrder           = models.CharField(max_length = 30)
	ReorderLevel           = models.CharField(max_length = 30)
	ProductAvailable       = models.CharField(max_length = 30)
	DiscountAvailable      = models.CharField(max_length = 30)
	CurrentOrder           = models.CharField(max_length = 30)
	Picture                = models.CharField(max_length = 30)
	Ranking                = models.CharField(max_length = 30)
	Note                   = models.CharField(max_length = 30)

	def __str__(self):
		return self.ProductID + ',' + self.SupplierID

class shippers(models.Model):
	ShipperID   = models.CharField(max_length = 30,primary_key = True)
	CompanyName = models.CharField(max_length = 30)
	Phone       = models.CharField(max_length = 30)

	def __str__(self):
		return self.ShipperID + ',' + self.CompanyName

class payment(models.Model):
	PaymentId	= models.CharField(max_length = 30,primary_key = True)
	PaymentType = models.CharField(max_length = 30)
	Allowed     = models.CharField(max_length = 30)

	def __str__(self):
		return self.PaymentId + ',' + self.PaymentType

class orders(models.Model):
	OrderID		   =  models.CharField(max_length = 30,primary_key = True)
	CustomerID     =  models.ForeignKey(customers)
	PaymentID      =  models.ForeignKey(payment)
	OrderDate      =  models.CharField(max_length = 30)
	RequiredDate   =  models.CharField(max_length = 30)
	ShipDate       =  models.CharField(max_length = 30)
	ShipperID      =  models.ForeignKey(shippers)
	Freight        =  models.CharField(max_length = 30)
	SalesTax       =  models.CharField(max_length = 30)
	Timestamp      =  models.CharField(max_length = 30)
	TransactStatus =  models.CharField(max_length = 30)
	ErrLoc         =  models.CharField(max_length = 30)
	ErrMsg         =  models.CharField(max_length = 30)
	Fulfilled      =  models.CharField(max_length = 30)
	Deleted        =  models.CharField(max_length = 30)
	Paid           =  models.CharField(max_length = 30)
	PaymentDate    =  models.CharField(max_length = 30)

	def __str__(self):
		return self.PaymentID + ',' + self.OrderID

class orderDetails(models.Model):
	OrderDetailID  =  models.CharField(max_length = 30,primary_key = True)
	OrderID        =  models.ForeignKey(orders)
	ProductID      =  models.ForeignKey(products)
	Price          =  models.CharField(max_length = 30)
	Quantity       =  models.CharField(max_length = 30)
	Discount       =  models.CharField(max_length = 30)
	Total          =  models.CharField(max_length = 30)
	Size           =  models.CharField(max_length = 30)
	Color          =  models.CharField(max_length = 30)
	Fulfilled      =  models.CharField(max_length = 30)
	BillDate       =  models.CharField(max_length = 30)
	ShipDate       =  models.CharField(max_length = 30)
	Freight        =  models.CharField(max_length = 30)
	ShipperID      =  models.ForeignKey(shippers)
	SalesTax       =  models.CharField(max_length = 30)

	def __str__(self):
		return self.ShipperID + ',' + self.ProductID




