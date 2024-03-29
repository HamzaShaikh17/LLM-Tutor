# Use a pipeline as a high-level helper
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from yt_recommendation import recommendations
from mongoDB_query import db_update
from image_extract import image_text

pipe = pipeline("conversational", model="microsoft/GODEL-v1_1-large-seq2seq")
tokenizer = AutoTokenizer.from_pretrained("microsoft/GODEL-v1_1-large-seq2seq")
model = AutoModelForSeq2SeqLM.from_pretrained("microsoft/GODEL-v1_1-large-seq2seq")

app = FastAPI()
class newList(BaseModel):
  #query: str
  #knowledge: str
  query: str
  user_id:str


@app.post("/items/")
async def read_items(q: newList):

    query = q.query
    user_id = q.user_id
    videos = recommendations(query)
    
    instruction = "Give answer like you are helping a school child to help a problem. Detect mathematics terminology in the question and response accordingly"
    # knowledge = knowledge_dict[feel]
    knowledge = ""


    dialog = [q.query]
    if knowledge != '':
        knowledge = '[KNOWLEDGE] ' + knowledge
    dialog = ' EOS '.join(dialog)

    query = f"{instruction} [CONTEXT] {dialog} {knowledge}"
    input_ids = tokenizer(f"{query}", return_tensors="pt").input_ids
    outputs = model.generate(input_ids, max_length=128, min_length=8, top_p=0.9, do_sample=True)
    output = tokenizer.decode(outputs[0], skip_special_tokens=True)

    db_update(user_id,dialog,output)
    return {
        "response" : output,
        "videos":videos
    }    

    



