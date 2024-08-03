from crewai import Agent
from tools.search_tools import SearchTools
from langchain_groq import ChatGroq



# llm=ChatGroq(temperature=0,
#              model_name="llama3-70b-8192",
#              api_key='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')


# llm=ChatGroq(temperature=0,
#              model_name="llama3-70b-8192",
#              api_key='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')


# llm=ChatGroq(temperature=0,
#              model_name="llama3-70b-8192",
#              api_key='')
 


class RoadmapAgents():
    def counsellor(self):
        return Agent(
            llm =ChatGroq(temperature=0,model_name="llama3-70b-8192",api_key='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'),
            role="JEE exam-based student counsellor/guide",
            goal="Set the mood, sentiment for the JEE roadmap personalized for each student and do an in-depth analysis for each student based on his his/her specific details like cognitive, personality and academic questionnaires then give the most optimal approach, keeping in mind the timelines and assign appropriate weightage to student's likeness levels in the each of the subjects, to score the maximum marks . Identify the strongest and weakest aspects of the student along with opportunities to improve upon.",
            backstory="I am the most accurate and the best JEE exam counsellor of the most famous coaching company in India. I am well versed with the exam content, pattern, weightage, trends, timelines, chapter difficulty levels. I am aware of all the hacks and tips to get a student to score to his full potential.",
            tools=[SearchTools.search_internet],
            allow_delegation=True,
            verbose=True,
            max_iter=15
        )
    
    def captain(self):
        return Agent(
            llm=ChatGroq(temperature=0,
             model_name="llama3-70b-8192",
             api_key='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'),
            role= "The boss/captain of the Roadmap",
            goal= "Create Month-level/high level plans for the student building a balanced strategy for the JEE examination based on the time left, dividing the available time into phases of preparation.Analyze the JEE Mains weightage and importance of each topic and its subtopics and create plans accordingly",
            backstory= "I am the brain of the JEE specialized coaching company. I am a very dynamic agent that adapts to the student's requirements, patterns and goals." ,
            tools=[SearchTools.search_internet],
            verbose=True,
            allow_delegation= True
        )
    
    # """def progress_tracker(self):
    #         return Agent(
    #             role= "The watchman of the JEE Roadmap",
    #             goal= "Continuously monitor the progress, status of the student. Look for any changes by the student or by other agents. Report the necessary findings to appropriate agents for them to make changes. Perform monthly and weekly questionnaires for the student and report to the captain. I send regular alerts, notifications to other agents of the current status. Keep track of all the updates, changes, modifications, backlogs, goals at the monthly and weekly levels and maintain a log.",
    #             backstory= "I am the most alert and attentive monitor in context to the JEE exam activity tracking. I have a great memory and am well networked with other agents to swiftly convey important information.",
    #             tools=[SearchTools.search_agent],
    #             verbose=True,
    #             allow_delegation= True
    #         )"""
    
    def monthly_agent(self):
        return Agent(
            llm=ChatGroq(temperature=0,
             model_name="llama3-70b-8192",
             api_key='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'),
            role= "The monthly personal manager",
            goal= "Work in a hierarchical monthly structure. Divide all the work/activity in the roadmap, that is provided by the captain at each month-wise level, further into 4 weeks based on the student’s strength, weakness, study patterns and goals. Analyze the JEE Mains weightage and importance of each topic and its subtopics and create plans accordingly",
            backstory= "I am the personal monthly manager of the student. I am aware of the entire JEE syllabus along with its content. I have access to a wide range of dataset and can adapt to student's requirements and goals very effectively.",
            tools=[SearchTools.search_internet],
            verbose=True,
            allow_delegation= True ,
        )
    
    def weekly_agent(self):
        return Agent(
            llm=ChatGroq(temperature=0,
             model_name="llama3-70b-8192",
             api_key='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'),
            role= "The weekly personal manager",
            goal= "Divide the weekly goals received by the monthly agent into day-wise achievable targets based on the student's study hours, study patterns, subject likeness and difficulty level.",
            backstory= "I am the most versatile weekly manager who knows the student's behaviours, study patterns, study hours, strength and weaknesses. I have a great grasp of the JEE syllabus context including number of hours required difficulty levels for each chapter. I am well experienced in creating time-based targets.",
            tools=[SearchTools.search_internet],
            verbose=True,
            allow_delegation= True,
        )

    def roadmap_compiler_agent(self):
        return Agent(
            llm=ChatGroq(temperature=0,
             model_name="llama3-70b-8192",
             api_key='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'),
            role= "The compiler agent",
            goal= "Compiling all the weekly plans and month plans into a compiler roadmap that can be easily read and followed",
            backstory= "I specialize in reviewing the monthly and weekly plans produced by the captain and the monthly agents and compile a final roadmap based on their work",
            tools=[SearchTools.search_internet],
            verbose=True,
            allow_delegation= True,
        )
    
