
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
        
        hit_list = []
        
        if base_point.x == cap_point.x and base_point.z == cap_point.z:
            a = ray.dir.x**2 + ray.dir.z**2
            b = 2 * (ray.dir.x*ray.loc.x - ray.dir.x*base_point.x + ray.dir.z*ray.loc.z - ray.dir.z*base_point.z)
            c = ray.loc.x**2 + base_point.x**2 - 2*ray.loc.x*base_point.x + ray.loc.z**2 + base_point.z**2 - 2*ray.loc.z*base_point.z - radius**2
            D = b**2 - 4*a*c

            if D > 0:
                t1 = (-b - sqrt(D))/(2*a)
                t2 = (-b + sqrt(D))/(2*a)

                #if ray.at(t1).y > base_point.y and ray.at(t1).y < cap_point.y:
                normal_vect = Vec3(ray.at(t1).x - base_point.x, 0, ray.at(t1).z - base_point.z)
                h1 = Hit(t1, normal_vect.normalized(), self)
                hit_list.append(h1)
                
                #if ray.at(t2).y > base_point.y and ray.at(t2).y < cap_point.y:
                normal_vect = Vec3(ray.at(t2).x - base_point.x, 0, ray.at(t2).z - base_point.z)
                h2 = Hit(t2, normal_vect.normalized(), self)
                hit_list.append(h2)
        else:
            print('Cylinder is not aligned with y axis')
        
        return hit_list


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
