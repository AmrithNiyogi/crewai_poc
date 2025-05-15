from crewai import Task

def extract_entities_task(text):
    return Task(
        description=f"Extract entities from the following text: {text}",
        expected_output="List of entities",
        agent="Entity Extractor"
    )