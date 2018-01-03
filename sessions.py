import xmltodict
import requests

class Session:
	def __init__(self, session_number, session_data=None):
		if session_data:
			self.data = [x for x in session_data[u'löggjafarþing'][u'þing'] if x[u'@númer'] == str(session_number)][0]
		else:
			url = 'http://www.althingi.is/altext/xml/loggjafarthing/?lthing='+str(session_number)
			response = requests.get(self.url)
			data = xmltodict.parse(response.text)
			self.data = [x for x in data if x[u'@númer'] == str(session_number)][0]
		self.number = self.data[u'@númer']
		self.session_start = self.data[u'þingsetning']
		self.session_end = self.data[u'þinglok']
		self.issues = self.data[u'yfirlit'][u'þingmálalisti']
		self.documents = self.data[u'yfirlit'][u'þingskjalalisti']
		self.votes = self.data[u'yfirlit'][u'atkvæðagreiðslur']
		self.mps = self.data[u'yfirlit'][u'þingmannalisti']
		self.speeces = self.data[u'yfirlit'][u'ræðulisti']
		self.commitees = self.data[u'yfirlit'][u'nefndir']
		self.comments = self.data[u'yfirlit'][u'erindi']
		self.submitters = self.data[u'yfirlit'][u'sendendurerinda']

class Sessions:
	url = 'http://www.althingi.is/altext/xml/loggjafarthing/'
	url_current = 'http://www.althingi.is/altext/xml/loggjafarthing/yfirstandandi/'
	def __init__(self):
		response = requests.get(self.url)
		self.data = xmltodict.parse(response.text)		

	def session_numbers(self):
		return [x[u'@númer'] for x in self.data[u'löggjafarþing'][u'þing']]

	def get_session(self, session_number):
		return Session(session_number, self.data)
