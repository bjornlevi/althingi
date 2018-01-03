import xmltodict
import requests

class Issue:

	def __init__(self, data=None):
		if data:
			self.issue_number = data[u'@málsnúmer']
			self.session_number = data[u'@þingnúmer']
			self.category = data[u'@málsflokkur']
			self.name = data[u'málsheiti']
			self.xml = data[u'xml']
			#try:
				#self.issue_type = data[u'málstegund'][u'heiti']
				#self.issue_type_short = data[u'málstegund'][u'@málstegund']
			#except:
				#response = requests.get(self.xml)
				#issue_data = xmltodict.parse(response.text)
				#self.issue_type = issue_data[u'þingmál'][u'mál'][u'málstegund'][u'heiti']
				#self.issue_type_short = issue_data[u'þingmál'][u'mál'][u'málstegund'][u'@málstegund']

class Issues:

	def __init__(self, data=None):
		if data:
			self.data = [Issue(i) for i in data[u'málaskrá'][u'mál']]