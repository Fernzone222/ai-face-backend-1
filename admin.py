from fastapi import FastAPI

app = FastAPI()

@app.get("/admin/")
def admin_panel():
    return {"orders": []}

