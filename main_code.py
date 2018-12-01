#no need for database
#direct querying

import urllib.request,urllib.parse,urllib.error;
import ssl;
import json;
import time;

serviceurl = "https://maps.googleapis.com/maps/api/timezone/json?";
api_key = 'BZ-------------------uY';

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

params = dict();

latitude = input("enter latitude-- ");
longitude = input("enter longitude-- ");
time = int(time.mktime(time.strptime('2000-01-01 12:34:00', '%Y-%m-%d %H:%M:%S'))) - time.timezone;

location = latitude+","+longitude;
params['location'] = location;
params['timestamp'] = (time);
params['key'] = api_key;

url = serviceurl + urllib.parse.urlencode(params);
print(url);

data = urllib.request.urlopen(url,context = ctx);
data = data.read().decode();
data = json.loads(data);

timezoneid = data["timeZoneId"];
timezonename = data["timeZoneName"];

print(timezoneid);
print(timezonename);

