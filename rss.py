import urllib2
"http://www.techworld.com/rss/feeds/techworld-news.xml"
url = urllib2.Request(url = "http://www.techworld.com/rss/feeds/techworld-news.xml")
url_open_use = urllib2.urlopen(url)
inside = url_open_use.read()

title_tag = '<title>'
date_tag = '<pubDate>'
des_tag = '<description>'
link_tag = '<link>'
start=0
list_data = []

while inside.find(title_tag,start) != -1:
    str1 = ""
    str2 = ""
    str3 = ""
    str4 = ""

    start = inside.find(date_tag,start)
    end = inside.find('</pubDate>',start)
    #print inside[start + len(date_tag):end] + "."
    str1 = inside[start + len(date_tag):end] 
    start = end

    start = inside.find(title_tag,start)
    end = inside.find('</title>', start)
    #print inside[start + len(title_tag):end] + "."
    str2 = inside[start + len(title_tag):end]
    start = end

    start = inside.find(link_tag,start)
    end = inside.find('</link>', start)
    #print inside[start + len(title_tag):end] + "."
    str3 = inside[start + len(link_tag):end] 
    start = end

    start = inside.find(des_tag,start)
    end = inside.find('.&lt',start)
    #print inside[start + len(des_tag):end] + "." + "\n"
    str4 = inside[start + len(des_tag):end] + "." + "\n"
    start = end

    tup = (str1, str2, str3, str4)
    list_data.append(tup)

#print list_data