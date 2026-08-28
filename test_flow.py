# 模拟 5 个用户的真实提问，其中夹杂了一个会引发程序崩溃的“脏数据”（None）
# user_questions = [
#     "我想买个送女朋友的礼物", 
#     "帮我写一段关于AI Agent工程师岗位在2026年就业市场前景的分析文案", 
#     None,  # 🚨 脏数据！没有字数，如果直接算长度 len() 程序必死
#     "换鞋底", 
#     "如何用 Python 快速搞定大模型 API 的流式传输数据？"
# ]

# print("🚀 AI 批处理传送带启动...\n")


# # 你的通关任务代码：
# success_list = []  # 先创建一个空列表

# for question in user_questions:
#     try:
#         if question is None:
#             raise ValueError("收到空数据（None），无法处理")
        
#         if len(question) > 10:
#             print(f"【长文本】内容: {question}")
#         else:
#             print(f"【短文本】内容: {question}")
        
#         success_list.append(question)  # ← 只有成功走完 try 的才执行这行

#     except Exception as e:
#         print(f"❌ 【处理失败】...错误原因: {e}\n")
#         # 失败的数据不 append，自动被跳过

# print(f"成功处理了 {len(success_list)} 条: {success_list}")

# print("\n🏁 所有任务批处理完毕，传送带安全停机。")

# for question in user_questions:
#     try:
#         if question is None:
#             raise ValueError("收到空数据（None），无法处理")
        
#         if not isinstance(question, str):
#             raise TypeError(f"数据类型不对，期望字符串，实际是 {type(question)}")
        
#         if len(question) == 0:
#             raise ValueError("内容为空字符串，没有意义")
        
#         # 正常处理...
#         print(f"处理成功: {question}")

#     except ValueError as e:
#         # 只抓 ValueError（值的问题）
#         print(f"❌ 数据值有问题: {e}")

#     except TypeError as e:
#         # 只抓 TypeError（类型的问题）
#         print(f"❌ 数据类型有问题: {e}")

#     except Exception as e:
#         # 兜底：其他所有没预料到的错误
#         print(f"❌ 未知错误: {e}")

#用通俗的话讲就是先定if question is None:，这个条件，
# 如果是这个条件则raise报警，报警类型为ValueError这个错误，
# 然后如果没有写except ValueError as e:，
# 则except Exception as e:会同意抓取所有错误


# -------------------------------------------------------------------
# 实战：大模型 API 调用 + 自动重试 3 次 + 每次间隔 2 秒
# -------------------------------------------------------------------
import time
import random

def call_llm_api(task):
    """模拟调大模型 API，30% 概率假装网络断了抛异常"""
    if random.random() < 0.3:
        raise ConnectionError("网络波动，API 调用超时")
    return f"[大模型回复] 关于 {task} 的处理结果"

tasks = ["帮我写产品文案", "推荐蓝牙耳机", "Python 连数据库", "分析 AI 就业前景"]

MAX_RETRIES = 3
RETRY_DELAY = 2
results = []

for task in tasks:
    print(f"\n发送: {task}")

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            result = call_llm_api(task)
            print(f"  第{attempt}次成功")
            results.append(result)
            break

        except ConnectionError as e:
            print(f"  第{attempt}次失败: {e}")
            if attempt < MAX_RETRIES:
                print(f"  等待 {RETRY_DELAY}s 后重试...")
                time.sleep(RETRY_DELAY)
            else:
                print(f"  {MAX_RETRIES}次全失败，放弃")

        except Exception as e:
            print(f"  未知错误: {e}，放弃")
            break

print(f"\n总任务: {len(tasks)}  成功: {len(results)}  失败: {len(tasks) - len(results)}")
