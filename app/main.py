from crew_config import crew
from agents.entity_extractor import extract_entities_task
from agents.relationship_builder import build_relationships_task
from neo4j_client import Neo4jClient

def main():
    text = "Alice works at Acme Corp in New York."

    # Extract entities
    entity_task = extract_entities_task(text)
    crew.tasks = [entity_task]
    entities = crew.run()

    # Build relationships
    relationship_task = build_relationships_task(entities)
    crew.tasks = [relationship_task]
    relationships = crew.run()

    # Store in Neo4j
    neo4j = Neo4jClient()
    for entity in entities:
        neo4j.create_entity(entity)
    for rel in relationships:
        neo4j.create_relationship(rel['from'], rel['to'], rel['type'])
    neo4j.close()

if __name__ == "__main__":
    main()
