import os
from typing import Union

# import openai
from fastapi import FastAPI
from extract import ans_chat

# openai.api_key = os.environ['OPENAI_API']

from replit.ai.modelfarm import ChatExample, ChatMessage, ChatModel, ChatSession

from fastapi.middleware.cors import CORSMiddleware

model = ChatModel("chat-bison")

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message": "Hello, world!"}


# Old Peoples Stretches
@app.get("/stretches/{body_part}/{age}/{weight}/{medications}")
async def stretches(body_part: str, age: int, weight:int, medications: str):
    question = f"Suggest 3 Stretches for Having pain on {body_part} according to their age, Age-> {age} years,, Weight->{weight} kg, Medications: {medications}"

    reformatted_ans = ans_chat(question=question)
    
    return {"question": question, "answer": reformatted_ans}


# This is for the other things like gym or cardio
@app.get("/warmups/{body_part}/{age}/{weight}/{medications}")
async def warmups(body_part: str, age:int, medications: str, weight: Union[int, float]):
    question = f"Suggest 3-5 warm-up for {body_part} with a full tutorial on how to do it carefully pointwise. My Medication -> . My Weight->{weight} kg weight, My Age-> {age}, My Goal->"
    # response = openai.Completion.create(
    #     engine="text-davinci-003",
    #     prompt=question,
    #     max_tokens=200,
    #     n=1,
    #     stop=None,
    #     temperature=0.7
    # )
    reformatted_ans = ans_chat(question=question)

    return {"question": question, "answer": reformatted_ans}

@app.get("/cooldowns/{body_part}/{age}/{weight}/{medications}")
async def warmups(body_part: str, age:int, medications: str, weight: Union[int, float]):
  question = f"Suggest 3-5 warm-up for {body_part} with a full tutorial on how to do it carefully pointwise. My Medication -> . My Weight->{weight} kg weight, My Age-> {age}"
  # response = openai.Completion.create(
  #     engine="text-davinci-003",
  #     prompt=question,
  #     max_tokens=200,
  #     n=1,
  #     stop=None,
  #     temperature=0.7
  # )
  reformatted_ans = ans_chat(question=question)

  return {"question": question, "answer": reformatted_ans}