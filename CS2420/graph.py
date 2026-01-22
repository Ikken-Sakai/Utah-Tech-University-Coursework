from graphics import *
import math

class Stack:

    def __init__(self):
        self.mItems = []
        self.mLength = 0
    def top(self):
        if self.empty() == False:
            return self.mItems[self.mLength -1]
    def push(self, item):
        self.mItems.append(item)
        self.mLength +=1
    def pop(self):
        if self.empty() == False:
            a = self.mItems.pop()
            self.mLength -=1
            return a
    def empty(self):
        if len(self.mItems) == 0:
            return True
        else:
            return False


def main():

    infix = input("Enter the fuction you want to graph. (EX: x*x): ")
    postfix = InfixToPostFix(infix)
    print (postfix)
    win = GraphWin("My Circle", 500, 500)
    XLOW = -10
    YLOW = -10
    XHIGH = +10
    YHIGH = +10
    win.setCoords(XLOW, YLOW,  XHIGH, YHIGH)

    xpoints = []
    ypoints = []
    x = XLOW
    while x<=XHIGH:
        y = EvaluatePostFix(postfix, x) 
        print (y)
        xpoints.append(x)
        ypoints.append(y)
        x += .1

    for i in range(len(xpoints)-1):
        p1 = Point(xpoints[i], ypoints[i])
        p2 = Point(xpoints[i+1], ypoints[i+1])
        line = Line(p1, p2)
        line.draw(win)
        
    # x-axis
    linex = Line(Point(XLOW, 0), Point(XHIGH,0))
    linex.setOutline("red")
    linex.setWidth(3)
    linex.draw(win)
    # y-axis
    liney = Line(Point(0,YLOW), Point(0, YHIGH))
    liney.setOutline("red")
    liney.setWidth(3)
    liney.draw(win)
    
    win.getMouse() 
    win.close()   

def InfixToPostFix(input):
    stack = Stack()            
    postFix = ""          
    for x in input:       
        if x in "0123456789x":  
            postFix += x     
        elif x =="(":       
            stack.push(x)     
        elif x == ")":      
            while stack.empty() == False:   
                top = stack.top()          
                if top in "+-/*":           
                    postFix += stack.pop()
                elif top == "(":        
                    stack.pop()           
                    break             
        elif x in "+-":         
            top = stack.top()   
            if stack.empty() or top == "(":
                stack.push(x)
            else:
                postFix += stack.pop()
                stack.push(x)
        elif x in "*/":
            top = stack.top()
            if stack.empty() or top not in "*/" :
                stack.push(x)
            else:
                postFix += stack.pop()
                stack.push(x)

    while not stack.empty():
        postFix+= stack.pop()
    return postFix
def EvaluatePostFix(input, value):
    stack = Stack()
    for x in input:
        if x in "x0123456789":
            if x =="x":
                stack.push(value)
            else:
                stack.push(float(x))
        elif x =="+":
            rhs = stack.pop()
            lhs = stack.pop ()
            number = lhs + rhs
            stack.push(number)
        elif x =="-":
            rhs = stack.pop()
            lhs = stack.pop()
            number = lhs - rhs
            stack.push(number)
        elif x =="/":
            rhs = stack.pop()
            lhs = stack.pop()
            number = lhs / rhs
            stack.push(number)
        elif x =="*":
            rhs = stack.pop()
            lhs = stack.pop()
            number = lhs * rhs
            stack.push(number)
    return stack.top()

if __name__ == "__main__":
    main()
