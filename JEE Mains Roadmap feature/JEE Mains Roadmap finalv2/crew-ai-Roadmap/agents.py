from crewai import Agent
from tools.search_tools import SearchTools
from langchain_openai import ChatOpenAI

from langchain_groq import ChatGroq


# llm=ChatGroq(temperature=0,
#              model_name="llama3-70b-8192",
#              api_key='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')


llm=ChatGroq(temperature=0,
             model_name="llama3-70b-8192",
             api_key='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')


# llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0,api_key='sk-None-jXbxiHyllWiCEyh35xQcT3BlbkFJhYRylIJ3lcFZVO89NpYe')

class RoadmapAgents():
    def counsellor(self):
        return Agent(
            llm = llm,
            role='JEE Mains exam-based student counsellor/guide',
            goal='Set the mood, sentiment for the JEE roadmap personalized for each student doing an in-depth analysis and providing the most optimal approach.',

            # - Do an in-depth analysis for each student based on his his/her specific details like cognitive, personality and academic questionnaires.
            # - give the most optimal approach, keeping in mind the timelines and assign appropriate weightage to student's likeness levels in the each of the subjects, to score the maximum marks. 
            # - Identify the strongest and weakest aspects of the student along with opportunities to improve upon.
            # """,

            backstory="""
            I am the most accurate and the best JEE exam counsellor of the most famous coaching company in India. I am well versed with the exam content, pattern, weightage, trends, timelines, chapter difficulty levels.
            """,

            tools=[SearchTools.search_internet],
            allow_delegation=True,
            verbose=True,
            max_iter=5

        )
    


    def captain(self):
        return Agent(
            llm = llm,
            role= 'The boss/captain of the Roadmap',

            goal= 'Create Month-level/high level plans for the student building a balanced strategy for the JEE Mains examination.',

            # - Analyze the JEE Mains weightage and importance of each topic and its subtopics and create a high level plan that includes all the necessary guides, resources and action-plan for the month.
            # """,

            backstory= """
            I am the brain of the JEE specialized coaching company. I am a very dynamic agent that adapts to the student's requirements, patterns and goals.
            """,

            tools=[SearchTools.search_internet],
            verbose=True,
            allow_delegation= True
        )
    
    



    def monthly_agent(self):
        return Agent(
            llm = llm,
            role= 'The monthly manager',
            goal= 'Divide all the work/activity in the roadmap, that is provided by the captain further into 4 weeks.',


            # """
            # - Work in a hierarchical monthly structure. 
            # - 
            # - The division of the tasks are to be done to maximize the score of student based on their questionnaire, cognitive abilities, personality and routine behavior. 
            # - Provide necessary tools, resources, guides, books and online materials most important to excel in each specific topic.
            # """,

            backstory= "I am the personal monthly manager of the student. I am aware of the entire JEE syllabus along with its content.""",

            verbose=True,
            allow_delegation= True ,
        )
    
    def weekly_agent(self):
        return Agent(
            llm = llm,
            role= 'The weekly manager',
            
            goal= 'Divide the weekly goals received by the monthly agent into the 7 days Monday-Sunday, day-wise achievable targets. Do not provide an hourly time-table or routine.',

            backstory= """I am the most versatile weekly manager who knows the student's behaviours, study patterns, study hours, strength and weaknesses. I have a great grasp of the JEE syllabus context including number of hours required difficulty levels for each chapter. I am well experienced in creating time-based targets.""",

            verbose=True,
            allow_delegation= True,
        )

    def roadmap_compiler_agent(self):
        return Agent(
            llm = llm,
            role= 'JEE Roadmap compiler agent',

            goal= 'Compile all analyzed content into a final Roadmap. ',
            backstory= """As a final architect, I specialize in creating a detailed compilation of the Roadmap that captivates the students.""",

            tools=[SearchTools.search_internet],

            verbose=True,
            allow_delegation= True,
        )
    
    # def manager_agent(self):
    #     return Agent(
    #         role = "Manager,
    #         goal = "Manage the crew and ensure the opportunities report is based on strengths and challenges, and the actionables report is based on strengths, challenges and opportunities.",
    #         backstory = "Known as the best manager, you're experienced in overseeing complex projects and guiding teams to success. Your role is to coordinate the efforts of the crew members, ensuring that each task is completed on time and to the highest standard.",
    #         llm = llm,
    #         allow_delegation = False,
    #         verbose = True

    #     )
    

    # """def progress_tracker(self):
    # #         return Agent(
    # #             role= "The watchman of the JEE Roadmap",
    # #             goal= "Continuously monitor the progress, status of the student. Look for any changes by the student or by other agents. Report the necessary findings to appropriate agents for them to make changes. Perform monthly and weekly questionnaires for the student and report to the captain. I send regular alerts, notifications to other agents of the current status. Keep track of all the updates, changes, modifications, backlogs, goals at the monthly and weekly levels and maintain a log.",
    # #             backstory= "I am the most alert and attentive monitor in context to the JEE exam activity tracking. I have a great memory and am well networked with other agents to swiftly convey important information.",
    # #             tools=[SearchTools.search_agent],
    # #             verbose=True,
    # #             allow_delegation= True
    # #         )"""