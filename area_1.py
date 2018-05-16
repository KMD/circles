import unittest

class Area:

    def __init__(self, lat, long, radius, id):
        self.lat = lat
        self.long = long
        self.radius = radius
        self.id = id

    def is_in_area(self, lat, long):
        mod = ((self.lat -  lat) ** 2 + (self.long - long) ** 2) ** (1 / 2)
        if mod > self.radius:
            return False
        else:
            return True

class AreaList:

    areas = []

    def batch_create(self, areas):
        for area in areas:
            a = Area(area[0], area[1], area[2], area[3])
            self.areas.append(a)
    
    def query(self, lat, long):
        r = []
        for area in self.areas:
            if area.is_in_area(lat, long):
                r.append(area.id)
        return r


class TestArea(unittest.TestCase):

    def test_isinarea(self):
        x = Area(1.0, 1.0, 2.0, 0)
        self.assertTrue(x.is_in_area(1.0, 1.0))
    
    def test_isinareanegative(self):
        x = Area(-1.0, -1.0, 2.0, 0)
        self.assertTrue(x.is_in_area(0.3, 0.3))

    def test_isnotinarea(self):
        x = Area(1.0, 1.0, 2.0, 0)
        self.assertFalse(x.is_in_area(3.0, 2.0))

    def test_isnotinareanegative(self):
        x = Area(-1.0, -1.0, 2.0, 0)
        self.assertFalse(x.is_in_area(-3.0, -2.0))


class TestAreaList(unittest.TestCase):

    def test_querymethod(self):
        al = AreaList()
        al.batch_create([(1.0, 1.0, 2.0, 0),(3.0, 1.0, 1.0, 1),(13.0, 12.0, 10.0, 2),(5.0, 4.0, 10.0, 3)])
        self.assertListEqual(sorted([0,3]), sorted(al.query(1.0, 1.0)))

if __name__ == '__main__':
    unittest.main()