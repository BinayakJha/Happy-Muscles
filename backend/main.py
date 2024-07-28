import os
from typing import Union

# import openai
from fastapi import FastAPI
from extract import ans_chat
from replit.ai.modelfarm import ChatExample, ChatMessage, ChatModel, ChatSession
from fastapi.middleware.cors import CORSMiddleware

model = ChatModel("chat-bison")

class MyApp:
    def _init_(self):
        self.app = FastAPI()
        self._setup_middleware()
        self._setup_routes()
    
    def _setup_middleware(self):
        origins = [
            "http://localhost",
            "http://localhost:3000",
            "*",
        ]

        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    
    def _setup_routes(self):
        self.app.get("/")(self.read_root)
        self.app.get("/stretches/{body_part}/{age}/{weight}/{medications}")(self.stretches)
        self.app.get("/warmups/{body_part}/{age}/{weight}/{medications}")(self.warmups)
        self.app.get("/cooldowns/{body_part}/{age}/{weight}/{medications}")(self.cooldowns)

    async def read_root(self):
        return {"message": "Hello, world!"}
    
    async def stretches(self, body_part: str, age: int, weight: int, medications: str):
        question = (
            f"Suggest 3 Stretches for Having pain on {body_part} according to their age, "
            f"Age-> {age} years, Weight->{weight} kg, Medications: {medications}"
        )
        reformatted_ans = ans_chat(question=question)
        return {"question": question, "answer": reformatted_ans}
    
    async def warmups(self, body_part: str, age: int, weight: Union[int, float], medications: str):
        question = (
            f"Suggest 3-5 warm-up for {body_part} with a full tutorial on how to do it carefully pointwise. "
            f"My Medication -> {medications}. My Weight->{weight} kg, My Age-> {age}, My Goal->"
        )
        reformatted_ans = ans_chat(question=question)
        return {"question": question, "answer": reformatted_ans}

    async def cooldowns(self, body_part: str, age: int, weight: Union[int, float], medications: str):
        question = (
            f"Suggest 3-5 warm-up for {body_part} with a full tutorial on how to do it carefully pointwise. "
            f"My Medication -> {medications}. My Weight->{weight} kg, My Age-> {age}"
        )
        reformatted_ans = ans_chat(question=question)
        return {"question": question, "answer": reformatted_ans}

my_app = MyApp()
app = my_app.app 
