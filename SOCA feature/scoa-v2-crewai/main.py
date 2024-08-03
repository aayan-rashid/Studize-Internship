from crewai import Agent, Task, Crew, Process
# from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from textwrap import dedent
from agents import SCOAAgents
from tasks import SCOATasks
# import os
# from dotenv import load_dotenv
# load_dotenv()

class SCOACrew:
    def __init__(self, academic_scores, study_profile, cognitive_inputs):
        self.academic_scores = academic_scores
        self.study_profile = study_profile
        self.cognitive_inputs = cognitive_inputs

    def run(self):
        agents = SCOAAgents()
        tasks = SCOATasks()

        strengths_analyst_agent = agents.strengths_analyst_agent()
        challenges_analyst_agent = agents.challenges_analyst_agent()
        opportunities_analyst_agent = agents.opportunities_analyst_agent()
        actionables_analyst_agent = agents.actionables_analyst_agent()
        manager_agent = agents.manager_agent()

        strength_analysis_task = tasks.strength_analysis_task(
            strengths_analyst_agent,
            self.academic_scores,
            self.study_profile,
            self.cognitive_inputs
        )

        challenges_analyst_task = tasks.strength_analysis_task(
            challenges_analyst_agent,
            self.academic_scores,
            self.study_profile,
            self.cognitive_inputs
        )

        opportunities_analysis_task = tasks.opportunities_analysis_task(
            opportunities_analyst_agent,
            self.academic_scores,
            self.study_profile,
            self.cognitive_inputs,
            [strength_analysis_task, challenges_analyst_task]
        )

        actionables_analysis_task = tasks.actionables_analysis_task(
            actionables_analyst_agent,
            # self.academic_scores,
            # self.study_profile,
            # self.cognitive_inputs,
            [strength_analysis_task, challenges_analyst_task, opportunities_analysis_task]
        )

        crew = Crew(
            agents = [strengths_analyst_agent, challenges_analyst_agent, opportunities_analyst_agent, actionables_analyst_agent],
            tasks = [strength_analysis_task, challenges_analyst_task, opportunities_analysis_task, actionables_analysis_task],
            process=Process.hierarchical,
            manager_agent=manager_agent,
            manager_llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash"),
            # manager_llm=ChatGroq(
            #     temperature=0.7,
            #     model_name="llama3-70b-8192",
            #     api_key=os.environ.get("GROQ_API_KEY")
            # ),
            verbose= True
        )

        result = crew.kickoff()
        return result
    
if __name__ == "__main__":
    print("## Welcome to SCOA Analyser!")
    print('-------------------------------')


    academic_scores = {
        'maths': {},
        'physics': {},
        'chemistry': {}
    }
    study_profile = {}
    cognitive_inputs = {}
    

    physics_topics = [
        "Kinematics", "Mechanics", "Waves and Fluid Mechanics", "Thermodynamics",
        "Electricity and Electrostatics", "Electromagnetism", "Optics", "Modern Physics"
    ]

    chemistry_topics = [
        "11th Physical Chemistry", "11th Inorganic Chemistry", "11th Organic Chemistry",
        "12th Physical Chemistry", "12th Inorganic Chemistry", "12th Organic Chemistry"
    ]

    maths_topics = [
        "Sets, Relations and Functions", "Algebra", "Trigonometry", "Coordinate Geometry",
        "Differential Calculus", "Integral Calculus", "Vector Algebra and 3D Geometry",
        "Statistics and Probability"
    ]

    study_profile_prompts = {
        'time_division': "How do you divide your study time among Physics, Chemistry and Mathematics for JEE ? (Allocate Percentage)",
        'mock_test_frequency': "How often do you use mock tests and past question papers for JEE preparation ?",
        'progress_monitoring': "How do you monitor your progress in JEE topics or chapters",
        'study_methods': "How do you adjust your study methods for difficult or new JEE topics ?",
        'study_techniques': "What techniques do you use to remember JEE concepts and formulas for a long time ? eg: Revise frequently, Mindmap, etc."
    }

    cognitive_inputs_prompts = {
        'problem_solving_approach': "When faced with complex,multi-stemp problems in JEE, how likely are you to approach problem-solving systematically, breaking down each step ?",
        'thorough_understanding': "In your JEE preparation, how likely are you to ensure thorough understanding of fundamental concepts before moving on to advanced topics ?",
        'feedback': "How likely are you to integrate feedback from practice tests or teachers into your JEE preparation strategy ?",
        'misconception': "When encountering a misconception or misunderstanding in a JEE concept, how likely are you to identify and resolve it ?",
        'time_management': "How likely are you to effectively manage time during JEE exams, especially in sections with limited time constraints?"
    }



    # Collect confidence scores for each subject
    print("\nEnter your confidence scores for Physics topics:")
    for topic in physics_topics:
        academic_scores['physics'][topic] = input(dedent(f"Rate your confidence in {topic} (1-10): "))

    print("\nEnter your confidence scores for Chemistry topics:")
    for topic in chemistry_topics:
        academic_scores['chemistry'][topic] = input(dedent(f"Rate your confidence in {topic} (1-10): "))

    print("\nEnter your confidence scores for Maths topics:")
    for topic in maths_topics:
        academic_scores['maths'][topic] = input(dedent(f"Rate your confidence in {topic} (1-10): "))

    print("\nAnswer the following study profile questions:")
    for key, prompt in study_profile_prompts.items():
        study_profile[key] = input(dedent(prompt))

    print("\nAnswer the following cognitive questions:")
    for key, prompt in cognitive_inputs_prompts.items():
        cognitive_inputs[key] = input(dedent(prompt))


    # Create an instance of SCOACrew and run the process
    scoa_crew = SCOACrew(academic_scores, study_profile, cognitive_inputs)
    result = scoa_crew.run()
    print(result)