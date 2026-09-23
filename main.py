# 0
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()  # reads your .env file so GROQ_API_KEY is available
from langchain_core.messages import AIMessage ,SystemMessage , HumanMessage
llm = ChatGroq(model="openai/gpt-oss-20b" , temperature=0.9)

messages = [
    SystemMessage(content="You are Funny Ai agent")
]


print("--------------Welcome type 0 to exit the application------------- ")
while True:
    prompt = input("you : ")
    messages.append(HumanMessage(content=prompt))
   
    if prompt == "0":
        break
    response = llm.invoke(messages)
    messages.append(AIMessage(content=response.content))

    print("Bot :", response.content)

print(messages)