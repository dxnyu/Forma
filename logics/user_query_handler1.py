from crewai import Agent, Task, Crew
from crewai_tools import WebsiteSearchTool

tool_websearch = WebsiteSearchTool()

agent_website = Agent(
    role="Website Extracter",
    goal = "Collect relevent information on incentives and programs from the Singapore government that could support {question}.",
    backstory = """You are helping to collate information on {question}."
    A company executive will be providing you information on their company or business in {question}.
    Based on what was shared, you should:
        1. Suggest appropriate business activities (e.g. headquarters, manufacturing, or R&D) they could establish in Singapore.
        2. Suggest incentives and programs available in Singapore, by searching websites of Singapore Government ministries and agencies (usually marked by gov.sg).
    Your work is the basis for the agent Content Writer to respond to the user on this question.""",
    tools = [tool_websearch],
    allow_delegation = False,
    verbose = True,
)

agent_writer = writer = Agent(
    role="Content Writer",
    goal="Provide accurate facts about the question: {question}",

    backstory="""You're working on helping a foreign investor on: {question}.
    You base your writing on the work of the Website Extracter, who provide relevant context about the question.
    Your objective is to suggest business activites and relevant incentives and programs based on the company's description in {question}.""",

    allow_delegation=False, 
    verbose=True, 
)

task_plan = Task(
    description="""\
    1. Prioritize key pieces of information on: {question}.
    2. Identify the target user, based on details of the {question} provided.
    3. Develop a detailed content outline, including introduction, key points, and a call to action to set up a business in Singapore.""",

    expected_output="""\
    A comprehensive business plan with an outline, steps on what to do, and useful resources to refer to.""",
    agent=agent_website,
)

task_write = Task(
    description="""\
    1. Use the content plan to craft a business plan on {question} based on the target audience's interests.
    2. Sections/Subtitles are properly named in an engaging manner.
    3. Ensure the post is structured with an engaging introduction, insightful body, and a summarizing conclusion.
    4. Proofread for grammatical errors and alignment the common style used in business reports.""",

    expected_output="""
    A well-written report, each section should have 1 or 2 paragraphs.""",
    agent = agent_writer,
)

crew = Crew(
    agents=[agent_website, agent_writer],
    tasks=[task_plan, task_write],
    verbose=True
)