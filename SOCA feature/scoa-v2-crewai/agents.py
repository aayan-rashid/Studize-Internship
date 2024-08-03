from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_groq import ChatGroq
# from tools.rag_tool import SearchTools
# from dotenv import load_dotenv
# import os

# load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
# llm = ChatGroq(
#     temperature=0.7,
#     model_name="llama3-70b-8192",
#     api_key=os.environ.get("GROQ_API_KEY")
# )
# search_tools = SearchTools()

class SCOAAgents:
    def strengths_analyst_agent(self):
        return Agent(
            role = "The best student strengths analyser.",
            goal = "Provide our user the best strengths report based on his responses.",
            backstory = "Known as the best student performance analyser, you're skilled in identifying the core strengths of a student by analysing his/her academic confidence scores, cognitive and study profile responses and also comparing with the benchmark data you have.",
            llm = llm,
            allow_delegation = True,
            verbose = True
            )
    
    def challenges_analyst_agent(self):
        return Agent(
            role = "The best student challenges analyser.",
            goal = "Provide our user the best challenges report based on his responses.",
            backstory = "Known as the best student performance analyser, you're skilled in identifying the core challenges of a student by analysing his/her academic confidence scores, cognitive and study profile responses and also comparing with the benchmark data you have.",
            llm = llm,
            allow_delegation = True,
            verbose = True
        )
    
    def opportunities_analyst_agent(self):
        return Agent(
            role = "The best student opportunities analyser.",
            goal = "Provide our user the best opportunities report based on his responses.",
            backstory = "Known as the best student performance analyser, you're skilled in identifying the core opportunities for a student by analysing his/her academic confidence scores, cognitive and study profile responses and also comparing with the benchmark data you have.",
            llm = llm,
            allow_delegation = True,
            verbose = True
        )
    
    def actionables_analyst_agent(self):
        return Agent(
            role = "The best actionables creator for the student.",
            goal = "Provide our user the best actionables report based on his strengths, challenges, opportunities reports.",
            backstory = "Known as the best student coach, you're skilled in preparing a high quality set of actionables based on the student's strengths, challenges and opportunities reports prepared by your colleague agents.",
            llm = llm,
            allow_delegation = True,
            verbose = True
        )
    
    def manager_agent(self):
        return Agent(
            role = "Manager",
            goal = "Manage the crew and ensure the opportunities report is based on strengths and challenges, and the actionables report is based on strengths, challenges and opportunities.",
            backstory = "Known as the best manager, you're experienced in overseeing complex projects and guiding teams to success. Your role is to coordinate the efforts of the crew members, ensuring that each task is completed on time and to the highest standard.",
            llm = llm,
            allow_delegation = False,
            verbose = True

        )

