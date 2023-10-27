from collections import deque
from vector import *


SQRT_2 = math.sqrt(2)


def pow2(a):
    return a * a


# 树结构，用于回溯路径
class Vector2Node:
    pos = None  # 当前的x、y位置
    frontNode = None  # 当前节点的前置节点
    childNodes = None  # 当前节点的后置节点们
    g = 0  # 起点到当前节点所经过的距离
    h = 0  # 启发值
    D = 1   # 一个参数，在启发式函数中用到，相当于常量，值为1

    def __init__(self, pos):
        self.pos = pos
        self.childNodes = []

    # 定义估计函数estimation function
    def f(self):
        return self.g + self.h

    # 定义启发函数heuristic function h(n)
    def calcGH(self, targetPos):
        self.g = self.frontNode.g + math.sqrt(
            pow2(self.pos.X - self.frontNode.pos.X)
            + pow2(self.pos.Y - self.frontNode.pos.Y)
        )
        dx = abs(targetPos.X - self.pos.X)
        dy = abs(targetPos.Y - self.pos.Y)
        self.h = (dx + dy + (SQRT_2 - 2) * min(dx, dy)) * self.D


NEIGHBOR_DISES = [
    Vector(1, 0),
    Vector(1, 1),
    Vector(0, 1),
    Vector(-1, 1),
    Vector(-1, 0),
    Vector(-1, -1),
    Vector(0, -1),
    Vector(1, -1),
]


# 地图
class spMap:
    def __init__(self, msize, map, startPos=None, endPos=None):
        self.setMap(msize, map)  # 地图，0是空位，1是障碍
        self.setStartEnd(startPos, endPos)

    def setMap(self, msize, _map):
        self.mapsize = msize
        self.map = _map

    def setStartEnd(self, startPoint, endPoint):
        self.startPoint = startPoint  # 起始点
        self.endPoint = endPoint  # 终点
        self.tree = None  # 已经搜寻过的节点，是closed的集合
        self.foundEndNode = None  # 寻找到的终点，用于判断算法结束
        self.addNodeCallback = None

    # 判断当前点是否超出范围
    def isOutBound(self, pos):
        return pos.X < 0 or pos.Y < 0 or pos.X >= self.mapsize or pos.Y >= self.mapsize

    # 判断当前点是否是障碍点
    def isObstacle(self, pos):
        return self.map[pos.Y][pos.X] == 1

    # 判断当前点是否已经遍历过
    def isClosedPos(self, pos):
        if self.tree == None:
            return False
        nodes = []
        nodes.append(self.tree)
        while len(nodes) != 0:
            node = nodes.pop()
            if node.pos == pos:
                return True
            if node.childNodes != None:
                for nodeTmp in node.childNodes:
                    nodes.append(nodeTmp)
        return False

    # 获取周围可遍历的邻居节点
    def getNeighbors(self, pos):
        result = []
        for neighborDis in NEIGHBOR_DISES:
            newPos = pos + neighborDis
            if (
                self.isOutBound(newPos)
                or self.isObstacle(newPos)
                or self.isClosedPos(newPos)
            ):
                continue
            result.append(newPos)
        return result

    # 主体过程
    def process(self):
        # 初始化open集合，并把起始点放入
        willProcessNodes = deque()
        self.tree = Vector2Node(self.startPoint)
        willProcessNodes.append(self.tree)

        counter = 0
        # 开始迭代，直到找到终点，或找完了所有能找的点
        while (
            self.foundEndNode == None and len(willProcessNodes) != 0 and counter <= 300
        ):
            # 寻找下一个最合适的点，这里是最关键的函数，决定了使用什么算法
            counter += 1

            node = self.popLowGHNode(willProcessNodes)

            if self.addNodeCallback != None:
                self.addNodeCallback(node.pos)

            # 获取合适点周围所有的邻居
            neighbors = self.getNeighbors(node.pos)
            for neighbor in neighbors:
                # 初始化邻居，并计算g和h
                childNode = Vector2Node(neighbor)
                childNode.frontNode = node
                childNode.calcGH(self.endPoint)
                node.childNodes.append(childNode)

                # 添加到open集合中
                willProcessNodes.append(childNode)

                # 找到了终点
                if neighbor == self.endPoint:
                    self.foundEndNode = childNode

    # A*算法，寻找f = g + h最小的节点
    def popLowGHNode(self, willProcessNodes):
        foundNode = None
        for node in willProcessNodes:
            if foundNode == None:
                foundNode = node
            else:
                if node.f() < foundNode.f():
                    foundNode = node
        if foundNode != None:
            willProcessNodes.remove(foundNode)
        return foundNode
