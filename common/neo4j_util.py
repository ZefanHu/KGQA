from py2neo import Graph

neo4j_url = "http://localhost:7474"
neo4j_auth = ("neo4j", "1234")

def connect_neo4j():
    neo4j = Graph(neo4j_url, auth = neo4j_auth)
    return neo4j

class Neo4jQuery:
    def __init__(self):
        self.graph = connect_neo4j()

    def run(self,cql):
        result = []
        find_rela = self.graph.run(cql)
        for i in find_rela:
            result.append(i.items()[0][1])
        return result