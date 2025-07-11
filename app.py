from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from uvicorn import run as app_run

from typing import Optional

from src.constants import APP_HOST, APP_PORT
from src.pipline.prediction_pipeline import USvisaData, USvisaClassifier
from src.pipline.training_pipeline import TrainPipeline

app = FastAPI()

# Mount static folder
app.mount("/static", StaticFiles(directory="static"), name="static")

# Template folder
templates = Jinja2Templates(directory='templates')

# Allow all origins for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Form Data Class
class DataForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.continent: Optional[str] = None
        self.education_of_employee: Optional[str] = None
        self.has_job_experience: Optional[str] = None
        self.requires_job_training: Optional[str] = None
        self.no_of_employees: Optional[str] = None
        self.company_age: Optional[str] = None
        self.region_of_employment: Optional[str] = None
        self.prevailing_wage: Optional[str] = None
        self.unit_of_wage: Optional[str] = None
        self.full_time_position: Optional[str] = None

    async def get_usvisa_data(self):
        form = await self.request.form()
        self.continent = form.get("continent")
        self.education_of_employee = form.get("education_of_employee")
        self.has_job_experience = form.get("has_job_experience")
        self.requires_job_training = form.get("requires_job_training")
        self.no_of_employees = form.get("no_of_employees")
        self.company_age = form.get("company_age")
        self.region_of_employment = form.get("region_of_employment")
        self.prevailing_wage = form.get("prevailing_wage")
        self.unit_of_wage = form.get("unit_of_wage")
        self.full_time_position = form.get("full_time_position")


# Home Page
@app.get("/", tags=["Home"])
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "context": "Rendering"})


# Training Endpoint
@app.get("/train", tags=["Training"])
async def train_route():
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()
        return Response("✅ Model training completed successfully!")
    except Exception as e:
        return Response(f"❌ Training failed: {e}")


# Prediction Endpoint
@app.post("/", tags=["Prediction"])
async def predict_route(request: Request):
    try:
        form = DataForm(request)
        await form.get_usvisa_data()

        # Build input data
        usvisa_data = USvisaData(
            continent=form.continent,
            education_of_employee=form.education_of_employee,
            has_job_experience=form.has_job_experience,
            requires_job_training=form.requires_job_training,
            no_of_employees=form.no_of_employees,
            company_age=form.company_age,
            region_of_employment=form.region_of_employment,
            prevailing_wage=form.prevailing_wage,
            unit_of_wage=form.unit_of_wage,
            full_time_position=form.full_time_position,
        )

        # Convert to DataFrame
        usvisa_df = usvisa_data.get_usvisa_input_data_frame()

        # Predict using the model
        model_predictor = USvisaClassifier()
        prediction = model_predictor.predict(dataframe=usvisa_df)[0]

        # Map output
        status_map = {
            1: "Visa Approved",
            0: "Visa Not Approved"
        }
        status = status_map.get(prediction, "Prediction Error")

        return templates.TemplateResponse("index.html", {"request": request, "context": status})

    except Exception as e:
        return {"status": False, "error": str(e)}


# Run with uvicorn manually or through __main__
if __name__ == "__main__":
    app_run(app, host=APP_HOST, port=APP_PORT)
