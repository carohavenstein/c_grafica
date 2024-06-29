#include "colors.inc"
#include "woods.inc"

camera {
    location <0, 3, 0>
    look_at <10, 0, 0>
    up <0, 1, 0>
    angle 60
}

light_source {
    <4, 6, 9>,
    rgb <1, 1, 1>
}


cylinder {
    <8, -2, 0>, <8, 2, 0>, 1
    pigment {rgb <0.2, 0, 1>}
}