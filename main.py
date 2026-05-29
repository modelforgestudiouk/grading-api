from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# This tells the server to accept data from any phone browser without blocking
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "Your Grading Backend is Live!"}

@app.post("/analyze")
async def analyze_card(file: UploadFile = File(...)):
    # This is a temporary placeholder result that will show up on your phone screen!
    return {
        "left_right_ratio": "52/48",
        "top_bottom_ratio": "50/50",
        "verdict": "Excellent (Potential PSA 10 Centering)"
    }
