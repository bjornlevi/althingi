from sessions import Sessions
import pprint

pp = pprint.PrettyPrinter(indent=4)
s = Sessions()
pp.pprint(s.get_session(148).get_session_mps())