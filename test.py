from sessions import Sessions
import pprint

pp = pprint.PrettyPrinter(indent=4)
s = Sessions()
pp.pprint(s.get_session(146).votes)