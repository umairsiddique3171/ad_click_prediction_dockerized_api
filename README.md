# ad_click_prediction_dockerized_api

This project aims to predict whether a user will click on an advertisement based on their age and annual salary. The project includes data collection, model training for prediction, creation of a FastAPI api for predictions, containerizing the api using Docker, and testing the Docker container.

## Table of Contents
 - [Overview](#overview)
 - [Model Training](#model-training)
 - [Creation of FastAPI API](#creation-of-fastapi-api)
 - [Containerization of API](#containerization-of-api)
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
        git clone https://github.com/your_username/ad_click_prediction.git
        cd ad_click_prediction/app
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
        uvicorn main:app --reload
        ```

    5. Access the app in your browser at `http://localhost:8000`.

## Containerization of API
- **Docker Setup:**

    To check docker installation in your system, run the following command in your terminal:

    ```
    docker
    ```

- **Dockerfile Setup:**

    Setup "Dockerfile" as mentioned [here]().

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

## License
This project is licensed under the [MIT License]().

## Author 
[@umairsiddique3171]()
