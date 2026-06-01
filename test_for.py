# 1. 定义一个包含5个用户提问的列表
user_questions = [
    "今天天气怎么样？",
    "如何学习Python编程？需要从哪里开始？",
    "人工智能和机器学习有什么区别？",
    "推荐一些好看的电影吧",
    "1 + 1 等于几？",
    102,
    "你好",
    True
    
]

# # 2. 使用 for 循环遍历列表
# print("=== 使用 for 循环处理 ===")
# for question in user_questions:
#     try:
#         # 检查问题字数是否大于10
#         if len(question) > 10:
#             print(f"'{question}' -> 长文本")
#         else:
#             print(f"'{question}' -> 短文本")
#     except Exception as e:
#         # 捕获未知错误，打印信息但不中断程序
#         print(f"'{question}' -> 处理失败")

# 3. 使用列表推导式处理（创建新列表）
# print("\n=== 使用列表推导式处理 ===")
# result_list = [
#     "长文本" if len(q) > 10 else "短文本"
#     for q in user_questions
# ]
# print("处理结果列表:", result_list)

# 4. 列表推导式 + 异常处理
# print("\n=== 列表推导式 + 异常处理 ===")
# result_with_exception = []
# for q in user_questions:
#     try:
#         result_with_exception.append("长文本" if len(q) > 10 else "短文本")
#     except:
#         result_with_exception.append("处理失败")
# print("带异常处理的结果:", result_with_exception)

#=== 列表推导式 + 异常处理 ===
#带异常处理的结果: ['短文本', '长文本', '长文本', '短文本', '短文本', '处理失败', '短文本', '处理失败']


# for x in [9, 4, 6]:
#     print("我在循环里")    # ← 缩进了，属于循环，执行3次
#     print("我也在循环里")  # ← 缩进了，属于循环，执行3次
# print("我不在循环里")      # ← 没缩进，不属于循环，只执行1次

# # ❌ 丑：写一堆没用的数字占位置
# for x in [9, 4, 6, 8, 2]:
#     print("我在循环里")

# # ✅ 帅：用 range，清晰表达"我要跑5次"
# for i in range(5):
#     print("我在循环里")

nums=[3,8,15,22,7,0,10,5]
for num in nums:
    try:
        if num==0:
            1/0
        elif num>=10:
            print(num,"是大的")
        else:
             print(num,"小于的")
    except:
        print(num,"跳过")

scores=[80,90,75,95,84,92,88]
result_scores=["及格" if score>=60 else "不及格" 
for score in scores]
print(result_scores)

mixed=["hello",123,"world",None,"python"]
for mix in mixed:
    try:
        
        print(mix.upper())
    except:
        print(mix,"处理失败")

words=["apple","banana","orange","kiwi","grape"]
new_words=[q for q in words if len(q)%2==0]
print(new_words)
