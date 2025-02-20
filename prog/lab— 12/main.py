def analyze_car_exports(car_brands, exports):
    delivered_to_all = set(car_brands)
    for country, brands in exports.items():
        delivered_to_all.intersection_update(brands)

    delivered_to_some = set()
    for country, brands in exports.items():
        delivered_to_some.update(brands)

    not_delivered = set(car_brands) - delivered_to_some

    return delivered_to_all, delivered_to_some, not_delivered


car_brands = {"Toyota", "Honda", "Ford", "BMW", "Tesla"}
exports = {
    "Germany": {"Toyota", "BMW", "Tesla"},
    "USA": {"Ford", "Tesla", "Honda"},
    "Japan": {"Toyota", "Honda"},
}

delivered_to_all, delivered_to_some, not_delivered = analyze_car_exports(car_brands, exports)

print("Марки, доставленные во все страны:", delivered_to_all)
print("Марки, доставленные в некоторые страны:", delivered_to_some)
print("Марки, не доставленные ни в одну страну:", not_delivered)