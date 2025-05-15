from crewai import Agent, Task, Crew, Process, LLM

llm = LLM(
    model="ollama/llama3",
    base_url="http://localhost:11434",
)

entity_extractor = Agent(
    role="Entity Extractor",
    goal="Extract entities from text",
    backstory="Specializes in identifying key entities.",
    llm=llm
)

relationship_builder = Agent(
    role="Relationship Builder",
    goal="Establish relationships between entities",
    backstory="Expert in connecting entities meaningfully.",
    llm=llm
)

crew = Crew(
    agents=[entity_extractor, relationship_builder],
    tasks=[],
    process=Process.sequential,
    verbose=True
)