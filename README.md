<div align="center"><img src ="https://capsule-render.vercel.app/api?type=egg&color=FCB188&height=100&section=header&text=주류룹&fontSize=90"></div>



<div align="center">
  <h1>: 주류 추천 및 구매 시스템</h1>
</div>
<br> </br>

<div align="center">
  <img src="https://github.com/mchaewon/alcohol_order_service/assets/94179998/d4dd6885-d332-4255-bc03-50b377ae7eb6" alt="주류 이미지">
</div>

<br> </br>
<br> </br>

## 🍺 프로젝트 소개

DB를 사용한 web 기반 프로그램 제작

```
주류 추천 및 구매 시스템 **주류룹**에서 주류 검색부터 배송까지 **한번에**~
```

⏰ **기간** : 2023.09.01 ~ 2023.12.15
<br> </br>

📝 **목적** : 코로나19의 단계적 회복에 힘입어 매년 감소세를 보이던 주류 출고량이 지난해 증가세로 전환된 것으로 나타났다. 따라서 다양한 종류의 주류를 편리하게 구매 및 배달하고 추천을 해주는 서비스를 기획하였다.
<br> </br>

💡 **차별성** : 랜덤 주류 추천 기능을 통하여 사용자가 다양한 주류를 볼 수 있도록 한다.
<br> </br>
<br> </br>

## 🍷 데모 영상
<a href = "https://youtu.be/lgBAGRqF85c?si=A4GEQfFO9bmLoiX1">
<img width="535" alt="스크린샷 2023-12-06 오전 4 11 40" src="https://github.com/mchaewon/alcohol_order_service/assets/94179998/da67622c-ea71-4131-8f6e-4c99e35aeda0">
</a>

https://youtu.be/lgBAGRqF85c?si=A4GEQfFO9bmLoiX1


<br> </br>
<br> </br>
<br> </br>

## 🍹 개발 환경

<img src="https://img.shields.io/badge/python-3776AB?style=flat-square&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/oracle-F80000?style=flat-square&logo=oracle&logoColor=white"/> <img src="https://img.shields.io/badge/flask-000000?style=flat-square&logo=flask&logoColor=white"/>

```markdown
### version

python : 3.8.0
Oracle : 19.3.0.0.0
flask : 2.2.2
Werkzeug : 2.2.2
cx_Oracle : 8.3.0
```

<br> </br>
<br> </br>
<br> </br>

## 🍾 실행 및 사용방법

```markdown
### environment setting

pip install -r requirements.txt

### 실행방법

1. python run.py
2. 주소 "[localhost:5000](http://localhost:5000)"로 접속
3. 처음 웹 방문이면 회원가입 후 로그인 / 회원이라면 로그인
```

<br> </br>
<br> </br>
<br> </br>

## 🥃 기능 설명

```
1. 회원가입 / 로그인
	1.1 회원가입
		1.1.1 ID, Name, Password, Phone Number, Birthday, Address 입력
	1.2 로그인
		1.2.1 User Type 선택 가능
			1) Customer : ID, Password 입력
			2) Manager : ID, Name 입력

2. Manager
	2.1 Search
		2.1.1 본인이 쓴 공지사항을 조회할 수 있음
		2.1.2 원하는 공지사항을 삭제할 수 있음
	2.2 Write
		2.1.1 공지사항을 작성 가능

3. Customer
	3.1 오늘의 술 추천
		3.1.1 ('주종', '가격', '평점') 중 원하는 정보를 기입하고 필터링된 술 중에서 오늘의 술을 추천받을 수 있음.
			1) 정보를 기입하지 않아도 술을 추천받을 수도 있음.
	3.2 술 구매
		3.2.1 원하는 술을 Cart에 담고, Cart에서 구매할 수 있음.
			1) Cart에서 술을 삭제할 수 있음.
		3.2.2 구매한 술은 Order List에서 볼 수 있음.
	3.3 술 검색
		3.3.1  'alcohol name', 'price', 'degree', 'star' 중 원하는 정보를 기입하여 술을 검색할 수 있음.
	3.4 술 평점
		3.4.1 구매한 술에 대해 1~5까지의 평점을 남길 수 있음.
	3.5 가게 조회
		3.5.1 원하는 지역을 선택하여 해당하는 가게들을 조회할 수 있음.
	3.6 공지사항 조회
		3.6.1 Manager에 의해 작성된 공지사항을 조회할 수 있음.
	3.7 customer 정보 조회
		3.7.1 본인의 정보를 조회할 수 있음.
```

<br> </br>
<br> </br>
<br> </br>

## 🐣 팀원 소개

### 7조 : 디비디비-딥!

**team notion :** <a href = "https://remarkable-wakeboard-c22.notion.site/DB_Project-Team7-204b8d5bf8e649c5a68d5c15f4466890?pvs=4" target = "_blank"><img src="https://img.shields.io/badge/notion-000000?style=flat-square&logo=notion&logoColor=white"/></a>

![image](https://github.com/mchaewon/alcohol_order_service/assets/94179998/ec4d7b5f-cc86-48a7-bd68-af42690c532e)


|                                                                                  김은정                                                                                  |                                                                                   김은지                                                                                   |                                                                                  문채원                                                                                  |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                                                      ![image](https://avatars.githubusercontent.com/u/94179998?v=4)                                                      |                                                       ![image](https://avatars.githubusercontent.com/u/87495422?v=4)                                                       |                                                     ![image](https://avatars.githubusercontent.com/u/111948424?v=4)                                                      |
| <a href="https://github.com/ezzkimm/" target="_blank"><img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white"/></a> | <a href="https://github.com/EunJiKim02" target="_blank"><img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white"/></a> | <a href="https://github.com/mchaewon" target="_blank"><img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white"/></a> |
|                                                                                Front-end                                                                                 |                                                                                 Back-end                                                                                  |                                                                                 Front-end                                                                                 |
|                                                                                2020112393                                                                                |                                                                                 2021111183                                                                                 |                                                                                2021114611                                                                                |

<br> </br>
<br> </br>
<br> </br>
