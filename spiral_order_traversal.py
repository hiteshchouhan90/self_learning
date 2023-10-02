from pprint import pprint
class spiral_order_traversal:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, a):
        left_boundary = 0
        right_boundary = a - 1
        top_boundary = 0
        bottom_boundary = a - 1
        val = 1
        lst = [[None for i in range(a)] for j in range(a)]
        while 1==1:
            if left_boundary > right_boundary or top_boundary > bottom_boundary:
                return lst

            for k in range(left_boundary,right_boundary + 1):
                lst[top_boundary][k] = val
                val += 1
            top_boundary += 1

            for k in range(top_boundary, bottom_boundary + 1):
                lst[k][right_boundary]= val
                val += 1
            right_boundary -= 1

            for k in range(right_boundary, left_boundary - 1, -1):
                lst[bottom_boundary][k] = val
                val += 1
            bottom_boundary -= 1

            for k in range(bottom_boundary, top_boundary - 1, -1):
                lst[k][left_boundary] = val
                val += 1
            left_boundary += 1

obj = spiral_order_traversal()
pprint(obj.generateMatrix(5))