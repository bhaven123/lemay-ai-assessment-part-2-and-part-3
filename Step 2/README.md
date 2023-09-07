# Model Deployment Demonstration

## Reasons for choosing the model

The reason for choosing the model [bert-based-uncased](https://huggingface.co/bert-base-uncased) was because recently I was going through the Hugging Face NLP course which has detailed information about transformer models, their usage, use of the pipeline() function, use of tokenizers and other pretrained models available on the Hugging Face hub and also because BERT is a transformers model pretrained on a large corpus of English data in a self-supervised fashion and it was pretrained with two objectives: Masked language modeling (MLM) and Next sentence prediction (NSP).

## Installing and Running the Demo

Steps to create the docker image and run the docker container:

- First, we clone the repository using the command

  ```
  git clone repository-url
  ```

  You can open it using **Visual Studio Code** or any editor of your choice. Navigate to Step 2 directory.

- We need to have docker installed on our system. The docker image can either be created (in the root directory which has the Dockerfile) using the command

  ```
  docker build -t name-of-your-image .
  ```

- Once we have the image, we can run it inside a container using the command

  ```
  docker run -d --name name-of-your-container -p 80:80 name-of-your-image
  ```

Steps to make **POST** requests to the container endpoint:

Now that we have our container running, we can start making POST requests to it. This can be done in the following ways:

- Open the notebook request.ipynb. Run all the cells of the notebook to make a POST request to the endpoint and receive a response.
