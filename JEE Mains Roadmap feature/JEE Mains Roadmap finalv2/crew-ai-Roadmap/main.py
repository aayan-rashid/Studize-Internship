from crewai import Crew, Process
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from file_io import save_markdown


from agents import RoadmapAgents
from tasks import RoadmapTasks


llm=ChatGroq(temperature=0,
             model_name="llama3-70b-8192",
             api_key='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')


#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

# llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0,api_key='sk-None-jXbxiHyllWiCEyh35xQcT3BlbkFJhYRylIJ3lcFZVO89NpYe')



print("")

print("Welcome to the Studize JEE Roadmap!")
print("-----------------------------------")

print("")
print("")

print("Answer the following questions to get your Personalised JEE Roadmap tailored to your need:")
print("-----------------------------------")

print("")

home_state = input("What is your Home state?")
print("")
category = input("Which category do you belng to?")
print("")
gender = input("What is your gender?")
print("")
year_of_exam = input("Which year are you going to give your JEE Mains exam?")
print("")
fav_sub = input("Which is your most favourite subject?")
print("")
least_fav_sub = input("Which is your least favourite subject?")
print("")
confidence_lvl_phy = input("What is your confidence level in Physics - low, medium, high?")
print("")
confidence_lvl_chem = input("What is your confidence level in Chemistry - low, medium, high?")
print("")
confidence_lvl_maths = input("What is your confidence level in Maths - low, medium, high?")
print("")
avg_score = input("What is your current average score?")
print("")
target_score = input("What is your target score for the JEE Mains exam?")
print("")
coaching = input("Do you take any coaching for JEE?")
print("")
hours_of_study = input("How many hours a day do you study on weekdays?")
print("")
hours_of_study_weekends = input("How many hours a day do you study on weekends?")
print("")
target_college = input("Do you have a target college in mind?")
print("")
strengths = input("What according to you are your strengths on basis of - memory, visualization, problem solving, retention, speed, accuracy, calculation, concept understanding?")
print("")
weaknesses = input("What according to you are your weaknessess on basis of - memory, visualization, problem solving, retention, speed, accuracy, calculation, concept understanding?")
print("")




user_input = {
    "year_of_exam": year_of_exam,
    "fav_sub": fav_sub,
    "least_fav_sub": least_fav_sub,
    "confidence_lvl_phy": confidence_lvl_phy,
    "confidence_lvl_chem": confidence_lvl_chem,
    "confidence_lvl_maths": confidence_lvl_maths,
    "avg_score": avg_score,
    "target_score": target_score,
    "coaching": coaching,
    "hours_of_study": hours_of_study,
    "hours_of_study_weekends": hours_of_study_weekends,
    "home_state": home_state,
    "category": category,
    "gender": gender,
    "target_college": target_college,
    "strengths": strengths,
    "weaknesses": weaknesses
}



agents = RoadmapAgents()
tasks = RoadmapTasks()



# Agents
counsellor = agents.counsellor()
captain = agents.captain()
monthly_agent = agents.monthly_agent()
weekly_agent = agents.weekly_agent()
roadmap_compiler_agent = agents.roadmap_compiler_agent()



# Tasks
sentiment_analysis = tasks.sentiment_analysis(counsellor, user_input)
high_level_plan = tasks.high_level_plan(captain, [sentiment_analysis])
month_level_plan = tasks.month_level_plan(monthly_agent, [high_level_plan])
week_level_plan = tasks.week_level_plan(weekly_agent, [month_level_plan])
compiled_roadmap = tasks.compile_roadmap(roadmap_compiler_agent, [week_level_plan], save_markdown)



# Build the crew
crew = Crew(
            agents=(counsellor, captain, monthly_agent, weekly_agent, roadmap_compiler_agent),
            tasks=(sentiment_analysis, high_level_plan, month_level_plan, week_level_plan, compiled_roadmap),

            process=Process.hierarchical,
            manager_llm=llm,
            verbose=True
        )



# Crew Run
result = crew.kickoff()

print("Studize JEE Roadmap:")
print(result)