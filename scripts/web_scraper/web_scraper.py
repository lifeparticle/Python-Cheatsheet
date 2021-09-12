from selenium import webdriver
from urllib.parse import urljoin
from selenium.webdriver.chrome.options import Options

def navigate(driver, url, page_no):
	driver.get(urljoin(url, str(page_no)))


def get_data(driver, class_name):
	return driver.find_elements_by_class_name(class_name)


def has_data(data):
	return len(data) > 0

def parse_data(data, class_names):
	for quote in data:
		text = quote.find_element_by_class_name(class_names["text"]).text
		author = quote.find_element_by_class_name(class_names["author"]).text
		print("%s -- %s" %(text, author))

def main():
	options = Options()
	options.add_argument('--headless')
	driver = webdriver.Chrome(options=options)
	url = "http://quotes.toscrape.com/page/"
	page_no = 1
	while True:
		navigate(driver, url, page_no)
		data = get_data(driver, "quote")
		parse_data(data, {"text": "text", "author": "author"})
		page_no += 1
		if (has_data(data) == False):
			break
	driver.close()


if __name__ == '__main__':
	main()