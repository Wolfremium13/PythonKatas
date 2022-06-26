from itertools import chain, product

zero_to_nine_combinations = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')

def get_pins(observed_number: str):
    combinations_product = [product(*(zero_to_nine_combinations[int(d)])) for d in observed_number]
    flat_combinations = list(chain(*combinations_product))
    neighborhood_combinations = list(sum(flat_combinations, ()))
    return neighborhood_combinations