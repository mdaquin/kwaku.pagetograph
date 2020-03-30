# KWAKU Page to Graph

An import module based on data scrapping and crawling from webpages. Based on selenium.

## Configuration

The parameters for the scaper include:

Seeds: [URL]
follow_link: [{selector: string, attribute: string}] # css selectors and attr
Nodes: [{selector: string, # selector of the element
         id: string, # selector of the id wihing the element,
	 attributes: [selector: string, # selector of an attribute,
	  	      edge_label: string # label of the edge to create
		      ],
	 relations: [selector: string, # selector of a relation (text is the id)
	             edge_label: string # label of the edge to create
		     ]
		     }]


