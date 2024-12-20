import datetime
today = datetime.date.today().strftime('%Y-%m-%d')
#这里定义一个函数，输入书名可以返还这本书的ISBN
def ISBN(title):
    for isbn, details in library_books.items():
        if details['title'] == title:
            return isbn
    return None 


library_books = {
    '978-7-111-123456-1': {'title': '深入理解计算机系统', 'author': 'Randal E. Bryant', 'categories': {'计算机', '系统'},'quantity':5 },
    '978-7-302-654789-2': {'title': '计算机网络：自顶向下方法', 'author': 'James F. Kurose', 'categories': {'计算机', '网络'}, 'quantity':2},
    '978-7-121-789456-3': {'title': '算法导论', 'author': 'Thomas H. Cormen', 'categories': {'计算机', '算法'},'quantity':1},
    '978-7-302-987654-4': {'title': 'C程序设计语言', 'author': 'Brian W. Kernighan', 'categories': {'计算机', '编程'},'quantity':2},
    '978-7-115-765432-5': {'title': 'Python编程:从入门到实践', 'author': 'Eric Matthes', 'categories': {'计算机', '编程'},'quantity':2},
    '978-7-121-654321-6': {'title': 'Java核心技术 卷I', 'author': 'Cay S. Horstmann', 'categories': {'计算机', '编程'},'quantity':4},
    '978-7-302-876543-7': {'title': '编译原理', 'author': 'Alfred V. Aho', 'categories': {'计算机', '编译'},'quantity':2},
    '978-7-111-987654-8': {'title': '数据库系统概念', 'author': 'Abraham Silberschatz', 'categories': {'计算机', '数据库'},'quantity':2},
    '978-7-302-123456-9': {'title': '操作系统原理', 'author': 'Andrew S. Tanenbaum', 'categories': {'计算机', '系统'},'quantity':6},
    '978-7-115-234567-0': {'title': '机器学习', 'author': '周志华', 'categories': {'计算机', '人工智能'},'quantity':2},
    '978-7-121-345678-1': {'title': '数据结构与算法分析:C语言描述', 'author': 'Mark Allen Weiss', 'categories': {'计算机', '算法'},'quantity':1},
    '978-7-121-456789-2': {'title': 'C++ Primer', 'author': 'Stanley B. Lippman', 'categories': {'计算机', '编程'},'quantity':2},
    '978-7-115-567890-3': {'title': '计算机组成与设计', 'author': 'David A. Patterson', 'categories': {'计算机', '硬件'},'quantity':2},
    '978-7-115-678901-4': {'title': 'Linux内核设计与实现', 'author': 'Robert Love', 'categories': {'计算机', '操作系统'},'quantity':2},
    '978-7-302-789012-5': {'title': '深入浅出React', 'author': 'Stoyan Stefanov', 'categories': {'计算机', '前端开发'},'quantity':2},
    '978-7-121-890123-6': {'title': '云计算：概念、技术与架构', 'author': 'Thomas Erl', 'categories': {'计算机', '云计算'},'quantity':7},
    '978-7-121-901234-7': {'title': '大数据技术原理与应用', 'author': '李三立', 'categories': {'计算机', '大数据'},'quantity':3},
    '978-7-121-012345-8': {'title': '深度学习', 'author': 'Ian Goodfellow', 'categories': {'计算机', '人工智能'},'quantity':2},
    '978-7-115-123456-9': {'title': 'Web开发权威指南', 'author': 'John Duckett', 'categories': {'计算机', 'Web开发'},'quantity':0},
    '978-7-111-234567-0': {'title': 'TensorFlow深度学习', 'author': 'Tom Hope', 'categories': {'计算机', '人工智能'},'quantity':8}
}


