
#Using OpenAi API for LLM:
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o-mini", api_key="Insert OpenAiApi Key here", max_tokens=256)
llm.invoke("hello").content


#Alternatively, Using Groq for LLM:
from langchain_groq import ChatGroq

UltimateSmallTalker = ChatGroq(
    model="llama-3.3-70b-versatile",  # Model name for LLM
    temperature=0.5,                  # Temperature setting for text generation randomness
    api_key="insert your groq api key",  # API key for accessing the LLM service
)