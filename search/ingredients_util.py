import pandas as pd



def get_ingredient_cluster(ingredient_string):
    df = pd.read_csv("/Users/celeste/code/HangryGoat/data/parsed/ingredients.csv")
    d = df['ingredient'].apply(lambda x: x.split(",")).explode("ingredients").apply(lambda x: x.replace("'", "").split("_")).apply(pd.Series)
    # print(d.head())
    idx = df['ingredient'].apply(lambda x: x.split(",")).explode("ingredients").values
    d = d.set_index(idx)
    filtered = d.filter(like=ingredient_string, axis = 0).drop_duplicates().head()


    final_ingredients = [ingredient_string]

    for i in filtered.values:
        if ingredient_string in i:
            try:
                final_ingredients.append(" ".join(list(i)))
            except:
                pass

    return final_ingredients


if __name__ == '__main__':
    print(get_ingredient_cluster("lemon"))

    print(get_ingredient_cluster("stalks_lemongrass"))
    print(get_ingredient_cluster("cloves"))

    print(get_ingredient_cluster("garlic"))
    print(get_ingredient_cluster("garlic powder"))


