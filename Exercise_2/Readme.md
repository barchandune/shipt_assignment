2. Locate one bug or bad workflow within the app.

a. Title : item count does not match search result count

	Reproduction steps : 
	1. Login to shipt.com
	2. Select a store (in my case I used Target)
	3. Select Category > Deli
	4. It shows 164 results but if you add count from all the sub categories it does not match i.e. (41 + 1 + 158 + 1)

	Deli Counter (41)
	Party Trays & Dips (1)
	Prepared Meals (158)
	Specialty Deli Cheeses (1)

b. Screenshots : See "Search_Results_item_count_wrong_1" and others.

c. Why and How needs to be corrected - 
	i. Why - user thinks there are 164 items to select from but there are more options.
	ii. How - I checked response of "https://api.shipt.com/search/v2/search/?bucket_number=19&white_label_key=shipt" and looks like problem is in backend (no problem with the front end) as item count recevied in response matches with what is displayed to the user on front end.

	"hierarchical_categories.level_1":{

"Dairy":16,
"Deli":164,
"Frozen":1,
"Meat \u0026 Seafood":39,
"Pantry":8,
"Snacks":19
},

"hierarchical_categories.level_2":{

"Dairy \u003e Cheese":16,

"Deli \u003e Deli Counter":41,
"Deli \u003e Party Trays \u0026 Dips":1,
"Deli \u003e Prepared Meals":158,
"Deli \u003e Specialty Deli Cheeses":1,

"Frozen \u003e Apps \u0026 Sides":1,
"Frozen \u003e Frozen Meals":1,

"Meat \u0026 Seafood \u003e Beef":2,
"Meat \u0026 Seafood \u003e Lunch Meat":35,
"Meat \u0026 Seafood \u003e Pork":1,
"Meat \u0026 Seafood \u003e Poultry":3,

"Pantry \u003e Canned Goods":1,
"Pantry \u003e Condiments \u0026 Dressings":5,
"Pantry \u003e Gluten Free Pantry":2,

"Snacks \u003e Chips":12,
"Snacks \u003e Crackers":1,
"Snacks \u003e Dips \u0026 Spreads":18
},

d. Steps to report the issue : Since severity of this issue is P2 so I would put this in backlog but at the same time would like to priortize it.

e. Priority : P2

f. Reproducibility rate : 100% for some items example if you select "Deli" but at the same time does not happen when you select others like "Deli counter"