from fastapi import FastAPI, UploadFile, File
import cv2
import numpy as np

# Create the web application engine
app = FastAPI()

@app.get("/")
def check_status():
    return {"status": "Your Grading Backend is Live!"}

@app.post("/analyze")
async def analyze_card(file: UploadFile = File(...)):
    # 1. Read the image file sent from the phone
    file_bytes = await file.read()
    nparr = np.frombuffer(file_bytes, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # 2. Get the dimensions of the uploaded image
    height, width, _ = image.shape
    
    # 3. Running our basic boundary placeholder logic
    # For now, we will simulate a clean 52/48 alignment split
    left_ratio = 52.5
    right_ratio = 47.5
    
    # 4. Reply back to the mobile phone with text data
    return {
        "left_right_ratio": f"{left_ratio:.1f} / {right_ratio:.1f}",
        "top_bottom_ratio": "50.0 / 50.0",
        "verdict": "Excellent Centering! Strong Grade Candidate."
    }