from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep


def add_google() :
    #구글 장소 추가
    driver = webdriver.Chrome('크롬드라이버 위치') #크롬 드라이버
    driver.implicitly_wait(1)
    driver.get('https://www.google.com/maps/@37.3238594,127.1365129,15z/data=!10m2!1e2!2e13?hl=ko')
    driver.implicitly_wait(1)
    driver.find_element_by_xpath('//*[@id="rap-card"]/div/div[2]/button').click()
    driver.implicitly_wait(1)
    driver.find_element_by_name("identifier").send_keys("아이디")
    driver.implicitly_wait(1)
    driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span').click()
    driver.implicitly_wait(1)
    driver.find_element_by_name("password").send_keys("비번")
    driver.implicitly_wait(1)
    sleep(2)
    driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span').click()
    driver.implicitly_wait(5)
    sleep(3)
    #여기까지 로그인


    iframes = driver.find_elements_by_tag_name('iframe')
    print('현재 페이지에 iframes %d개가 있다' % len(iframes))
    driver.implicitly_wait(5)

    #iframe분석 결과, 해당 페이지에서 첫번째 iframe 즉 0번째 인덱스가 Add A Place임
    driver.switch_to_frame(0)
    #print(driver.page_source)

    driver.implicitly_wait(5)
    sleep(3)
    #driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[4]/div[3]/div/span[1]/button/span').click()
    #driver.implicitly_wait(5)
    #driver.find_element_by_id("yDmH0d").send_keys("ggg")
    #driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[4]/div[2]/div[1]/div[2]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input').send_keys("dd")
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[4]/div[2]/div[1]/div[3]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input').send_keys("장애인용 공용 화장실")#카테
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[4]/div[2]/div[1]/div[3]/div/div[2]/div/div[2]').click() 

    driver.implicitly_wait(10)
    #주소추가 무조건 뒤에 띄어쓰기 필수
    driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[4]/div[2]/div[1]/div[4]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input').send_keys("서울시 광진구 뚝섬로62길 2 ")
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="unstructured-input"]').click() #주소추가 첫 줄 선택
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id=""]/').click() #보내기버튼클릭
    print('구글 추가 완료')


    #부가내용 추가 

add_google()