import time, BAC0 
from influxdb import InfluxDBClient

def get_values(bacnet, influx):
	reading13 = bacnet.read('192.168.0.23 analogInput 13 presentValue')
	# print(reading13)
	reading26 = bacnet.read('192.168.0.23 analogInput 26 presentValue')
	# print(reading26)
	reading12 = bacnet.read('192.168.0.23 analogInput 12 presentValue')
	# print(reading12)
	reading14 = bacnet.read('192.168.0.23 analogInput 14 presentValue')
	# print(reading14)
	reading15 = bacnet.read('192.168.0.23 analogInput 15 presentValue')
	# print(reading15)
	reading16 = bacnet.read('192.168.0.23 analogInput 16 presentValue')
	# print(reading16)
	reading25 = bacnet.read('192.168.0.23 analogInput 25 presentValue')
	# print(reading25)
	reading11 = bacnet.read('192.168.0.23 analogInput 11 presentValue')
	# print(reading11)
	reading9 = bacnet.read('192.168.0.23 analogInput 9 presentValue')
	# print(reading9)
	reading1 = bacnet.read('192.168.0.23 pulseConverter 1 presentValue')
	# print(reading1)
	reading2 = bacnet.read('192.168.0.23 pulseConverter 2 presentValue')
	# print(reading2)

	json_body = [
		{
			"measurement": "TOA Temp Ext",
				"fields": {
					"value": reading13
				}
		},
		{
			"measurement": "RaySol Ray Solaire",
			"fields": {
				"value": reading26
			}
		},
		{
			"measurement": "TBo Temp Bruleur",
			"fields": {
				"value": reading12
			}
		},
		{
			"measurement": "Tcol Temp Collecteur Sol",
			"fields": {
				"value": reading14
			}
		},
		{
			"measurement": "TTnkBtm Temp Basse Ballon ECS",
			"fields": {
				"value": reading15
			}
		},
		{
			"measurement": "TTnkTop Temp Haute Ballon ECS",
			"fields": {
				"value": reading16
			}
		},
		{
			"measurement": "TreSol Temp retour solaire",
			"fields": {
				"value": reading25
			}
		},
		{
			"measurement": "TR affichage Ambiante",
			"fields": {
				"value": reading11
			}
		},
		{
			"measurement": "TFL Temp dep chauffage",
			"fields": {
				"value": reading9
			}
		},    
		{
			"measurement": "Cpt Eau",
			"fields": {
				"value": reading1
			}
		},
		{
			"measurement": "Cpt Elec",
			"fields": {
				"value": reading2
			}
		}
	]
	influx.write_points(json_body)

def main():
	bacnet = BAC0.connect() 
	bacnet.whois()
	client = InfluxDBClient(host='192.168.0.32', port=8086, database='InfluxDB_BACnet')
	while True:
		get_values(bacnet, client)
		time.sleep(60)

if __name__ == '__main__':
	main()
