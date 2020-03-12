from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep

#안드로이드에서 가져오는 정보들
place_name = '';
place_address = '';
category = '';
phone_number = '';
info = '';
etc_info = ''; 

#인자 삽입 순서 : 이름, 주소, 카테고리, 번호, 부가정보, 시설가능5개
def add_kakao(pn, pa, ca, pb, etc, ec, sc, pc, tc, elc) :
    place_name = pn
    place_address = pa
    category = ca
    phone_number = pb #서버에서 폰넘버없으면 - 표시
    etc_info = etc #서버에서 없으면 - 표시
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



    #카카오 장소 추가
    driver = webdriver.Chrome('크롬드라이버 위치 ') #크롬 드라이버
    driver.implicitly_wait(2)
    driver.get('https://accounts.kakao.com/login/kakaomap?continue=https%3A%2F%2Fmap.kakao.com') #카카오맵의 로그인탭 로그인 완료하면 카카오맵으로 바로 이동
    driver.implicitly_wait(5)


    driver.find_element_by_xpath('//*[@id="id_email_2"]').send_keys("아이디")#아이디 입력
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="id_password_3"]').send_keys("비번")#비밀번호 입력
    driver.implicitly_wait(2)
    driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[8]/button').click()#로그인 완료 버튼 클릭
    driver.implicitly_wait(5)
    driver.implicitly_wait(5)
    #click()으로 안되서 keys.enter사용
    driver.find_element_by_xpath('//*[@id="info.main.newplace"]/div/a[1]').send_keys(Keys.ENTER)#신규 장소 등록 버튼 클릭
    driver.implicitly_wait(5)

    #map.kakao.com에서 두번째 iframe이 장소 추가 팝업창임.
    driver.switch_to_frame(1)
    #장소 추가 팝업창 진입
    driver.find_element_by_xpath('//*[@id="tfFiy1"]').send_keys(place_name)
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="kakaoContent"]/form/div/div[2]/div[1]/a').send_keys(Keys.ENTER)#위치 등록 버튼 클릭
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="kakaoContent"]/div/div[1]/form/fieldset/div/input').send_keys(place_address)#주소 폼 입력
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="kakaoContent"]/div/div[1]/form/fieldset/div/button[2]').click()#주소 검색 버튼 클릭
    driver.implicitly_wait(5)
    address_list_ul = driver.find_element_by_class_name('list_result')
    address_list_li = address_list_ul.find_elements_by_tag_name('li')
    driver.implicitly_wait(5)
    address_list_li[0].click()
    #주소 중 첫번째 리스트 클릭
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="tfFiy3"]').send_keys(category) #업종 추가
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="tfFiy4"]').send_keys(phone_number) #전화번호 추가
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="tfFiy6"]').send_keys(info)  #부가 정보 추가 및 휠체어 가능 자세히
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="kakaoContent"]/form/div/div[9]/div/a').send_keys(Keys.ENTER)#제공 서비스 클릭
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="kakaoContent"]/form/fieldset/div[7]/div/div[1]/label').click()#휠체어 사용 가능
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//*[@id="kakaoHead"]/button').click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//*[@id="kakaoHead"]/button').click()
    driver.implicitly_wait(10)
    print('카카오 추가 완료')

    driver.quit()


add_kakao()

