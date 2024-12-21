1## ingredients management
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

## saved ingredients management
- Route: /ingredients/saved/<int:ingredient_id>
- Method: GET
- Description: Get if the ingredient is saved or not
Sample Response:
```

```