user_info = {
    1: {'name': '张伟', 'borrowed_books': ['算法导论', '编译原理', '深入浅出React', '大数据技术原理与应用', '深度学习']},
    2: {'name': '李娜', 'borrowed_books': []},
    3: {'name': '王强', 'borrowed_books': []},
    4: {'name': '刘敏', 'borrowed_books': []},
    5: {'name': '陈杰', 'borrowed_books': []},
    6: {'name': '杨洋', 'borrowed_books': []},
    7: {'name': '赵丽', 'borrowed_books': []},
    8: {'name': '孙涛', 'borrowed_books': []},
    9: {'name': '周峰', 'borrowed_books': []},
    10: {'name': '郑辉', 'borrowed_books': []},
    11: {'name': '何婷', 'borrowed_books': []},
    12: {'name': '宋佳', 'borrowed_books': []},
    13: {'name': '马刚', 'borrowed_books': []},
    14: {'name': '高磊', 'borrowed_books': []},
    15: {'name': '冯芳', 'borrowed_books': []},
    16: {'name': '吴斌', 'borrowed_books': []},
    17: {'name': '蒋辉', 'borrowed_books': []},
    18: {'name': '钱玉', 'borrowed_books': []},
    19: {'name': '沈娟', 'borrowed_books': []},
    20: {'name': '姚明', 'borrowed_books': []},
    21: {'name': '许涛', 'borrowed_books': []},
    22: {'name': '邓颖', 'borrowed_books': []},
    23: {'name': '任飞', 'borrowed_books': []},
    24: {'name': '贾磊', 'borrowed_books': []},
    25: {'name': '白雪', 'borrowed_books': []},
    26: {'name': '崔浩', 'borrowed_books': []},
    27: {'name': '罗华', 'borrowed_books': []},
    28: {'name': '唐梅', 'borrowed_books': []},
    29: {'name': '胡兵', 'borrowed_books': []},
    30: {'name': '褚强', 'borrowed_books': []}
}

borrow_infolist={ ('2024-10-28','张伟','算法导论','借'),
                  ('2024-10-28','张伟','编译原理','借'),
                  ('2024-10-28','张伟','深入浅出React','借'),
                  ('2024-10-28','张伟','大数据技术原理与应用','借'),
                  ('2024-10-28','张伟','深度学习','借'),
                            #借阅记录 元祖类型
}

set=[]

def borrow_book(username,booktitle):
    #先判断user_info有没有这个人
    for user in user_info.values():
        user_found=False
        if user['name']==username:
            userfound=True
            break#这段语句的含义在于，如果遍历一遍名单里的人没有这个人 ，那么user_found最终没有办法从false变成true，在后面的判定中，你还是false，那你出局
    if user_found==False:
        print("读者{}不存在".format(username))

    #现在检查一下你有没有借满五本书
    borrow_count=0
    for record in borrow_infolist:
        if record[1]==username:
            borrow_count+=1
    if borrow_count>=5:
        print("读者{}已经借了5本书,不能再借了".format(username))
        return
    #检查一下你是不是借过这本书
    for record in borrow_infolist:
        if record[1]==username:
            if record[2]==booktitle:
                print("读者{}已借阅过{}这本书".format(username,booktitle))
                return
    #检查一下这本书还有没有存货，又是对library_books的一次遍历
    for record2 in library_books.values():
        if record2['title']==booktitle and record2['quantity']== 0:
            print("{}存有0本,不可借".format(booktitle))
            return 
    #满足了所有条件，终于可以借书了，但要先注意各位字典大爷的改动，有三个字典要改动
        #library_books的书籍数量-1
        #user_info里的该读者的'borrowed_books'对应的列表里面加上这本书的书名
        #borrow_infolist里加上“日期”“姓名”“书名”“借”
    for isbn,record3 in library_books.items:
        if record3['title']==booktitle :
            record3['quantity']-=1
    for user_id, record4 in user_info.items():
        if record4['name']==username:
            record4['borrowed_books'].append(booktitle)
    borrow_infolist.append((today, username, booktitle, '借'))
    