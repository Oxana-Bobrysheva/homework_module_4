from src.smartphone import Smartphone


def test_smartphone_init(smartphone_1):
    assert smartphone_1.name == 'Samsung Galaxy S23 Ultra'
    assert smartphone_1.quantity == 5
    assert smartphone_1.colour == "Серый"
    assert smartphone_1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_1.price == 180000.0
    assert smartphone_1.efficiency == 95.5
    assert smartphone_1.memory == 256
    assert smartphone_1.model == "S23 Ultra"

def test_smartphone_adding():
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8,
                             98.2, "15", 512, "Gray space")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14,
                             90.3, "Note 11", 1024, "Синий")
    smartphone_sum = smartphone2 + smartphone3
    assert smartphone_sum == 2114000.0

