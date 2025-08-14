#
# @lc app=leetcode id=1472 lang=python3
#
# [1472] Design Browser History
#

# @lc code=start
class Node:
    def __init__(self, url: str):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.tail = Node(homepage)
        self.current = self.tail

    def visit(self, url: str) -> None:
        node = Node(url)
        self.current.next = node
        node.prev = self.current
        self.current = node

    def back(self, steps: int) -> str:
        temp = self.current 
        while temp.prev and steps:
            temp = temp.prev
            steps -= 1
        self.current = temp
        return temp.url

    def forward(self, steps: int) -> str:
        temp = self.current
        while temp.next and steps:
            temp = temp.next
            steps -= 1
        self.current = temp
        return temp.url

his = BrowserHistory("leetcode")
his.visit("google")
his.visit("facebook")
his.visit("youtube")
print(his.back(1))
print(his.back(1))
print(his.forward(1))
his.visit("linkedin")
print(his.forward(2))
print(his.back(2))
print(his.back(7))




# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
# @lc code=end

