#! /usr/bin/env python3
##
# Created for EasyCTF 2018_Starman 2
# By Amos (LFlare) Ng <amosng1@gmail.com>
##
import math
import operator
import sys

DOUBLE_MAX_VALUE = sys.float_info.max


class Rectangle2D:
    """ Sample Rec2D class """
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def getX(self):
        return self._x

    def setX(self, x):
        self._x = x

    def getY(self):
        return self._y

    def setY(self, y):
        self._y = y

    def getWidth(self):
        return self._width

    def setWidth(self, width):
        self._width = width

    def getHeight(self):
        return self._height

    def setHeight(self, height):
        self._height = height

    def getMinX(self):
        return self.getX()

    def getMinY(self):
        return self.getY()

    def getMaxX(self):
        return self.getX() + self.getWidth()

    def getMaxY(self):
        return self.getY() + self.getHeight()

    def getArea(self):
        return self._width * self._height

    def getPerimeter(self):
        return 2 * (self._width + self._height)

    def containsPoint(self, x, y):
        xDist = abs(x - self._x)
        yDist = abs(y - self._y)
        return ((xDist < self._width / 2) and (yDist < self._height / 2))

    def containsRectangle(self, rectangle):
        lBound = rectangle.getX() - rectangle.getWidth() / 2
        rBound = rectangle.getX() + rectangle.getWidth() / 2
        uBound = rectangle.getY() - rectangle.getHeight() / 2
        dBound = rectangle.getY() + rectangle.getHeight() / 2
        return self.containsPoint(lBound, uBound) and self.containsPoint(rBound, dBound)

    def overlaps(self, rectangle):
        xDist = abs(self._x - rectangle.getX())
        yDist = abs(self._y - rectangle.getY())
        return xDist < (self._width + rectangle.getWidth()) / 2 and yDist < (self._height + rectangle.getHeight()) / 2

    def __contains__(self, another):
        return another.containsRectangle(self)

    def __cmp__(self, another):
        temp = self.getArea() - another.getArea()
        if temp > 0:
            return 1
        elif temp < 0:
            return -1
        else:
            return 0

    def __lt__(self, another):
        return self.getArea() < another.getArea()

    def __le__(self, another):
        return self.getArea() <= another.getArea()

    def __eq__(self, another):
        return self.getArea() == another.getArea()

    def __ne__(self, another):
        return self.getArea() != another.getArea()

    def __gt__(self, another):
        return self.getArea() > another.getArea()

    def __ge__(self, another):
        return self.getArea() >= another.getArea()


class Point:
    def __init__(self, x_init, y_init):
        self.x = x_init
        self.y = y_init

    def distance(self, p):
        return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)

    def translate(self, x, y):
        self.x += x
        self.y += y

    def rotate(self, theta):
        radius = self.distance(Point(0, 0))
        angle = math.atan2(self.y, self.x)

        # Rotate point
        angle += theta
        self.y = math.sin(angle) * radius
        self.x = math.cos(angle) * radius

class FastConvexHull:
    '''
    // From https://code.google.com/p/convex-hull/source/browse/
    //     Convex+Hull/src/algorithms/FastConvexHull.java?r=4
    // Under GPL2 license
    '''
    @staticmethod
    def rightTurn(a: Point, b: Point, c: Point):
        return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x) > 0

    @staticmethod
    def execute(points):
        xSorted = sorted(points, key=operator.attrgetter('x'))

        n = len(xSorted)

        lUpper = []
        lUpper.append(xSorted[0])
        lUpper.append(xSorted[1])

        lUpperSize = 2

        i = 2
        while i < n:
            if (lUpperSize >= len(lUpper)):
                lUpper.append(xSorted[i])
            else:
                lUpper[lUpperSize] = xSorted[i]
            lUpperSize += 1

            while (lUpperSize > 2 and not
                   FastConvexHull.rightTurn(lUpper[lUpperSize - 3], lUpper[lUpperSize - 2],
                                            lUpper[lUpperSize - 1])
                   ):
                # Remove the middle point of the three last
                lUpper[lUpperSize - 2] = lUpper[lUpperSize - 1]
                lUpperSize -= 1

            i += 1

        lLower = []
        lLower.append(xSorted[n - 1])
        lLower.append(xSorted[n - 2])

        lLowerSize = 2

        i = n - 3
        while i >= 0:
            if (lLowerSize >= len(lLower)):
                lLower.append(xSorted[i])
            else:
                lLower[lLowerSize] = xSorted[i]
            lLowerSize += 1

            while (lLowerSize > 2 and not
                   FastConvexHull.rightTurn(lLower[lLowerSize - 3],
                                            lLower[lLowerSize - 2],
                                            lLower[lLowerSize - 1])
                   ):
                # Remove the middle point of the three last
                lLower[lLowerSize - 2] = lLower[lLowerSize - 1]
                lLowerSize -= 1

            i -= 1

        result = []
        for j in range(lUpperSize):
            result.append(lUpper[j])

        for j in range(1, lLowerSize - 1):
            result.append(lLower[j])

        return result

