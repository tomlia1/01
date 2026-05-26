import json

# 模拟大模型通过 API 返回的原始 JSON 字符串
# 里面套了字典，字典里又套了列表，列表里又套了字典
raw_response = """
{
    "status": "success",
    "data": {
        "agent_name": "Media_Bot_V1",
        "generated_articles": [
            {"id": 101, "title": "2026如何用AI搞钱", "clicks": 3200},
            {"id": 102, "title": "三本学生的AI逆袭路线", "clicks": 8500}
        ]
    }
}
"""

# 第一步：把字符串解析成 Python 认识的字典/列表结构
# 注意：这一行你不用动，这是固定的解包动作
parsed_data = json.loads(raw_response)




# 任务 1：请尝试写一行代码，打印出这个 Agent 的名字（期待输出: Media_Bot_V1）
print("【任务1结果】：", parsed_data["data"]["agent_name"])

# 任务 2：请写代码，打印出第二篇文章的标题（期待输出: 三本学生的AI逆袭路线）
# 提示：文章在 generated_articles 列表里，列表的第 2 个元素的索引是 1
print("【任务2结果】：", parsed_data["data"]["generated_articles"][1]["title"])
