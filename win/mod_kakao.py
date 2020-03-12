from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep

place_address = '';
etc_info = '';
info = '';


def mod_kakao(pa,etc,ec,sc,pc,tc,elc) :
    place_address = pa
    etc_info = etc
    if ec == 1 :
        info = ''.join("휠체어 출입가능 입구")
    if sc == 1 :
        info = ''.join("휠체어 좌석 가능")
    if pc == 1 :
        info = ''.join("장애인 주차장")
    if tc == 1 :
        info = ''.join("장애인 화장실")
    if elc == 1 :
        info = ''.join("엘레베이터 보유")

    info = ''.join(etc_info)

    #카카오 정보 수정
    driver = webdriver.Chrome('크롬드라이버 위치') #크롬 드라이버
    driver.set_window_size(2000,1000)
    driver.implicitly_wait(2)
    driver.get('https://accounts.kakao.com/login/kakaomap?continue=https%3A%2F%2Fmap.kakao.com')# 카카오맵의 로그인탭 로그인 완료하면 카카오맵으로 바로 이동
    driver.implicitly_wait(5)

    driver.find_element_by_xpath('//*[@id="id_email_2"]').send_keys("아이디")#아이디 입력
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="id_password_3"]').send_keys("비번")#비밀번호 입력
    driver.implicitly_wait(2)
    driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[8]/button').click()#로그인 완료 버튼 클릭
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="search.keyword.query"]').send_keys(place_address)#검색 주소로
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="search.keyword.submit"]').send_keys(Keys.ENTER)#검색 버튼
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="info.search.place.list"]/li[1]/div[5]/div[4]/a[1]').send_keys(Keys.ENTER)#검색된 결과 리스트중 첫번째 인덱스의 상세정보 버튼 클릭
    driver.implicitly_wait(5)

    #상세정보 버튼을 누르면 새탭으로 켜져서 새탭으로 이동
    driver.switch_to_window(driver.window_handles[1])
    driver.implicitly_wait(5)
    sleep(2)
    driver.find_element_by_xpath('//*[@id="mArticle"]/div[1]/div[2]/span/a').send_keys(Keys.ENTER)#틀린 정보 신고 버튼 클릭
    driver.implicitly_wait(10)
    sleep(2)
    driver.switch_to_frame(1)
    driver.find_element_by_xpath('//*[@id="kakaoContent"]/div/a[2]').send_keys(Keys.ENTER)#정보 수정 버튼 클릭
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="kakaoContent"]/form/div/div[7]/div/a').send_keys(Keys.ENTER)#제공 서비스 클릭
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="kakaoContent"]/form/fieldset/div[7]/div/div[1]/label').click()#휠체어 사용 가능
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//*[@id="kakaoHead"]/button').click()#완료 버튼 클릭
    driver.implicitly_wait(10)

    driver.find_element_by_xpath('//*[@id="tfFiy6"]').send_keys(info)#부가정보 추가
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="kakaoHead"]/button').click()#완료 버튼 클릭
    driver.implicitly_wait(10)
    print('카카오 수정 완료')

mod_kakao()