def computeConvexHullPoints(points):
    return FastConvexHull.execute(points)

def computeCorners(points):
    convexHullPoints = computeConvexHullPoints(points)
    alignmentPointIndex = computeAlignmentPointIndex(convexHullPoints)

    r = computeAlignedBounds(convexHullPoints, alignmentPointIndex)

    alignedCorners = []
    alignedCorners.append(Point(r.getMinX(), r.getMinY()))
    alignedCorners.append(Point(r.getMaxX(), r.getMinY()))
    alignedCorners.append(Point(r.getMaxX(), r.getMaxY()))
    alignedCorners.append(Point(r.getMinX(), r.getMaxY()))

    center = convexHullPoints[alignmentPointIndex]
    angleRad = computeEdgeAngleRad(convexHullPoints, alignmentPointIndex)

    def transform_func(point):
        point.translate(center.x, center.y)
        point.rotate(angleRad)
        return point

    corners = transform(alignedCorners, transform_func)
    return corners

def computeAlignmentPointIndex(points):
    minSide = DOUBLE_MAX_VALUE
    minSideIndex = -1
    for i, p in enumerate(points):
        r = computeAlignedBounds(points, i)
        width = r.getWidth()
        height = r.getHeight()

        if (width < minSide):
            minSide = width
            minSideIndex = i
        if (height < minSide):
            minSide = height
            minSideIndex = i
    return minSideIndex


def computeEdgeAngleRad(points, index):
    i0 = index
    i1 = (i0 + 1) % len(points)
    p0 = points[i0]
    p1 = points[i1]

    dx = p1.x - p0.x
    dy = p1.y - p0.y
    angleRad = math.atan2(dy, dx)
    return angleRad


def computeAlignedBounds(points, index):
    p0 = points[index]
    translateX = -p0.x
    translateY = -p0.y
    angleRad = computeEdgeAngleRad(points, index)

    def rotate_transform(point):
        point.rotate(-angleRad)
        point.translate(translateX, translateY)
        return point

    transformedPoints = transform(points, rotate_transform)
    bounds = computeBounds(transformedPoints)
    return bounds

def transform(points, funct_affine_transform):
    transformed = list(map(funct_affine_transform, points))
    return transformed

def computeBounds(points):
    minX = DOUBLE_MAX_VALUE
    minY = DOUBLE_MAX_VALUE
    maxX = -DOUBLE_MAX_VALUE
    maxY = -DOUBLE_MAX_VALUE
    for p in points:
        x = p.x
        y = p.y
        minX = min(minX, x)
        minY = min(minY, y)
        maxX = max(maxX, x)
        maxY = max(maxY, y)
    return Rectangle2D(minX, minY, maxX - minX, maxY - minY)


def main():
    # The first line contains a single integer N,
    # representing the number of asteroids.
    N = int(input().strip())

    # The following N lines each contain two integers x_i and y_i,
    # representing the x and y coordinates of the ith asteroid.
    points = []
    for i in range(N):
        coord_str = input().strip().split(' ')
        x = coord_str[0]
        y = coord_str[1]
        p = Point(int(x), int(y))
        points.append(p)

    minObbCorners = computeCorners(points)
    reference_point = minObbCorners[0]

    # get distances between each point of rect
    distances = []
    for rect_point in minObbCorners:
        d = rect_point.distance(reference_point)
        if d > 0:
            distances.append(d)

    # print the min width
    answer = min(distances)
    print("%.6f" % answer)

if __name__ == '__main__':
    main()
