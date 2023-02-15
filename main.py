from fastapi import FastAPI


import app as app
import motor.motor_asyncio



client = motor.motor_asyncio.AsyncIOMotorClient
("mongodb://Aboba:89210408@127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000")

@app.get("/myget")
async def get_int(user_id: int):
    return user_id