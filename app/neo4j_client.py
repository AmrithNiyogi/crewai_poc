from neo4j import GraphDatabase # type: ignore
import os


class Neo4jClient:
    def __init__(self):
        uri = os.getenv("NEO4J_URI")
        user = os.getenv("NEO4J_USER")
        password = os.getenv("NEO4J_PASSWORD")
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_entity(self, name):
        with self.driver.session() as session:
            session.run("MERGE (e:Entity {name: $name})", name=name)

    def create_relationship(self, from_entity, to_entity, relation):
        with self.driver.session() as session:
            session.run("""
                MATCH (a:Entity {name: $from_entity})
                MATCH (b:Entity {name: $to_entity})
                MERGE (a)-[r:RELATION {type: $relation}]->(b)
            """, from_entity=from_entity, to_entity=to_entity, relation=relation)