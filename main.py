from fastapi import FastAPI
import uvicorn

app = FastAPI()

# 修改为同时支持JSON body和查询参数
@app.post("/tools/add")
async def add_numbers(a: int, b: int):
    """加法工具接口（兼容JSON body和查询参数）"""
    return {"result": a + b}

@app.get("/resources/greeting/{name}")
async def get_greeting(name: str):
    """问候接口"""
    return {"result": f"Hello, {name}!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)