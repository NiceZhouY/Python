# -*- coding: utf-8 -*-
"""
@author: Yi_Zhou
"""


class Node:

    def __init__(self, value=None, next=None):
        self._value = value
        self._next = next

    def getValue(self):
        return self._value

    def getNext(self):
        return self._next

    def setValue(self, value):
        self._value = value

    def setNext(self, next):
        self._next = next



class ListNode:

    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def isEmpty(self):
        return self._head

    def add(self, value):
        """插入头部"""
        exaNode = Node(value)
        exaNode.setNext(self._head)
        self._head = exaNode
        if self._tail is None:
            self._tail = self._head
        self._length += 1

    def append(self, value):
        """插入尾部"""
        exaNode = Node(value)
        if self.isEmpty() is None:
            exaNode.setValue(value)
            exaNode.setNext(self._head)
            self._head = exaNode
        else:
            cursor = self._tail
            cursor.setNext(exaNode)
            # self._tail = cursor.getNext()
        self._tail = exaNode
        self._length += 1

    def search(self, value):
        """检索值是否存在"""
        cursor = self._head
        flag = False
        while cursor is not None and flag is not True:
            if cursor.getValue() == value:
                flag = True
            else:
                cursor = cursor.getNext()
        return flag

    def index(self, value):
        """查找值的位置"""
        cursor = self._head
        flag = False
        count = 0
        while cursor is not None and flag is not True:
            if cursor.getValue() == value:
                flag = True
            else:
                count += 1
                cursor = cursor.getNext()
        return count

    def remove(self, value):
        """删除指定值"""
        cursor = self._head
        prevalue = None
        while cursor is not None:
            if cursor.getValue() == value:
                if prevalue is None:
                    self._head = cursor.getNext()
                    break
                else:
                    prevalue.setNext(cursor.getNext())
                    self._length -= 1
                    break
            else:
                prevalue = cursor
                cursor = cursor.getNext()

    def lpop(self):
        """删除尾部值并返回"""
        count = 0
        prevalue = None
        cursor = self._head
        if self._length == 0: return None
        while count < self._length - 1:
            count += 1
            prevalue = cursor
            cursor = cursor.getNext()
        if count > 0 and self._length > 0:
            prevalue.setNext(None)
            result = cursor.getValue()
        else:
            result = cursor.getValue()
            cursor.setValue(None)
            self._length = 1
        self._tail = prevalue
        self._length -= 1
        return result

    def insert(self, value, position):
        """插入值到指定位置"""
        if position <= 1:
            self.add(value)
        elif position >= self._length:
            self.append(value)
        else:
            exaNode = Node(value)
            count = 0
            prevalue = None
            cursor = self._head
            while count < position:
                count += 1
                prevalue = cursor
                cursor = cursor.getNext()
            exaNode.setNext(prevalue.getNext())
            prevalue.setNext(exaNode)
            self._length += 1

    def getAllValue(self):
        items = []
        cursor = self._head
        if cursor is None: return None
        while True:
            if cursor.getNext() is not None:
                items.append(str(cursor.getValue()))
                cursor = cursor.getNext()
            else:
                items.append(str(cursor.getValue()))
                break
        return " ->".join(items)


class Solution:
    def addTwoNumbers(self, lN1, lN2):
        """
        :type lN1: ListNode
        :type lN2: ListNode
        :rtype: ListNode
        """
        cursor = ListNode()
        item1 = []
        item2 = []
        while lN1 is not None:
            result = lN1.lpop()
            if result is None:
                break
            item1.append(str(result))

        while lN2 is not None:
            result = lN2.lpop()
            if result is None:
                break
            item2.append(str(result))
        result = int(''.join(reversed(item1))) + int(''.join(reversed(item2)))

        while result > 0:
            remainder = result % 10
            cursor.append(remainder)
            result = result // 10
        return cursor



L1 = ListNode()
for i in [3, 4, 2, 6, 9]:
    L1.add(i)
print(L1.getAllValue())

L2 = ListNode()
for i in [4, 6, 5, 7, 2]:
    L2.add(i)
print(L2.getAllValue())

Lsum = Solution()
L3 = Lsum.addTwoNumbers(L1, L2)
print(L3.getAllValue())
