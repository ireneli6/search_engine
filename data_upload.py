#coding=utf-8
import pysolr


file=open('yelp_academic_dataset_review.json',encoding='utf-8')
#http://ip:port/solr/core_name/
solr = pysolr.Solr('http://127.0.0.1:8983/solr/test/', timeout=10)
i=1
for line in file:

    data=eval(line)

    result = solr.add([data])

    print(i)
    i+=1