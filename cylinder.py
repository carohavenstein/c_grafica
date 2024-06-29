
from pdb import set_trace as st

from math_3d import *
from another_thing import Thing

class Cylinder(Thing):
    """
        Cylinder esta definido por 2 puntos y un radio
        Cylinder(['base_point', vec3, 'cap_point', vec3, 'radius', float])
    """

    def __init__(self, pars = []):
        super().__init__(pars)

    def intersection(self, ray):
        base_point = self.params['base_point']
        cap_point = self.params['cap_point']
        radius = self.params['radius']

        a = ray.dir.x**2 + ray.dir.z**2
        b = 2 * (ray.loc.x * ray.dir.x + ray.loc.z * ray.dir.z)
        c = ray.loc.x**2 + ray.loc.z**2 - radius**2
        
        D = b**2 - 4*a*c

        #print('a: ', a)
        #print('b: ', b)
        #print('c: ', c)
        #print('D: ', D)

        if D > 0:
            t1 = (-b - sqrt(D))/(2*a)
            t2 = (-b + sqrt(D))/(2*a)
            
            print('t1: ', t1)
            print('t2: ', t2)
            #z1 = ray.loc.y + t1 * ray.dir.y
            #z2 = ray.loc.y + t2 * ray.dir.y
            
            print('ray.at(t1): ', ray.at(t1))
            print('ray.at(t2): ', ray.at(t2))

            h1 = Hit(t1, (ray.at(t1)).normalized(), self)
            h2 = Hit(t2, (ray.at(t2)).normalized(), self)
            
            return [h1, h2]
        else:
            return []


def test_cylinder():
    cyl = Cylinder(['base_point', Vec3(8, -2, 0), 'cap_point', Vec3(8, 2, 0), 'radius', 4.2])
    print(cyl)

    ray = Ray(Vec3(0, 0, 0), Vec3(1, 0, 0))
    hits = cyl.intersection(ray)
    for hit in hits:
        print(hit)


def main(args):
    test_cylinder()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
