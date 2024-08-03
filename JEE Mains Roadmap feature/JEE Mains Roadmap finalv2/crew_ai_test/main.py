from crewai import Crew, Process
from langchain_groq import ChatGroq
from agents import RoadmapAgents
from tasks import RoadmapTasks


llm=ChatGroq(temperature=0,
             model_name="llama3-70b-8192",
             api_key='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')




agents=RoadmapAgents()
tasks=RoadmapTasks()

counsellor = agents.counsellor()
captain = agents.captain()
monthly_agent = agents.monthly_agent()
weekly_agent = agents.weekly_agent()
roadmap_compiler_agent = agents.roadmap_compiler_agent()

sentiment_analysis = tasks.sentiment_analysis(counsellor)
high_level_plan = tasks.high_level_plan(captain, [sentiment_analysis])
month_level_plan = tasks.month_level_plan(monthly_agent, [high_level_plan])
week_level_plan = tasks.week_level_plan(weekly_agent, [month_level_plan])
compiled_roadmap = tasks.compile_roadmap(roadmap_compiler_agent, [week_level_plan])

crew = Crew(
    agents=(counsellor, captain, monthly_agent, weekly_agent, roadmap_compiler_agent),
    tasks=(sentiment_analysis, high_level_plan,month_level_plan, week_level_plan, compiled_roadmap),
    process=Process.hierarchical,
    manager_llm = llm,
    verbose=2
)

result = crew.kickoff()

print("CrewAI Output:")
print(result)
