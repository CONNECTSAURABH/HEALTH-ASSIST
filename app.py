from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

chatHistory = []
print("Hello I am Health Assist!\n")
system_msg = SystemMessage(content="You are Health Assisting AI. You Solve Health Realted Queries Only.") 
chatHistory.append(system_msg)

while True:
    query = input("You:  ")
    if query.lower()=="exit":
        break
    chatHistory.append(HumanMessage(content=query))
    
    result = model.invoke(query)
    response = result.content
    chatHistory.append(AIMessage(content=response))
    print(f"AI Response: {response}")
    
    
print ("-----------------------------Message history -----------------------------")
print(f"Whole History: {chatHistory}")

    

