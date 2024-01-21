#定义节点
class ListNode:
    def __init__(self, x):#x是_init_这个初始化函数的参数
        self.val = x
        self.next = None

#创建链表
y = [1, 2, 3, 4, 5]
head = ListNode(1)#1相当于初始化函数的参数
p = head
for i in range(1, len(y)):
	node = ListNode(y[i])
	p.next = node
	p = p.next

#增：在3和4之间增加一个值为6的节点
'''
def add(head):
	p = head
	while p.val != 3:
		p = p.next
	temp = p.next
	p.next = ListNode(6)
	p.next.next = temp
	while head != None:
		print(head.val)
		head = head.next
add(head)
'''
#删：删除值为3的节点，python会自动删除这个不用了的节点
'''
def sub(head):
	p = head
	while p.next.val != 3:
		p = p.next
	p.next = p.next.next
	while head != None:
		print(head.val)
		head = head.next
sub(head)
'''
#改：把值为3的节点的值改为6
'''
def change(head):
	p = head
	while p.val != 3:
		p = p.next
	p.val = 6
	while head != None:
		print(head.val)
		head = head.next
change(head)
'''
#查：输出值为3的节点的地址
'''
def search(head):
	p = head
	while p.val != 3:
		p = p.next
	print(p)
search(head)
'''
#定义遍历
'''
def show(head):
	p = head
	while p != None:
		print(p.val)
		p = p.next
show(head)	#show表示调用遍历函数show，给这个函数传入自变量head
'''
