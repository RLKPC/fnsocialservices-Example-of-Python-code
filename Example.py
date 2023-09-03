import requests
import json

class Api:

    def init(self):
        self.api_url = 'https://fnsocialservices.com/api/v2' # API URL
        self.api_key = '' # Your API key

    def order(self, data): # add order
        data.update({'key': self.api_key, 'action': 'add'})
        return requests.post(self.api_url, data=data).json()

    def status(self, order_id): # get order status
        data = {'key': self.api_key, 'action': 'status', 'order': order_id}
        return requests.post(self.api_url, data=data).json()

    def multiStatus(self, order_ids): # get multiple order status
        data = {'key': self.api_key, 'action': 'status', 'order': ','.join(str(x) for x in order_ids)}
        return requests.post(self.api_url, data=data).json()

    def services(self): # get services
        data = {'key': self.api_key, 'action': 'services'}
        return requests.post(self.api_url, data=data).json()

    def balance(self): # get balance
        data = {'key': self.api_key, 'action': 'balance'}
        return requests.post(self.api_url, data=data).json()


Examples
api = Api()

services = api.services() # return all services

balance = api.balance() # return user balance

add order
order = api.order({'service': 1, 'link': 'http://example.com/test', 'quantity': 100}) # Default
order = api.order({'service': 1, 'link': 'http://example.com/test', 'comments': "good pic\ngreat photo\n:)\n;)"}) # Custom Comments
order = api.order({'service': 1, 'link': 'http://example.com/test', 'quantity': 1000, 'username': "test"}) # Mentions User Followers
order = api.order({'service': 1, 'link': 'http://example.com/test'}) # Package
order = api.order({'service': 1, 'link': 'http://example.com/test', 'quantity': 100, 'runs': 10, 'interval': 60}) # Drip-feed
order = api.order({'service': 1, 'username': 'username', 'min': 100, 'max': 110, 'posts': 0, 'delay': 30, 'expiry': '11/11/2019'}) # Subscriptions
order = api.order({'service': 1, 'link': 'http://example.com/test', 'quantity': 100, 'username': "test"}) # Comment Likes
status = api.status(order.order) # return status, charge, remains, start count, currency
statuses = api.multi_status([1, 2, 3]) # return orders status, charge, remains, start count, currency
