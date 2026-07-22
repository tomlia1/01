# # 1. 定义一个包含5个用户提问的列表
# user_questions = [
#     "今天天气怎么样？",
#     "如何学习Python编程？需要从哪里开始？",
#     "人工智能和机器学习有什么区别？",
#     "推荐一些好看的电影吧",
#     "1 + 1 等于几？",
#     102,
#     "你好",
#     True

# ]

# # # 2. 使用 for 循环遍历列表
# # print("=== 使用 for 循环处理 ===")
# # for question in user_questions:
# #     try:
# #         # 检查问题字数是否大于10
# #         if len(question) > 10:
# #             print(f"'{question}' -> 长文本")
# #         else:
# #             print(f"'{question}' -> 短文本")
# #     except Exception as e:
# #         # 捕获未知错误，打印信息但不中断程序
# #         print(f"'{question}' -> 处理失败")

# # 3. 使用列表推导式处理（创建新列表）
# # print("\n=== 使用列表推导式处理 ===")
# # result_list = [
# #     "长文本" if len(q) > 10 else "短文本"
# #     for q in user_questions
# # ]
# # print("处理结果列表:", result_list)

# # 4. 列表推导式 + 异常处理
# # print("\n=== 列表推导式 + 异常处理 ===")
# # result_with_exception = []
# # for q in user_questions:
# #     try:
# #         result_with_exception.append("长文本" if len(q) > 10 else "短文本")
# #     except:
# #         result_with_exception.append("处理失败")
# # print("带异常处理的结果:", result_with_exception)

# #=== 列表推导式 + 异常处理 ===
# #带异常处理的结果: ['短文本', '长文本', '长文本', '短文本', '短文本', '处理失败', '短文本', '处理失败']


# # for x in [9, 4, 6]:
# #     print("我在循环里")    # ← 缩进了，属于循环，执行3次
# #     print("我也在循环里")  # ← 缩进了，属于循环，执行3次
# # print("我不在循环里")      # ← 没缩进，不属于循环，只执行1次

# # # ❌ 丑：写一堆没用的数字占位置
# # for x in [9, 4, 6, 8, 2]:
# #     print("我在循环里")

# # # ✅ 帅：用 range，清晰表达"我要跑5次"
# # for i in range(5):
# #     print("我在循环里")

# nums=[3,8,15,22,7,0,10,5]
# for num in nums:
#     try:
#         if num==0:
#             1/0
#         elif num>=10:
#             print(num,"是大的")
#         else:
#              print(num,"小于的")
#     except:
#         print(num,"跳过")

# scores=[80,90,75,95,84,92,88]
# result_scores=["及格" if score>=60 else "不及格" 
# for score in scores]
# print(result_scores)

# mixed=["hello",123,"world",None,"python"]
# for mix in mixed:
#     try:
        
#         print(mix.upper())
#     except:
#         print(mix,"处理失败")

# words=["apple","banana","orange","kiwi","grape"]
# new_words=[q for q in words if len(q)%2==0]
# print(new_words)

##--1

print("-----2注意没解决")
# orders = [
#     {"id": "A001", "price": 29.9, "qty": 3, "discount": "无"},
#     {"id": "A002", "price": 59.0, "qty": 1},
#     {"id": "A003", "price": 99.0, "qty": 2, "discount": 0.8},
#     {"id": 10086, "price": 50, "qty": 2, "discount": 0.9},
#     {"id": "A005", "price": "一百", "qty": 1},
# ]
# for n in range(len(orders)):
#     try:
#         discount=get(orders[n][discount],1)
#         sum=float(orders[n]["price"])*int(orders[n]["qty"])*float(discount)
#     except:
#         print("错误")
#         continue

emails = ["tom@qq.com", "jerry@gmail.com", "alice@163.com", "bob@outlook.com"]
reuslt=[]
for n in range(len(emails)):
    reuslt.append(emails[n].split("@")[0])
print(reuslt)
result=[email.split("@")[0] for email in emails]
##！！因为email.split("@")得到的是["tom","qq.com"]两个元素，所以需要取第一个元素
print(result)


names = ["张伟", "欧阳修", "司马", "李", "上官婉儿", "王小明"]
result=[name for name in names if len(name)>=2]
print(result)

ratings = [4.5, 3.0, 5.0, 2.5, 4.0, 1.0]
for rating in ratings:
    try:
        if rating>=4:
            print(rating,"推荐")
        elif rating>=2:
            print(rating,"一般")
        else:
            print(rating,"差评")
    except:
        print(rating,"跳过")

# ！！ strip() 方法返回移除字符串头尾指定的字符生成的新字符串，如果都不写就是去除空白
raw_items = [" 苹果 ", "香蕉", " 橘子 ", "", " 葡萄"]
# 列表推导式：遍历 raw_items 中的每个元素
# 1. item.strip() 去除字符串首尾的空白字符（空格、换行等）
# 2. if item.strip()!="" 过滤掉空字符串（去除空白后为空的不保留）
# 3. 最终保留的是：去除空白后非空的字符串
raw_items=[item.strip() for item in raw_items if item.strip()!=""]
print(raw_items)

# 数据
cities = ["北京", "上海", "广州", "深圳", "杭州", "成都", "武汉"]
result_cities = [city for city in cities if "州" in city]
print(result_cities)

# 数据（每个字典 = 一个学生）
students = [
    {"name": "小明", "age": 20, "score": 85},
    {"name": "小红", "age": 22, "score": 92},
    {"name": "小刚", "age": 19, "score": 58},
    {"name": "小丽", "age": 21, "score": 76},
]
names=[student["name"] for student in students if student["score"]>=80]
print(names)
##等价的
names=[students[n]["name"] for n in range(len(students)) if students[n]["score"]>=80]
print(names)

# 数据
movies = [
    {"title": "流浪地球", "rating": 7.9, "year": 2019},
    {"title": "哪吒之魔童降世", "rating": 8.4, "year": 2019},
    {"title": "你好李焕英", "rating": 7.8, "year": 2021},
    {"title": "战狼2", "rating": 7.1, "year": 2017},
    {"title": "长津湖", "rating": 7.4, "year": 2021},
]
for movie in movies:
    try:
        if movie["rating"]>=8:
            print("神作")
        elif movie["rating"]>=7:
            print("还行")
        else:
            print("不推荐")
    except:
        print(movie["title"],"跳过")
  
