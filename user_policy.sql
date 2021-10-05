CREATE TABLE user_policy (
	"policy" VARCHAR(12) UNIQUE PRIMARY KEY NOT NULL,
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL,
	drivers jsonb NOT NULL,
	vehicles jsonb NOT NULL,
	effective_date VARCHAR(10) NOT NULL,
	expiration_date VARCHAR(10) NOT NULL
);

INSERT INTO user_policy ("policy",first_name,last_name,drivers,vehicles,effective_date,expiration_date) VALUES (
	'ILP0001',
	'Mack',
	'Norris',
	'[
		{
		 "first_name": "Mack",
		 "last_name": "Norris",
		 "license": "TYFE999",
		 "gender": "M",
		 "birth_date": "1988-02-12"
		},
		{
		"first_name": "Lolli",
		"last_name": "Noobert",
		"license": "WED2211",
		"gender": "F",
		"birth_date": "1979-12-08"
		}
	]',
	'[
		{
		"year": "1986",
		"make": "Pontiac",
		"model": "Grand Am",
		"vin": "1G2NV27L4GC692652",
		"color": "Black"
		}
	]',
	'2021-01-01',
	'2022-01-01'
);