from datetime import datetime
from issues import Issue

class Vote:

	def __init__(self, data=None):
		if data:
			self.issue_number = data[u'@málsnúmer']
			self.issue_category = data[u'@málsflokkur']
			self.vote_id = data[u'@atkvæðagreiðslunúmer']
			self.session_number = data[u'@þingnúmer']
			self.issue = Issue(data['mál'])
			self.date = datetime.strptime(data[u'tími'], '%Y-%m-%dT%H:%M:%S') 
			self.meeting = data[u'fundur']
			self.type_short = data[u'tegund'][u'@tegund']
			self.type = data[u'tegund']

class Votes:

	def __init__(self, data=None):
		if data:
			self.data = [Vote(v) for v in data[u'atkvæðagreiðslur'][u'atkvæðagreiðsla']]