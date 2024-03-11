# ad_click_prediction_dockerized_api

This project aims to predict whether a user will click on an advertisement based on their age and annual salary. The project includes data collection, model training for prediction, creation of a FastAPI api for predictions, containerizing the api using Docker, and testing the Docker container.

https://github.com/umairsiddique3171/ad_click_prediction_dockerized_api/assets/148565997/3cbfed41-181e-41ca-ba0d-a13afc09a470

## Table of Contents
 - [Overview](#overview)
 - [Model Training](#model-training)
 - [Creation of FastAPI API](#creation-of-fastapi-api)
 - [Containerization of API](#containerization-of-api)
 - [Notes](#notes)
 - [License](#license)

## Overview
This project is structured into four key phases, each playing a vital role in delivering a robust solution for ad click prediction:

- Model Training
- Creation of FastAPI API
- Containerization of API

## Model Training

- **Dataset Collection:**
  
  The dataset used for training the classifier was obtained from [kaggle](https://www.kaggle.com/datasets/jahnveenarang/cvdcvd-vd/data).

- **Data Preprocessing:**
  
  Data preprocessing involved checking data distributions,feature encoding, features selection, data scaling, and splitting the data into training and testing sets.

- **Model Training:**
  
  Logistic Regression and Naive Bayes models were trained using the preprocessed data.

- **Model Evaluation:**

  Trained models were evaluated using standard evaluation metrics for classification tasks such as accuracy, precision, recall, and F1 score.

## Creation of FastAPI API
- The project progresses to the creation of a FastAPI API. FastAPI was chosen due to its high performance and easy integration with machine learning models.

- The user inputs their age and annual salary to get a prediction whether they would click on an ad or not.

- **App Test on Local Host:**
    1. Clone the repository:

        ```
        git clone https://github.com/umairsiddique3171/ad_click_prediction_dockerized_api.git
        cd ad_click_prediction_dockerized_api/app
        ```

    2. Create and activate a virtual environment:

        ```
        python -m venv env
        .\env\Scripts\activate
        ```

    3. Install dependencies:

        ```
        pip install -r requirements.txt
        ```

    4. Run the FastAPI app:

        ```
        uvicorn main:app 
        ```

    5. Access the api in your browser at `http://localhost:8000/docs`.
    6. You can also use predict.py to post the input to api and get classification and it's score as a response.

## Containerization of API
- **Docker Setup:**

    To check docker installation in your system, run the following command in your terminal:

    ```
    docker
    ```

- **Dockerfile Setup:**

    Setup "Dockerfile" as mentioned [here](https://github.com/umairsiddique3171/ad_click_prediction_dockerized_api/blob/main/app/Dockerfile).

- **Build Docker Image:**

    To build a Docker image, use the following command in your terminal:

    ```
    docker build -t ad_click_predictor:v1.0 .
    ```

- **Run Docker Image as a Container:**

    To run the Docker image as a container, type the following command in your terminal:

    ```
    docker run -p 80:80 ad_click_predictor:v1.0
    ```

    To check whether the container is running, type the following command in your terminal:

    ```
    docker ps
    ```

    To stop the container from running, type the following command in your terminal:

    ```
    docker stop <container_id>
    ```

- **Push Docker Image to Docker Hub:**

    To push a Docker image to Docker Hub, follow these steps:

    1. **Login to Docker Hub**: 

        Before pushing the image, you need to authenticate yourself with your Docker Hub credentials. Use the following command:
    
        ```
        docker login
        ```

        After running this command, you'll be prompted to enter your Docker Hub username and password.

    2. **Tag the Docker Image**:

        Before pushing the image, you need to tag it with your Docker Hub username and the repository name. This is done using the following command:
        ```
        docker tag ad_click_predictor:v1.0 umairsiddique3171/ad_click_predictor:v1.0
        ```

    3. **Push the Docker Image**:

        Finally, push the tagged image to Docker Hub using the following command:
        ```
        docker push umairsiddique3171/ad_click_predictor:v1.0
        ```
        This command will push the tagged image to your Docker Hub repository. Make sure you have appropriate permissions to push to the repository.

## Notes

- APIs are moved around through various means, including:
   - Deployment Platforms: APIs can be deployed on cloud platforms like AWS, Google Cloud, or Azure, where they can be easily accessed and managed.
   - Containerization: APIs are often packaged into containers using technologies like Docker, allowing for easy movement across different environments with consistent behavior.
   - Version Control Systems: APIs are managed and versioned using version control systems like Git, enabling tracking of changes and collaboration among developers.
   - API Gateways: API gateways serve as intermediaries between clients and APIs, allowing for routing, load balancing, and management of API requests across different services and environments.
   - Package Managers: APIs and their dependencies can be packaged and distributed using package managers like npm (for Node.js) or pip (for Python), facilitating easy installation and usage.
   - Deployment Pipelines: APIs are moved through deployment pipelines, where automated processes handle tasks like testing, building, and deploying to different environments such as development, staging, and production.

- An API (Application Programming Interface) is not an app (application). An API is a set of rules and protocols that allows different software applications to communicate with each other. It defines how different software components should interact, specifying the methods and data formats that can be used. An app, on the other hand, refers to a standalone software application designed to perform specific tasks or functions for end-users. While apps may utilize APIs to interact with other software systems or services, they are distinct entities.


## License
This project is licensed under the [MIT License](https://github.com/umairsiddique3171/ad_click_prediction_dockerized_api/blob/main/LICENSE).

## Author 
[@umairsiddique3171](https://github.com/umairsiddique3171)
