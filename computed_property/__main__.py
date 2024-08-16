from circle import Circle
from vector import Vector


def run():
    print(10 * "-" + " Test Vector " + 10 * "-")

    v = Vector(9, 2, 6)
    print(v.magnitude())
    v.color = "red"
    print(v.magnitude())
    v.y = 18
    print(v.magnitude())
    help(v)

    print(10 * "-" + " Test Circle " + 10 * "-")
    circ = Circle()
    print(circ.diameter)  # 2
    circ.diameter = 3
    print(circ.radius)  # 1.5
    del circ.diameter
    print(circ.radius)  # 0
    help(circ)


if __name__ == "__main__":
    run()
