from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Food(BaseModel):
    name: str
    price: float
    description: Union[str, None] = None


app = FastAPI()


@app.get("/animal/{animal_id}")
async def read_animal(animal_id: int):
    """
    Read animal identifier

    - **animal_id**: animal identifier
    """
    return {"animal_id": animal_id}


@app.get("/animal_info")
async def read_info_animal(name: str, age: int = 1, mood: Union[str, None] = None):
    """
    Read information about animal

    - **name**: animal name
    - **age**: animal age
    - **mood**: current mood of animal
    """
    if mood:
        return {"dog_name": name, "age": age, "mood": mood}
    return {"dog_name": name, "age": age}


@app.post("/create_food")
async def create_animal_food(food: Food):
    """
    Create animal food

    - **name**: food name
    - **description**: food description
    - **price**: price of food
    """
    return food
