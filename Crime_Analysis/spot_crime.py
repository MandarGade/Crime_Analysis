import json
from urllib2 import urlopen

def get_data():
	base_url="https://api.spotcrime.com/crimes.json?"
	latitude= float(raw_input("\n Enter Latitude :"))
	longitude= float(raw_input("\n Enter Longitude :"))
	radius= float(raw_input("\n Enter the radius :"))
	final_url=base_url+"lat="+str(latitude)+"&lon=-"+str(longitude)+"&radius="+str(radius)+"&key=privatekeyforspotcrimepublicusers-commercialuse-877.410.1607"
	print final_url
	web=urlopen(final_url)
	data=web.read()
#	print type(data)
	json_data=json.loads(data)
	return json_data
	
assault_count=0
arrest_count=0
burglary_count=0
robbery_count=0
theft_count=0
other_count=0

data = get_data()
address=[]
address_string=[]
count = 0
#print type(data)
#print type(data.values())
for item in data.values():
#	print len(item)
#	print item
	for value in item:
#		print value['address']
		address.append(value['address'])
#		count=count+1
		if value['type']=='Assault':
			assault_count=assault_count+1
#		if value['type']=='Arrest':
#			arrest_count=arrest_count+1
#		if value['type']=='Burglary':
#			burglary_count=burglary_count+1
#		if value['type']=='Robbery':
#			robbery_count=robbery_count+1
#		if value['type']=='Theft':
#			theft_count=theft_count+1
#		if value['type']=='Other':
#			other_count=other_count+1
#print len(address)
for val in address:
	address_string.append(str(val))

for val in address_string:
	if "&" in val:
		print val

#	if "BLOCK" in val:
#		print val
print assault_count
#print arrest_count
#print burglary_count
#print robbery_count
#print theft_count
#print other_count