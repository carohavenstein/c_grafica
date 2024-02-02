#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  box.py
#
#  Copyright 2023 John Coppens <john@jcoppens.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#


import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from math_3d import *
from another_thing import Thing


"""
 ____
| __ )  _____  __
|  _ \ / _ \ \/ /
| |_) | (_) >  <
|____/ \___/_/\_\

"""

class Box(Thing):
    """ El "box" está definido por dos vértices opuestos.
            Box(['corner1', vec3, 'corner2', vec3])
    """
    def __init__(self, pars):
        super().__init__(pars)


    def __str__(self):
        p0 = self.params['corner1']
        p1 = self.params['corner2']
        return f'box({p0}, {p1}'


    def intersection(self, ray):
        tnear = -float('inf')
        tfar  =  float('inf')
        p0 = self.params['corner1']
        p1 = self.params['corner2']

        # for each XY, YZ, ZX planes - check if parallel to the planes

        # YZ plane
        if ray.dir.x == 0:  # if dir.x == 0, ray is parallel to y, z
            if (ray.loc.x < self.p0.x) or (ray.loc.x > self.p1.x):
                return []

        else:
            t1 = (p0.x - ray.loc.x)/ray.dir.x
            t2 = (p1.x - ray.loc.x)/ray.dir.x
            if t1 > t2:         t1, t2 = t2, t1
            if t1 > tnear:      tnear = t1
            if t2 < tfar:       tfar = t2
            if tnear > tfar:    return []
            if tfar < 0:        return []

        # ZX plane
        if ray.dir.y == 0:  # if dir.y == 0, ray is parallel to z, y
            if (ray.loc.y < p0.y) or (ray.loc.y > p1.y):
                return []

        else:
            t1 = (p0.y - ray.loc.y)/ray.dir.y
            t2 = (p1.y - ray.loc.y)/ray.dir.y
            if t1 > t2:         t1, t2 = t2, t1
            if t1 > tnear:      tnear = t1
            if t2 < tfar:       tfar = t2
            if tnear > tfar:    return []
            if tfar < 0:        return []

        # XY plane
        if ray.dir.z == 0:  # if dir.z == 0, ray is parallel to y, x
            if (ray.loc.z < p0.z) or (ray.loc.z > p1.z):
                return []

        else:
            t1 = (p0.z - ray.loc.z)/ray.dir.z
            t2 = (p1.z - ray.loc.z)/ray.dir.z
            if t1 > t2:         t1, t2 = t2, t1
            if t1 > tnear:      tnear = t1
            if t2 < tfar:       tfar = t2
            if tnear > tfar:    return []
            if tfar < 0:        return []

        # Found intersections!!!
        return [Hit(tnear, self),
                Hit(tfar, self)]



    def callback(self, x, y):
        self.update_path()


def test_box():
    boxsize = Vec3(4)
    loc = Vec3(8, 0, 0)
    box = Box(['corner1', loc - boxsize/2, 'corner2', loc + boxsize/2])
    # ~ print(box)

    ray = Ray(Vec3(0, 0, 0), Vec3(1, 0, 0.1))
    hits = box.intersection(ray)
    for hit in hits:
        print(hit)


class MainWindow(Gtk.Window):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.connect("destroy", lambda x: Gtk.main_quit())
        self.set_default_size(400, 300)

        self.show_all()

    def run(self):
        Gtk.main()


def main(args):
    test_box()
    return 0

    mainwdw = MainWindow()
    mainwdw.run()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
