# ============================================================
# 题目：AI 工作流——Agent A 输出校验
# ============================================================
# 背景：Agent A 处理了 7 条任务，产出如下。你需要用 try/except/raise
#       逐条校验，合格才 .append() 到一个新列表里，最后打印结果。
# ============================================================

# 数据（不用改）：
agent_a_outputs = [
    "根据您的要求，推荐以下 3 款耳机：Sony、AirPods、Bose",
    "",
    None,
    "摘要：Python 连接数据库",                          # ← 少于 20 字
    "详细方案：关于 AI 就业市场分析...(此处省略 200 字)",
    "错误：API 调用超时，请重试",                       # ← 以 "错误" 开头
    12345,                                             # ← 不是字符串
]

# 校验规则（必须按顺序检查）：
# ① 如果是 None        → raise ValueError("Agent A 返回了 None，可能超时")
# ② 如果不是字符串      → raise TypeError(f"类型异常，收到 {type(x).__name__}")
# ③ 去空格后是空字符串  → raise ValueError("Agent A 返回了空字符串")
# ④ 字数小于 20        → raise ValueError(f"输出太短，仅 {len(x)} 字")
# ⑤ 以 "错误" 或 "Error" 开头 → raise RuntimeError(f"Agent A 报错：{x}")

# 要求：
# 1. 用 for i, output in enumerate(agent_a_outputs) 循环
# 2. 用 try/except 分别捕获 ValueError、TypeError、RuntimeError
# 3. 校验通过的才 .append() 到 qualified_outputs 列表
# 4. 打印每条的处理结果（通过 or 失败原因）
# 5. 最后打印：总条数、合格数、丢弃数

# ↓↓↓ 你的代码写在这里 ↓↓↓
qualified_outputs = []
for output in agent_a_outputs:
    try:
        if output is None:
            raise ValueError("Agent A 返回了 None，可能超时")
        elif not isinstance(output, str):#-----
            raise TypeError(f"类型异常，收到 {type(output).__name__}")
        elif output.strip()=="":
            raise ValueError("Agent A 返回了空字符串")
        elif len(output.strip())<=20:
            raise ValueError(f"输出太短，仅 {len(output)} 字")
        elif output.startswith("错误") or output.startswith("Error"):#----
            raise RuntimeError(f"Agent A 报错：{output}")
        else:
            qualified_outputs.append(output)
            print(f"通过：{output}")
            continue
    except ValueError as e:
        print(f"校验失败：{e}")
        continue
    except TypeError as e:
        print(f"校验失败：{e}")
        continue
    except RuntimeError as e:
        print(f"校验失败：{e}")
        continue

