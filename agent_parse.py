# 模拟大模型在网络不稳定时，返回的非标准结构化数据（缺少了 'usage' 字段，且 keys 格式混乱）
llm_response = {
    "id": "chatcmpl-9527",
    "model": "deepseek-v3",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "您好！我是您的 AI Agent 助理。"
            
            },
            "finish_reason": "stop"
        }

        
    
    ]
    # 🚨 注意：正常的返回本该有 "usage": {"total_tokens": 125}，但这里缺失了！
}
print("🚀 开始执行 AI Agent 响应防御性解析...\n")

# ----------------------------------------------------
# 你的生死通关任务：
# ----------------------------------------------------

# 任务 1：用安全的方式拿到大模型回复的文本内容（content）。
# 提示：逐层剥皮，Choices 是个列表，取出第 0 个元素，再拿 message。
content = llm_response["choices"][0]["message"]["content"]
print(f"【提取成功】大模型文本: {content}")

# 任务 2（核心死磕）：我们要拿 total_tokens，但现在字典里根本没有 "usage"！
# 如果你写 print(llm_response["usage"]["total_tokens"]) 程序必死！
# 🚨 你的目标：利用右侧 Trae AI，让他教你如何用 `.get()` 方法拿数据。
# 达标标准：如果存在就打印数字；如果不存在，不要崩盘，自动输出默认值 0。

# 请在此处补全你的防御性提取逻辑：
print(llm_response.get("usage", {}).get("total_tokens", 0))

print()

# ===================================================================
# 模拟大模型由于幻觉和流式输出，返回的前后夹杂了大量空格和换行符的脏文本
llm_dirty_text = "\n\n   【核心突破】手把手带你零基础搓出商业级 AI Agent 系统！   \n\n"

# ====================================================
# 🚨 你的死命令通关任务（今晚离开图书馆前必须搞定）：
# ====================================================

# 1. 查阅或让 Trae 告诉你，Python 里去除字符串"前后两端空格和换行符"的内置方法是什么？
# 2. 补全下面这行代码，把 llm_dirty_text 清洗干净，存进 clean_text 变量。

clean_text = llm_dirty_text.strip()  # 🚨 补全这行代码

print("--- 清洗前原样 ---")
print(llm_dirty_text)
print("--- 清洗后效果 ---")
print(clean_text)
print(clean_text.startswith("【核心"))  # 判断是不是以【核心开头的,是返回true,不是返回false

# 💡 附加思考题（能在控制台打印出来就行）：
# 如果我想判断这个清洗后的文本，是不是以 "【核心" 这两个字开头的，应该用 Python 字符串的哪个方法？


print("\n" + "="*60)
print("以下为新增练习题")
print("="*60 + "\n")


# ===================================================================
# 题目1：天气 API，数据不完整
# ===================================================================

weather = {
    "city": "深圳",
    "current": {
        "temp": 32,
        "humidity": 85,
        "desc": "  多云转阵雨  \n"
        # 缺失 "wind": {"speed": 12, "direction": "东南"}
    }
    # 缺失 "aqi": {"pm25": 45}
}

# 1-1 拿城市名
city = weather["city"]
city = weather.get("city", "未知城市名")
# 1-2 拿温度
##  temp = weather[1][0] 字典嵌套必须使用key调用
temp = weather.get("current",{}).get("temp",0)

# 1-3 清洗天气描述（去空格换行）
desc = weather["current"]["desc"].strip()

# 1-4 拿风速，没返回默认 0
wind_speed = weather.get("current",{}).get("speed",0)

# 1-5 拿 PM2.5，整块缺失默认 0
pm25 = weather.get("api",{}).get("pm25",0)

# 1-6 判断天气描述是否以 "多云" 开头
is_cloudy = desc.strip().startswith("多云")

print(city, temp, desc, wind_speed, pm25, is_cloudy)


# ===================================================================
# 题目2：快递查询 API，数据脏了还缺字段
# ===================================================================

express = {
    "nu": "YT9527133688",
    "com": "圆通速递",
    "data": [
        {"time": "2026-06-11 08:30", "context": "  已签收，签收人：本人  \n"},
        {"time": "2026-06-11 06:10", "context": "\n  派送中，快递员张师傅 13800138000  \n"},
        {"time": "2026-06-10 22:00", "context": "  【已到达】深圳集散中心  "}
    ]
    # 缺失 "state": "3"（3表示已签收）
}

# 2-1 拿快递单号
nu = express["nu"]

# 2-2 拿快递公司名，没返回默认 "未知快递"
com = express["com"]

# 2-3 拿物流状态码，没返回默认 "0"
state = express.get("state",0)

# 2-4 清洗第一条物流记录的 context
first_context = express["data"][0]["context"].strip()

# 2-5 判断第一条物流是否以 "已签收" 开头
is_signed = first_context.startswith("已签收")

print(nu, com, state, first_context, is_signed)


# ===================================================================
# 题目3：视频平台 API，返回的是一条视频信息
# ===================================================================

video = {
    "bv": "BV1xx411c7mD",
    "title": "   【教程】零基础学 Python  \n",
    "owner": {
        "name": "CodeSheep",
        "face": "https://xxx.com/face.jpg"
        # 缺失 "follower": 52000
    },
    "stat": {
        "view": 380000,
        "danmaku": 6500
        # 缺失 "like": 21000
    }
}

# 3-1 拿 BV 号
bv = video["bv"]

# 3-2 清洗标题
title = video["title"].strip()

# 3-3 判断标题是否以 "【教程】" 开头
is_tutorial = title.startswith("【教程】")

# 3-4 拿 UP 主名字
owner_name =video["owner"]["name"]

# 3-5 拿 UP 主粉丝数，没返回默认 0
follower = video["owner"].get("follower",0)

# 3-6 拿点赞数，没返回默认 0
like = video.get("stat",{}).get("like",0)

print(bv, title, is_tutorial, owner_name, follower, like)
