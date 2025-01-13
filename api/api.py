from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.culinarycrew.crew import Culinarycrew
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

class IngredientsRequest(BaseModel):
    ingredients: str

@app.post("/generate-recipe")
async def generate_recipe(data: IngredientsRequest):
    try:
        crew_instance = Culinarycrew().crew()

        inputs = {'ingredients': data.ingredients}

        results = crew_instance.kickoff(inputs=inputs)
        
        return {"data": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
