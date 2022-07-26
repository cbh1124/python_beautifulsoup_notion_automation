import notion_automation

auto = notion_automation.Notion_automation()
search = {}

chromepath = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
#url = 'https://www.notion.so/2022_02_24-79bc4e9442444d03bed40d046751f96b'
#auto.pdf(chromepath,url)
url2 = 'https://www.notion.so/da030cc0884d4c0b8aa8ba4405cc417d'

driver = auto.driver_r(chromepath)

#pdf = auto.pdf(driver, url)
auto.solution_pdf(driver,url2)
# search = auto.search_p_size(driver,url2)
# search.pop()
# print(format(search))
#
# path = "C:/Users/119vk/OneDrive/바탕 화면/인쇄 정리"
# print(auto.dir_path(path))
#
# print(auto.dir_compare(path))