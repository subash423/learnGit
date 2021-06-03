import requests

def scraper(keywords, N=20):
    pages=N//10
    if N%10!=0: pages+=1
    output = []
    keywords = keywords.replace(" ", "%2B").replace("/", "%252f")
    # print(keywords)

    try:
        for page_no in range(pages):
            url = "https://patents.google.com/xhr/query?url=q%3D{}%26oq%3D{}%26page%3D{}&exp=".format(
                keywords, keywords, page_no)
            resp = requests.get(url)
            json_data = resp.json()
            patents = json_data["results"]["cluster"][0]["result"]

            if page_no == pages-1:
                if N % 10 == 0:
                    n = 10
                else:
                    n = N % 10
            else:
                n = 10

            for i in range(n):
                # Title
                title = patents[i]["patent"]["title"]
                title = title.strip().replace("<b>", "").replace("</b>", "")
                # print(title)
                # Patent no.
                pat = patents[i]["patent"]["publication_number"]
                # print(pat)
                output.append((pat, title))
    except:
        pass

    #print("Length = ", len(output))
    return output


#print(scraper("gps", 34))
