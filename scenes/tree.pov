#include "colors.inc"
#include "woods.inc"

camera {
    location <0, 0, 0>
    look_at <8, 0, 0>
    up <0, 1, 0>
    angle 60
}

light_source {
    <4, 4, 0>,
    rgb <1, 1, 1>
}


cylinder {
    <6, -3, 0>, <6, -1, 0>, 0.3
    pigment {rgb <0.8, 0.4, 0.2>}
}

sphere {
    <6, -0.4, 0>, 0.5
    pigment {rgb <0, 1, 0.2>}
}

sphere {
    <6, 0.2, -0.6>, 0.6
    pigment {rgb <0, 0.8, 0.2>}
}

sphere {
    <6, 0.4, 0.4>, 0.7
    pigment {rgb <0, 1, 0.3>}
}

sphere {
    <5.8, 0.5, -0.4>, 0.5
    pigment {rgb <0, 0.95, 0.1>}
}

sphere {
    <6, 1.2, -0.3>, 0.8
    pigment {rgb <0, 1, 0.25>}
}
