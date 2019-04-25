from selenium import webdriver

browser = webdriver.Chrome()
try:
    # browser.get('http://localhost:8000/login/')
    browser.get('http://localhost:8003')
    print(browser.title)
    assert 'Django' in browser.title
except Exception as e:
    print('error')
finally:
    import time
    time.sleep(4)
    browser.close()
