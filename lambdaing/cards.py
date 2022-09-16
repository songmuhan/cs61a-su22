from classes import *

standard_cards = [
	AICard('Matthew, Master of Mattresses', 1000, 2300),
	AICard('Max the Timely', 1700, 1600),
	AICard('Michael，the Beast of Beast', 1100, 2200),
	AICard('Jiach, the Bubbalord', 2100, 1100),
	AICard('Davis, the Broke Nomad', 1600, 1500),
	AICard('Rohan, Acolyte of the Hat Gods', 1200, 1800),
	AICard('Ben, the Brutal Barbarian', 1900, 1100),
	AICard('Elana, EECS 16B Propagandist', 1500, 1700),
	AICard('Alan, the Virtuoso', 2200, 1100),
	AICard('Theo, Amateur Charlatan', 1000, 2300),
	AICard('Alex, Banana Peeler', 1000, 2300),
	AICard('Nessia, the Loch Ness Monster', 1100, 2000),
	AICard('Apache, the Air Dominator', 1600, 1500),
	AICard('Ikun, the beauty of chicken', 2400, 1000),
	InstructorCard('Richard, Protector of Grogu ', 1900, 1500),
	InstructorCard('λaryn, λord of λambdas', 2000, 1100),
	InstructorCard('Cooper, Real Housewife', 1600, 1700),
	TACard('Aditya, Existential Hermit', 1000, 2300),
	TACard('Vibha, Destroyer of Pomegranates ', 2000, 1300),
	TACard('Anto, Turner of Cubes', 2300, 1000),
	TACard('Gabe, Vacillator Supreme', 1300, 2000),
	TACard('Ethan, The Lazy Time-traveler', 1400, 1900),
	TACard('Rachel, the Gangsta Napper', 1200, 2200),
	TACard('Mingxiao, QwQ', 1000, 2000),
	TACard('Daphne, Carrier Pigeon', 1300, 1700),
	TACard('Jordan, Pigeon Carrier', 1700, 1300),
	TACard('Charlotte, the Shawarma Shooter', 1800, 1500),
	TACard('Hailey, the Hibernating Homebody', 1200, 2100),
	TutorCard('Praj, Lord of Skies', 2000, 1200),
	TutorCard('Reuben, the Bringer of Chaos and Chicken Nuggets', 2000, 1200),
	TutorCard('Tyler, Shepherd of Lambdas', 1500, 1600),
]

standard_deck = Deck(standard_cards)
player_deck = standard_deck.copy()
opponent_deck = standard_deck.copy()
