from crewai import Task

def build_relationships_task(entities):
    return Task(
        description=f"Establish relationships between the following entities: {entities}",
        expected_output="List of relationships",
        agent="Relationship Builder"
    )
