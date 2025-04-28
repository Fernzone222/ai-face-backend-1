from fastapi import FastAPI, UploadFile, File
from ai_generator import generate_profile_pictures
from payment import create_checkout_session, stripe_webhook

app = FastAPI()

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    content = await file.read()
    return {"message": "Upload successful"}

@app.post("/generate/")
def generate(file_url: str, style: str):
    images = generate_profile_pictures(file_url, style)
    return {"images": images}

@app.post("/create-checkout-session/")
def create_checkout():
    session_url = create_checkout_session()
    return {"sessionId": session_url, "publicKey": "pk_test_..."}  # placeholder

@app.post("/stripe-webhook/")
async def webhook(request):
    payload = await request.body()
    stripe_webhook(payload)
    return {"status": "ok"}
