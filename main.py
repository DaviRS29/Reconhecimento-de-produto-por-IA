from fastapi import FastAPI, UploadFile, File
from ultralytics import YOLO
from PIL import Image
import io

app = FastAPI()

model = YOLO("best.pt")

@app.get("/")
def home():
    return {"msg": "API funcionando"}

@app.post("/detectar")
async def detectar(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")

    results = model(image)

    melhor = None

    for r in results:
        for box in r.boxes:
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            nome = model.names[cls]

            
            if conf < 0.6:
                continue

            if melhor is None or conf > melhor["confianca"]:
                melhor = {
                    "produto": nome,
                    "confianca": conf
                }

    if melhor is None:
        return {
            "produto": None,
            "confianca": 0
        }

    return melhor