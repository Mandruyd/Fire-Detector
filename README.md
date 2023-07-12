# Fire Detector - Next.js, Tailwind CSS, & FastAPI Application

Fire Detector is a web-based application that allows users to upload an image and detect the presence and location of fire within the image. The frontend is built using Next.js and Tailwind CSS, while the backend leverages FastAPI with a custom trained YOLOv5 model for image analysis. The application is fully dockerized for ease of deployment.


![showcase](https://i.imgur.com/KJfBtB1.png)


## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have installed Docker and Docker Compose. If not, follow the installation guide [here](https://docs.docker.com/get-docker/).
* You have a Linux/Mac machine with command-line access.

## Setup & Configuration

To use Fire Detector, follow these steps:

1. Clone the repository:
    ```
    git clone <repo-link>
    ```

2. Create a `.env` file in the root directory and set the required environment variables:
    ```env
    NEXT_PUBLIC_BACKEND_SERVICE_IP=backend-service-ip
    ```

`backend-service-ip` should be the DNS of your host server, its ip address or `localhost` if you are running this project locally.

## Running the application

To start the Fire Detector, run the following command in your terminal:

```bash
docker-compose up
```

The frontend should now be running at <host_ip>:8080. You can upload an image through the main page, and the application will respond with an edited image highlighting the presence and location of fire.

The code used for training the model can be fully seen in the Jupyter notebook found in the backend folder.

## Disclaimer

This project is not meant for production, it is only a proof of concept as I was trying to gasp my knowledge on the tehnology stack used on this project.
