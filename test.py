import requests
import time


def test_services():
    # 测试加法接口（两种传参方式）
    print("测试加法接口:")
    print("\n方式1：通过URL查询参数传参")
    try:
        response = requests.post(
            "http://localhost:8000/tools/add?a=5&b=3",  # 查询参数
            timeout=5
        )
        print(f"响应: {response.json()}")
    except Exception as e:
        print(f"请求失败: {str(e)}")

    # 测试问候接口
    print("\n测试问候接口:")
    try:
        response = requests.get(
            "http://localhost:8000/resources/greeting/Alice",
            timeout=5
        )
        print(f"响应: {response.json()}")
    except Exception as e:
        print(f"请求失败: {str(e)}")


if __name__ == "__main__":
    test_services()