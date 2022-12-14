import utils


data = [{
	'Country': 'Colombia',
	'Population': 500
},
{
	'Country': 'Bolivia',
	'Population': 300
}
]

keys, values = utils.get_population()
print(keys, values)

result = utils.population_by_country(data,"Colombia")
print(result)

