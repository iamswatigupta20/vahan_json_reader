import json
import pandas as pd

#f=open("vahan.json")
f=open("path/to/file")
data=json.load(f)
sep='_'
f.close()


output_vahan = {}

def flatten(x, name=''):
	if isinstance(x, dict): # check if any nesting is present if so then applying flatenning the json
		for key in x:  
			flatten(x[key], name + key + sep)
	elif isinstance(x, list):
		i = 0
		if len(x) == 0: # if any empty list is there then writing just empty string
			flatten("", name )
		elif isinstance(x[0], str): #if a value contains only list of strings then joined them with comma seperated
			print(x, name)
			flatten(','.join(x), name)
		elif isinstance(x, list):
			for item in x:
			#print(item)
				flatten(item, name ) # if list nesting is there then applying flateening on json
			
	else:
		output_vahan[name[:-len(sep)]] = x
	return output_vahan




flattened_data= flatten(data["result"])
print(flattened_data)

	
df = pd.DataFrame([flattened_data])

#df.to_excel('vahan.xlsx', index=False)
df.to_excel('output/path', index=False)


