import kwaku.pagetograph as ptg
import ingraph.client as ig

config = {
    "seeds": ["https://www.insight-centre.org/research-staff"],
    "follow_links":[
        {"selector": ".views-field-field-family-name a",
         "attribute": "href"},
        {"selector": ".pager__item a",
         "attribute": "href"}                                    
        ],
    "nodes": [
        {"selector": ".pane-page-content:has(.content:has(.user-profile))",
         "ID": "h2",
         "attributes": [
             {"selector": ".l-user-profile-bottom p>span>span",
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
es_url = "http://127.0.0.1:9200"

# create the graph
ig.createGraph(graphid, es_endpoint=es_url, directed=True, labelled=True, weighted=False, multi=True)

print (ptg.crawl(config, graphid))

