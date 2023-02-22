FROM jupyter/scipy-notebook

RUN pip install joblib

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "api_server:app", "--host", "0.0.0.0", "--port", "80"]
