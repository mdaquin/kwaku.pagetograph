from selenium import webdriver
from bs4 import BeautifulSoup
import ingraph.client as ig
import urlparse

def crawl(config, graphid):
    if not validateConfig(config):
        return False
    to_crawl = []
    crawled = []
    to_crawl.extend(config["seeds"])
    while len(to_crawl) != 0:
        url = to_crawl.pop()
        crawled.append(url)
        # driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
        driver = webdriver.Firefox()
        print("=== getting "+url+"====")
        driver.get(url) # how to check this went OK?
        srce = driver.page_source
        driver.close()
        soup = BeautifulSoup(srce, features="lxml")
        for l in config["follow_links"]:
            nurls = extractURLs(soup, l, url)
            for u in nurls:
                if u not in to_crawl and u not in crawled:
                    to_crawl.append(u)
        for n in config["nodes"]:
            process(graphid, soup, n)
    return True

def process(graphid, soup, node):
    els = soup.select(node["selector"])
    for el in els:
        nid = el.select(node["ID"])[0].text.strip()
        obj = {"label": nid, "outedges": []}
        for attr in node["attributes"]:            
            val = []
            s = el.select(attr["selector"])
            if len(s)==1:
                val = s[0].text.strip()
            else:
                for i in s:
                    val.append(i.text.strip())
            obj[attr["attribute"]] = val
        for rel in node["relations"]:            
            s = el.select(rel["selector"])
            for i in s:
                obj["outedges"].append((rel["relation"], i.text.strip()))
        ig.updateNode(graphid, nid, obj)

def extractURLs(soup, link, base):
    es = soup.select(link["selector"])
    res = []
    for e in es:
        res.append(urlparse.urljoin(base, e["href"]))
    return res


def validateConfig(c):
    if "seeds" not in c:
        print("seeds missing")
        return False
    if "follow_links" not in c:
        print ("missing links to follow")
        return False
    if "nodes" not in c:
        print ("missing nodes to extract")
        return False
    for node in c["nodes"]:
        if "ID" not in node:
            print("missing ID selector for node")
            return False
    for node in c["nodes"]:
        if "attributes" not in node:
            print("missing attribute descriptions for node")
            return False
    for node in c["nodes"]:
        if "relations" not in node:
            print("missing relation descriptions for node")
            return False
    return True

