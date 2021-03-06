import json
import requests
from .models import *

def cookieCart(request):

	#Create empty cart for now for non-logged in user
	try:
		cart = json.loads(request.COOKIES['cart'])
		#print('CART:', cart)
	except:
		cart = {}
		#print('CART:', cart)

	items = []
	order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
	cartItems = order['get_cart_items']

	for i in cart:
		#We use try block to prevent items in cart that may have been removed from causing error
		try:	
			if(cart[i]['quantity']>0): #items with negative quantity = lot of freebies  
				cartItems += cart[i]['quantity']

				product = Product.objects.get(id=i)
				total = (product.price * cart[i]['quantity'])

				order['get_cart_total'] += total
				order['get_cart_items'] += cart[i]['quantity']

				item = {
				'id':product.id,
				'product':{'id':product.id,'name':product.name, 'price':product.price, 
				'imageURL':product.imageURL}, 'quantity':cart[i]['quantity'],
				'digital':product.digital,'get_total':total,
				}
				items.append(item)

				if product.digital == False:
					order['shipping'] = True
		except:
			pass
			
	return {'cartItems':cartItems ,'order':order, 'items':items}

def cartData(request):
	if request.user.is_authenticated:
		customer = request.user.customer

		
		#Create a new order if the customer's previous orders have all been completed.
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		#This is how I can track if an order was not processed in the correct way.


		items = order.orderitem_set.all()
		cartItems = order.get_cart_items
	else:
		cookieData = cookieCart(request)
		cartItems = cookieData['cartItems']
		order = cookieData['order']
		items = cookieData['items']

	return {'cartItems':cartItems ,'order':order, 'items':items}
	
def guestOrder(request, data):
	name = data['form']['name']
	email = data['form']['email']

	cookieData = cookieCart(request)
	items = cookieData['items']

	customer, created = Customer.objects.get_or_create(
			email=email,
			)
	customer.name = name
	customer.save()

	order = Order.objects.create(
		customer=customer,
		complete=False,
		)

	for item in items:
		product = Product.objects.get(id=item['id'])
		orderItem = OrderItem.objects.create(
			product=product,
			order=order,
			quantity=(item['quantity'] if item['quantity']>0 else -1*item['quantity']), # negative quantity = freebies
		)
	return customer, order

def userCartData(request):
	customer = request.user.customer
	order, created = Order.objects.get_or_create(customer=customer, complete=False)
	# items = order.orderitem_set.all()
	items = order.orderitem_set.order_by('id')
	cartItems = order.get_cart_items

	return {'cartItems':cartItems ,'order':order, 'items':items}

def guestCartData(request):

	#Create empty cart for now for non-logged in user
	try:
		cart = json.loads(request.COOKIES['cart'])
		#print('CART:', cart)
	except:
		cart = {}
		#print('CART:', cart)

	items = []
	order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
	cartItems = order['get_cart_items']

	for i in cart:
		#We use try block to prevent items in cart that may have been removed from causing error
		try:	
			if(cart[i]['quantity']>0): #items with negative quantity = lot of freebies  
				cartItems += cart[i]['quantity']

				product = Product.objects.get(id=i)
				total = (product.price * cart[i]['quantity'])

				order['get_cart_total'] += total
				order['get_cart_items'] += cart[i]['quantity']

				item = {
				'id':product.id,
				'product':{'id':product.id,'name':product.name, 'price':product.price, 
				'imageURL':product.imageURL}, 'quantity':cart[i]['quantity'],
				'digital':product.digital,'get_total':total,
				}
				items.append(item)

				if product.digital == False:
					order['shipping'] = True
		except:
			pass
			
	return {'cartItems':cartItems ,'order':order, 'items':items}

def getAccessToken(request):
	url = "https://api-m.sandbox.paypal.com/v1/oauth2/token"
	headers = {
				'Authorization': 'Basic QWFGenpIc3JiS1d3Y003NTZsd0hmN3RQamlCMjhRdVl4WXcxTlQ2cFBQaVlxcWZXbWVJa1ZsVDNQQkVJZ0xKRm9RWG81UXdYNzdEZ1FjLWo6RUJyczVwSWREOEh1TkdZRU5mWWd5TzZqY2FkUEFqVU04WjZnZGZvYm1Vek9XUGM3QU1NanBFXzJkV3VKSjB2anhIUWdMdEs4Snd5Mm1tUEY=',

				'Content-Type': 'application/x-www-form-urlencoded'
				}
	payload='grant_type=client_credentials'
	response = requests.request("POST", url, headers = headers, data = payload)
	response_json = response.json()
	accessToken = response_json['access_token']
	return accessToken

quantity_choices = {
  '1':'One',
  '2':'Two',
  '3':'Three',
  '4':'Four',
  '5':'Five',
  '6':'Six',
  '7':'Seven',
  '8':'Eight',
  '9':'Nine',
  '10':'Ten',
}