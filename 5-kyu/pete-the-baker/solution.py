def cakes(recipe, available):
    if not set(recipe.keys()).issubset(available.keys()):
        return 0

    return min([available[k] // v for k, v in recipe.items()])