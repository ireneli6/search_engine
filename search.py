import pysolr

def search(kw,start,paging_size):
    solr = pysolr.Solr('http://127.0.0.1:8983/solr/test/', timeout=10)
    param='text:'
    query =""
    i=1
    if " AND " in kw:
        list=kw.split('AND')
        for k in list:
            query+=param
            query +='"'
            query+=k
            query += '"'
            if i != len(list):
                query+=" AND "
                i+=1
            else:
                pass

    else:
        if " OR " in kw:
            list = kw.split('OR')
            for k in list:
                query += param
                query += '"'
                query += k
                query += '"'
                if i != len(list):
                    query += " OR "
                    i += 1
                else:
                    pass
        else:
            query += param
            query += '"'
            query +=kw
            query += '"'

    # print(query)
    result=solr.search(query, **{'start':start,'rows': paging_size})
    print("results number",result.hits)
    print("searching time",result.qtime)
    print(result.docs)


#search(keywords, start_row, page_size)
#exactly search: "good food"
#must contain: "good AND food"
#page rank algorithm:"good OR food" The most related results will at the top, the last one might only have 1 keywords.
search("good OR food","0","10")
