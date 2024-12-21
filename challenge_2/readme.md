## ingredients management
- Route: /ingredients
- Method: GET
- Description: List all ingredients
Sample Response:
```
[
	{
		"ingredient_id": 1,
		"name": "apple",
		"description": "sweet, red"
	},
	{
		"ingredient_id": 2,
		"name": "orange",
		"description": "sweet, orange"
	}
]

```

- Route: /ingredients
Method: POST
Description: Create a new ingredient
Sample Response:
```
{
	"ingredient_id": 2,
	"name": "orange",
	"description": "sweet, orange"
}

```

- Route: /ingredients/<int:ingredient_id>
- Method: GET
- Description: Get/Update/Delete a specific ingredient
Sample Response:
```
{
	"ingredient_id": 1,
	"name": "apple",
	"description": "sweet, red"
}
```

- Route: /ingredients/<int:ingredient_id>
- Method: PUT
- Description: Update a specific ingredient
Sample Response:
```
{
	"ingredient_id": 1,
	"name": "apple",
	"description": "sweet, red"
}
```

- Route: /ingredients/<int:ingredient_id>
- Method: DELETE
- Description: Delete a specific ingredient
Sample Response:
```
{
	"ingredient_id": 1,
	"name": "apple",
	"description": "sweet, red"
}

```

## save ingredients : must contain a body
- Route: /ingredients/saved
- Method: GET
- Description: Get if the ingredient is saved or not
Sample Response:
```
{
	"ingredient_id": 1,
	"quantity":0
}

```

- Route /ingredients/saved
- Method: POST
- Description: Save an ingredient
Sample Response:
```
{
	"ingredient_id": 1,
	"quantity":1
}
```

- Route /ingredients/saved/<int:ingredient_id>
- Method: PUT
- Description: Update the quantity of an ingredient
Sample Response:
```
{
	"ingredient_id": 1,
	"quantity":0
}
```

- Route /ingredients/saved/<int:ingredient_id>
- Method: DELETE
- Description: Delete the ingredient
Sample Response:
```
{
	"ingredient_id": 1,
	"quantity":0
}
```

## chatbot integration
### please create a .env file and add GEMINI_API_KEY
- Route: /ask
- Method: POST
- Description: Send a message to the chatbot: then the bot uses the current ingredients and recipes to generate a new recipe(considering the current query)
Sample Response:
```

```