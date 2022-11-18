items = [
    {
        "product": "Camisa",
        "price":100
    },
    {
        "product": "pantalones",
        "price":300
    },
    {
        "product": "pantalones2",
        "price":200
    }
    ]

precios = list(map(lambda item: item["price"],items))
print(precios)