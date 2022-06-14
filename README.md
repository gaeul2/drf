  
  
# 프로젝트 구조
user 앱 : 사용자 로그인과 사용자 정보를 관리하는 앱
  - models.py : User모델, UserProfile모델, Hobby모델
  - views.py: UserLoginView -> 사용자 로그인 기능  
              (/login)
              UserInfoView -> 사용자 정보조회 기능 
              (/user_info)


blog 앱 : 게시글 작성을 관리하는 앱
  - models.py : Category모델, Article모델 
  - views.py : WriteAfterThreeDaysOfSubscription클래스 -> permission관리 클래스 
                                                          (가입일기준 3일이상 지난 사용자만 접근가능하게 함)
               WriteArticleView -> 게시글 제목,카테고리, 게시글 내용을 사용자에게 받아서 게시글 생성    
               (/create/article/<int:id>)

