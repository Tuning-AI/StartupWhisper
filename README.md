# Startups Assistant

![Screenshot at 2023-09-15 20-17-23](https://github.com/Tuning-AI/startups_Assistant/assets/145156896/6283363c-d84a-4b7b-a32d-0a6e37ee2557)

## Overview
Welcome to the Startups Assistant project! This AI-powered assistant is designed to provide valuable information and support for startups, with a focus on Algerian tax law and startup-related topics.
## Model: **Llama2_13B_startup_Assistant**
The heart of this assistant is the Llama2_13B_startup_Assistant language model. It has been fine-tuned using a custom dataset and the innovative QLORA (Quantized LoRA) fine-tuning technique. This model is capable of generating both text and audio outputs, enhancing the user experience.
https://huggingface.co/TuningAI/Llama2_13B_startup_Assistant
## Features
* **Text Output**: Get detailed and informative responses to your startup-related questions.
* **Audio Output**: For those who prefer to listen, our assistant can provide spoken answers, making information accessible in multiple ways.
## Fine-tuning Technique
The QLORA technique extends the principles of LoRA and introduces 4-bit NormalFloat (NF4) quantization, optimizing parameter efficiency during fine-tuning. This ensures that our assistant delivers relevant and reliable insights
## Dataset:
This model was fine-tuned on a custom dataset meticulously curated with 200 unique examples. The dataset incorporates both manual entries and contributions from GPT3.5, GPT4, and Falcon 180B models.
https://huggingface.co/datasets/TuningAI/Startups_V2

## Use Cases
* **Startup Guidance**: Receive advice and recommendations for your startup journey.
* **Algerian Startups Tax Law**: Get assistance in navigating tax laws and regulations specific to Algeria.
* **Business Insights**: Access valuable insights for making informed business decisions.
## Limitations
It's important to note that while our assistant is a powerful tool, it's not without limitations. It may not always provide perfect answers, and its knowledge is based on the data it was trained on. Additionally, its performance can vary depending on the complexity of the queries.
## Frameworks
+ **Langchain**: We've implemented Langchain for the chat functionality, enabling smooth interactions with the assistant.
+ **Transformers**: The Transformers library is the backbone for fine-tuning and integrating advanced language models into our project.
+ **Streamlit**: For an interactive and user-friendly interface, we've incorporated Streamlit. This web app framework simplifies the presentation of our assistant, making it accessible and engaging for users.
