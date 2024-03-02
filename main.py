from fastapi import FastAPI

app = FastAPI()

@app.get("/get_recent_data")
async def get_recent_data():
    # Here you can implement the logic to retrieve the recent data based on the int_value received
    # For demonstration purposes, let's just print the received value and return a dummy response
    # print(f"Received int_value: {int_value}")
    recent_data = {"data": 1}  # Dummy data
    return recent_data
