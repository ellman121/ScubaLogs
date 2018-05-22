# Standard Lib Imports
import time
import os
import json
from datetime import date

# Local imports
import ParseFuncs


def gatherData():
	dive = {}
	raw_dive = [{
	 'prompt': 'Dive Number: ',
	 'data': None,
	 'parse': None
	}, {
	 'prompt': 'Location: ',
	 'data': None,
	 'parse': None
	}, {
	 'prompt': 'Time Under: ',
	 'data': None,
	 'parse': None
	}, {
	 'prompt': 'Avg Depth: ',
	 'data': None,
	 'parse': ParseFuncs.parseMeters
	}, {
	 'prompt': 'Max Depth: ',
	 'data': None,
	 'parse': ParseFuncs.parseMeters
	}, {
	 'prompt': 'Visibility: ',
	 'data': None,
	 'parse': None
	}, {
	 'prompt': 'Water Temp: ',
	 'data': None,
	 'parse': ParseFuncs.parseCelcius
	}, {
	 'prompt': 'Weight: ',
	 'data': None,
	 'parse': ParseFuncs.parseKilos
	}, {
	 'prompt': 'Air Type: ',
	 'data': None,
	 'parse': None
	}, {
	 'prompt': 'Wetsuit: ',
	 'data': None,
	 'parse': None
	}, {
	 'prompt': 'Divers: ',
	 'data': None,
	 'parse': None
	}]

	for _, datum in enumerate(raw_dive):
		inpt = ''
		while inpt == '':
			inpt = input(datum['prompt'])

		if datum['parse'] != None:
			inpt = datum['parse'](inpt)

		dive[datum['prompt'].strip()] = inpt.strip()

	return dive

def saveData(dive):
	base_name = date.today().strftime("%Y.%m.%d")
	os.chdir('./LogBook/')
	isSameDayDive = lambda f: f.find(base_name) != -1
	files = [f for f in os.listdir('.') if os.path.isfile(f) and isSameDayDive(f)]

	if len(files) == 0:
		with open(base_name + '.json', 'w') as outfile:
			json.dump(dive, outfile, skipkeys=True, indent=2)

	elif len(files) == 1:
		os.rename(base_name + '.json', base_name + '.1.json')
		with open(base_name + '.2.json', 'w') as outfile:
			json.dump(dive, outfile, skipkeys=True, indent=2)

	else:
		with open(base_name + '.' + str(len(files) + 1) + '.json', 'w') as outfile:
			json.dump(dive, outfile, skipkeys=True, indent=2)


def main():
	dive = gatherData()
	saveData(dive)


if __name__ == '__main__':
	main()
