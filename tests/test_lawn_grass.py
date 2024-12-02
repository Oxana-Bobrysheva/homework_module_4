from src.lawn_grass import LawnGrass


def test_LawnGrass_init(grass_1):
    assert grass_1.name == "Cleverance"
    assert grass_1.quantity == 23
    assert grass_1.colour == "Greenish"
    assert grass_1.description == "For sports ground"
    assert grass_1.price == 250
    assert grass_1.country == "Russia"


def test_LawnGrass_adding():
    grass_2 = LawnGrass("KIWI", "512GB, Gray space", 245, 8, 98.2, "15", "Gray space")
    grass_3 = LawnGrass("Roxy", "1024GB, Синий", 357, 14, 90.3, "Note 11", "Синий")
    grass_sum = grass_2 + grass_3
    assert grass_sum == 6958
