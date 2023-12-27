from replit.ai.modelfarm import ChatExample, ChatMessage, ChatModel, ChatSession

model = ChatModel("chat-bison")
response = model.chat([
  ChatSession(
    context="You are news bot.",
    examples=[
      ChatExample(
        input=ChatMessage(content="1 + 1"),
        output=ChatMessage(content="2")
      )
    ],
    messages=[
      ChatMessage(author="USER", content="Yesterday December 26, 2023 news kathmandu news with the dates with the source too"),
    ],
  )
], temperature=0.2)

print(response.responses[0].candidates[0].message.content)
