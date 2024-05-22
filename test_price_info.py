import price_info as info
def test_cost_shopping():
    result = info.total_cost_shopping()
    assert(result == 46.75)

def test_cost_of_fruit():
    result = info.cost_of_fruits('orange', 10)
    assert(result == 14.0)
