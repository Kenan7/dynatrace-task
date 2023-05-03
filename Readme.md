# Dynatrace Internship Task - Backend

## Build and run

If you have docker installed, you can run the following command to build and run the application:

```bash
docker-compose up --build
```

No docker? No problem! Just get your python environment **ready, activate it** and run the following commands:

```bash
pip install -r requirements.txt
uvicorn main:app
```

## Usage

The application is running on port 8000. You can access the API documentation on [localhost:80/docs](http://localhost:8000/docs)

## Testing

To run the tests, just run the following command:

```bash
pytest
```

## Demo

![demo1_image_swagger](/demo_screenshots/Screenshot%202023-05-03%20at%207.07.56%20PM.png)
![demo2_image_swagger](/demo_screenshots/Screenshot%202023-05-03%20at%207.08.05%20PM.png)

## FAQ

### I am getting platform error while running docker-compose up

This is because the docker-compose file is configured to run on linux. If you are on windows, you can change the platform to windows in the docker-compose file.

Either remove the platform line or change it to your own choice.
