from bs4 import BeautifulSoup
import requests
import json
import re
# class
class CustomCrawler:
    final_links = []
    def parse(self):
        html =''
        with open("vocalmusic.html",'r',encoding="utf-8") as f:
            html = f.read()
            f.close()
        contents = BeautifulSoup(html,features="html.parser")
        links = contents.find("div",{"class":re.compile("col-xs-12 play-list-box")}).findAll("div",{"class":re.compile('col-xs-12 item js-pl-item')})
        #print(links)
        for link in links:
            print(link.find("a",{"class":re.compile('dl-128')}).attrs["href"])
            self.final_links.append(link.a.attrs['href'])
        try:
            with open('mp3links.json',"w",encoding='utf-8') as f:
                print("saving file in scraped.json")
                json.dump(self.final_links,f,ensure_ascii=False,indent=4)
                f.close()
        except:
            print("Error while saving file")
        print("Task done!")
        #for link in self.final_links:
            #print(self.final_links.index(link))
    def download(self,link):
        try:
            print(f"Downloading the file {link}")
            response = requests.get(link)
            with open(f"{self.final_links.index(link)}.mp3","w",encoding="utf-8") as f:
                f.write(response.content)
                f.close()
        except:
            print("Error Accoured while downloading the mp3 file")     
    def run(self):
        #html = self.loadhtml()
        self.parse()
        self.download(self.final_links[1])
if __name__ == "__main__":
    bot = CustomCrawler()
    bot.run()