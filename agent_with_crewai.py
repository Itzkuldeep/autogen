import os
import subprocess
from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from crewai_tools import SerperDevTool, WebsiteSearchTool  # Correct tool import
from crewai.tools import tool

# 🔹 Load environment variables
load_dotenv()

# 🔹 Set up the LLM configuration
llm_config = LLM(
    model="ollama/mistral:latest",
    base_url="http://localhost:11434"
)
llm_code = LLM(
    model="ollama/deepseek-coder:6.7b",
    base_url="http://localhost:11434"
)

# Create instances of tools
serper_tool = SerperDevTool()
website_search_tool = WebsiteSearchTool()

# 🔹 Function to check and install dependencies
def install_missing_packages(package_name):
    try:
        subprocess.run(["pip", "install", package_name], check=True)
    except subprocess.CalledProcessError:
        print(f"Failed to install {package_name}. Try installing it manually.")

# 🔹 Ensure firecrawl is installed
try:
    from firecrawl import FirecrawlApp
except ModuleNotFoundError:
    print("🔥 'firecrawl' package missing. Installing...")
    install_missing_packages("firecrawl-py")

# 🔹 Define Tools (Fix invalid tool type issues)
@tool("code_search")
def code_search(input: str):
    """
    Code search tool to retrieve relevant code snippets based on user input.
    """
    response = llm_config.call(input)
    return response

# 🔹 Agent Definitions
coding_agent = Agent(
    role="Senior Software Developer",
    goal="Craft well-structured, optimized, and bug-free Python code.",
    tools=[code_search],  # Fixed tool usage
    verbose=True,
    backstory="You are a top-tier Python developer with expertise in clean code, debugging, and best practices.",
    llm=llm_code
)

teacher_agent = Agent(
    role="Skillful Teacher",
    goal="Teach complex subjects in an easy-to-understand way.",
    tools=[serper_tool, website_search_tool],  # Removed Firecrawl tools to prevent import issues
    verbose=True,
    backstory="A passionate teacher who explains math, social science, and computer science in the simplest way.",
    llm=llm_config
)

research_agent = Agent(
    role="Research Assistant",
    goal="Gather and summarize the latest advancements in AI technology.",
    tools=[serper_tool, website_search_tool],  # Removed problematic Firecrawl tools
    verbose=True,
    backstory="An AI research assistant skilled in analyzing and summarizing key tech developments.",
    llm=llm_config
)

# 🔹 Task Definitions
coding_task = Task(
    description="""
    Using input from the Student, analyze the question and provide an optimized Python solution.
    The code should be  well-documented, easy to understand, and efficient .
    Provide a brief explanation of the code and its workings using  comments .
    """,
    expected_output="""
    A clean, optimized, and well-documented Python solution with explanations.
    """,
    output_file="full_stack_web_app.py",
    agent=coding_agent,
)

teacher_task = Task(
    description="""
    Create a 15-minute math lesson plan on fractions.
    Include clear objectives, an outline, interactive activities, assessment methods, and teaching strategies .
    """,
    expected_output="""
    A structured lesson plan on fractions with clear learning objectives.
    """,
    output_file="comprehensive_lesson_plan.pdf",
    agent=teacher_agent
)


research_task = Task(
    description="""
    Gather  recent advancements in AI technology .
    Provide a  concise report  summarizing key breakthroughs and applications.
    """,
    expected_output="""
    A research report covering major AI advancements and their real-world applications.
    """,
    output_file="ai_advancements_report.pdf",
    agent=research_agent
)

# 🔹 Crew Definition (Connecting Agents with Tasks)
Schoolagent = Crew(
    agents=[coding_agent, teacher_agent, research_agent],
    tasks=[coding_task, teacher_task, research_task],
    verbose=True
)

# 🔹 User Input for Task Selection
task = input("🔹 Select a task: (coding/theoretical/research) ").strip().lower()

if task == "coding":
    user_input = input("🔹 Enter your coding problem: ").strip()
    # Properly passing inputs as a dictionary
    Schoolagent.kickoff(inputs={"problem": user_input})

elif task == "theoretical":
    user_question = input("🔹 Enter your question for the teacher: ").strip()
    teacher_task.description = f"Question: {user_question}\n{teacher_task.description}"
    Schoolagent.kickoff(teacher_task)

elif task == "research":
    Schoolagent.kickoff(research_task)

else:
    print("❌ Invalid choice. Please enter 'coding', 'theoretical', or 'research'.")
