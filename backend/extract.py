from replit.ai.modelfarm import ChatExample, ChatMessage, ChatModel, ChatSession

model = ChatModel("chat-bison")
def ans_chat(question):
  response = model.chat([
      ChatSession(
          context="You are Stretch Suggester for people when they have pain on some body parts according to their ages",
          
        examples=[
              ChatExample(input=ChatMessage(content="Having Pain On [Body Parts], My age is 45"),
              output=ChatMessage(content="""
here are some effective hamstring stretches:
\n
**Stretches:**

1. **Standing Hamstring Stretch:** 
   - Stand with your feet hip-width apart.
   - Keeping your back straight, bend at your hips and reach for your toes.
   - Hold for 15-20 seconds, feeling the stretch in your hamstrings.

2. **Leg Swings:** 
   - Hold onto a stable surface, like a wall or a bar.
   - Swing one leg forward and backward, gently increasing the range of motion.
   - Do this for about 20 seconds per leg.

3. **Knee Hug:** 
   - While standing, lift one knee towards your chest, holding it with your hands.
   - Hold for 15 seconds for each leg.

**Cool-down (after your workout):**

1. **Seated Hamstring Stretch:** 
   - Sit on the floor with your legs extended.
   - Reach for your toes and hold the stretch for 15-20 seconds.

2. **Lying Hamstring Stretch:** 
   - Lie on your back, and raise one leg while keeping it straight.
   - Gently pull it towards you using a towel or strap.
   - Hold for 15-20 seconds for each leg.

3. **Child's Pose:** 
   - Kneel on the floor, sit back on your heels, and reach your arms forward, lowering your chest towards the floor.
   - Hold for 20-30 seconds.

Remember to perform these stretches slowly and gently, without forcing any movement.
  """))
          ],
          messages=[
              ChatMessage(
                  author="USER",
                  content= question,
              )
          ],
      )
  ],
  temperature=0.7)
  
  return (response.responses[0].candidates[0].message.content)
