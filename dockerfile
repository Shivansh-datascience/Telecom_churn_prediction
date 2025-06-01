FROM python:3.12-slim

#creating an container name as churn application
COPY . .

#setting working directory as churn application
WORKDIR /app

#adding the dependencies
RUN pip install -r requirements.txt

#assigning the command to run flask server
CMD [ "python","app.py" ]

EXPOSE 8085








