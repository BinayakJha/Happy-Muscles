from replit.ai.modelfarm import ChatExample, ChatMessage, ChatModel, ChatSession

model = ChatModel("chat-bison")
response = model.chat([
  ChatSession(
    context="You are nepali text bot.",
    examples=[
      ChatExample(
        input=ChatMessage(content="1 + 1"),
        output=ChatMessage(content="2")
      )
    ],
    messages=[
      ChatMessage(author="USER", content="hajur ko haalkhabar ke cha?"),
    ],
  )
], temperature=0.2)

print(response.responses[0].candidates[0].message.content)
