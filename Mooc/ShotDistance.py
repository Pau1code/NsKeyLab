from math import pi, sin, cos, radians


def main():
    angle, vel, h0, time = getInput()
    xpos, ypos = 0, h0
    xvel, yvel = getXYComponents(vel, angle)
    while ypos >= 0:
        xpos, ypos, yvel = updatePosition(time, xpos, ypos, xvel, yvel)
    print("Distance traveled : {0: 0.1f} meters.".format(xpos))


def getInput():
    angle = eval(input("Enter the launch angle (in degrees):"))
    vel = eval(input("Enter the initial velocity (in meters/sec):"))
    h0 = eval(input("Enter the initial height(in meters):"))
    time = eval(input("Enter the time interval:"))
    return angle, vel, h0, time


def getXYComponents(vel, angle):
    theta = radians(angle)
    xvel = vel * cos(theta)
    yvel = vel * sin(theta)
    return xvel, yvel


def updatePosition(time, xpos, ypos, xvel, yvel):
    xpos = xpos + xvel * time
    yvel1 = ypos - time * 9.8
    ypos = ypos + time * (yvel + yvel1) / 2
    yvel = yvel1
    return xpos, ypos, yvel


if __name__ == '__main__':
    main()

