import sys
sys.path.insert(1, '/home/mdaquin/code/ingraph/')
from ingraph.ingraph import InGraph

graphid = "test_ptg_graph"
es_url = "http://127.0.0.1:9200/"

graph = InGraph(graphid, es_url)

print(graph.search(query=sys.argv[1], size=1))



