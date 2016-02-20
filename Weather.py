import urllib2
import json


url_base =  'http://api.wunderground.com/api/e1fde55153190b2a/'
extension =  'geolookup/conditions/q/IA/Cedar_Rapids.json'
url_full = url_base + extension


import urllib2
import json
f = urllib2.urlopen(url_full)
json_string = f.read()
parsed_json = json.loads(json_string)
print parsed_json
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
print "Current temperature in %s is: %s" % (location, temp_f)
f.close()