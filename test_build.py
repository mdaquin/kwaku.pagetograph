import sys
sys.path.insert(1, '/home/mdaquin/code/ingraph/')
import kwaku.pagetograph as ptg
from ingraph.ingraph import InGraph



config = {
    "seeds": ["https://www.insight-centre.org/research-staff"],
    "follow_links":[
        {"selector": ".views-field-field-family-name a",
         "attribute": "href"},
        {"selector": ".pager__item a",
         "attribute": "href"}                                    
        ],
    "nodes": [
        {"selector": ".pane-page-content",
         "ID": "h2",
         "attributes": [
             {"selector": ".l-user-profile-bottom p span span",
              "attribute": "biography"}
         ],
         "relations": [
             {"selector": ".field--name-field-user-job-title .field__items .field__item",
              "relation": "role"},
             {"selector": ".field--name-field-user-insight-institude .field__items .field__item",
              "relation": "affiliation"
              }
             ]
         },
        {"selector": ".view-publications li",
         "ID": ".views-field-title a",
         "attributes": [
             {"selector": ".views-field-title a",
              "attribute": "title"
              },
             {"selector": ".date-display-single",
              "attribute": "date"
              }
         ],
         "relations": [
             {"selector": ".views-field-field-pub-journal .field-content",
              "relation": "journal"
             },
             {"selector": ".views-label-field-pub-conference .field-content",
             "relation": "conference"
             },
             {"selector": ".views-field-field-pub-display-authors p",
              "relation": "authorlist"
             },
             {"selector": ".views-field-field-pub-display-authors p a",
              "relation": "author"
             }             
         ]     
         }
        ]
    }

graphid = "test_ptg_graph"
es_url = "http://127.0.0.1:9200/"

graph = InGraph(graphid, es_url)

# create the graph
graph.create_graph(directed=True, labelled=True, weighted=False, multi=True)

print (ptg.crawl(config, graph, turl="https://www.insight-centre.org/users/francisco-pena"))


