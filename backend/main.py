from fastapi import FastAPI

#this creates a new FastAPI app (my web server)
app = FastAPI()

#this says: when someone visits the main page (/), run the function below
@app.get("/")

#this function returns a message
def read_root():
    return {"message": "Hello from GRC platform!"}

@app.get("/health")
def health_check():
    return {"status":"healthy"}