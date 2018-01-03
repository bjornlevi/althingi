from datetime import datetime
class MP:

	def __init__(self, data=None):
		if data:
			self.mp_id = data[u'@id']
			self.name = data[u'nafn']
			self.date = datetime.strptime(data[u'fæðingardagur'], '%Y-%m-%d') 
			self.abbreviation = data[u'skammstöfun']
			self.xml = data[u'xml']

class MPs:

	def __init__(self, data=None):
		if data:
			self.data = [MP(mp) for mp in data[u'þingmannalisti'][u'þingmaður']]