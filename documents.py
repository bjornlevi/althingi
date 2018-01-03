from datetime import datetime

class Document:

	def __init__(self, data=None):
		if data:
			self.document_number = data[u'@skjalsnúmer']
			self.session_number = data[u'@þingnúmer']
			self.date = datetime.strptime(data[u'útbýting'], '%Y-%m-%d %H:%M') 
			self.document_type = data[u'skjalategund']
			self.xml = data[u'slóð'][u'xml']

class Documents:

	def __init__(self, data=None):
		if data:
			self.data = [Document(d) for d in data[u'þingskjöl'][u'þingskjal']]