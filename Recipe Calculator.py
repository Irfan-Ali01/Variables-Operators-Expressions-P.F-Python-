recipe_ingredients = {"flour": 500, "sugar": 100, "butter": 80, "eggs": 8, "milk": 100}
recipe_amounts = {"grams": ["flour", "sugar", "butter"], "units": ["eggs"], "milliliters": ["milk"]}
servings = 5
def adjust_quantities(ingredients, amounts, servings):
    adjusted_quantities = {}
    for ingredient, amount in ingredients.items():
        quantity_per_serving = amount / servings
        adjusted_quantity = quantity_per_serving * servings
        adjusted_quantity = round(adjusted_quantity)
        adjusted_quantities[ingredient] = adjusted_quantity
    return adjusted_quantities
adjusted_quantities = adjust_quantities(recipe_ingredients, recipe_amounts, servings)
print(f"Adjusted quantities for {servings} servings:")
for ingredient, quantity in adjusted_quantities.items():
    if ingredient in recipe_amounts["grams"]:
        unit = " g"
    elif ingredient in recipe_amounts["units"]:
        unit = ""
    elif ingredient in recipe_amounts["milliliters"]:
        unit = " ml"
    print(f"{ingredient}: {quantity}{unit}")