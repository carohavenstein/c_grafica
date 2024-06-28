
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

        a = ray.dir.x**2 + ray.dir.y**2
        b = 2 * (ray.loc.x * ray.dir.x + ray.loc.y * ray.dir.y)
        c = ray.loc.x**2 + ray.loc.y**2 - radius**2
        
        D = b**2 - 4*a*c

        if D > 0:
            t1 = (-b - sqrt(D))/(2*a)
            t2 = (-b + sqrt(D))/(2*a)
            
            #z1 = ray.loc.z + t1 * ray.dir.z
            #z2 = ray.loc.z + t2 * ray.dir.z
            
            h1 = Hit(t1, (ray.at(t1)).normalized() - base_point, self)
            h2 = Hit(t2, (ray.at(t2)).normalized() - base_point, self)

            return [h1, h2]

        else:
            return []


def test_cylinder():
    cyl = Cylinder(['base_point', Vec3(8, 0, 0), 'cap_point', Vec3(8, 10, 0), 'radius', 4.2])
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
