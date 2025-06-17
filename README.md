# Chatbot_Generative_AI

# How to run?
### STeps:

clone the repository

```bash
Project repo: https://github.com/shashanksnaik07/Chatbot_Generative_AI
```

### step 1 - create a conda environment after opening the repo

```bash
conda create -n medbot python=3.10
```

```bash
conda activate medbot
```
### step 2 - install the requirements
```bash
pip install -r requirements.txt
```
### Create a `.env` file in the root directory and add your pinecone api and openai api key as follows:

```ini
PINECONE_API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXX"
OPENAI_API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXX"
```

```bash
# Run the following command to stiore embeddings to pinecone 
python store_index.py
```

```bash 
# finally run the following command 
python app.py
```

Now,
```bash
open up localhost:8000
```

### TechStack Used:

- Python
- LangChain
- Flask
- GPT
- Pinecone

