ai_job=["AI应用开发","AI实施工程师","大模型数据清洗工"]
print(ai_job[1])
print(ai_job[2])  # 索引从 0 开始，3个元素只有 [0][1][2]
# 需求：打印出你的目标岗位（target_job）
user_data = {
    "name": "tomlia1",
    "school": "民办三本",
    "target_job": "AI实施工程师"
    
}

print(user_data["target_job"])  # 键名是 "target_job"，有下划线
# 需求：如果自学时间大于等于 4 小时，打印合格；否则打印偷懒
study_hours = 5
if study_hours >= 4:  # == 是比较，= 是赋值；>= 才是"大于等于"
    print("今日自学达标，抗压成功！")
else:
    print("你在偷懒，秋招要凉！")
