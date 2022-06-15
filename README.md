  
  
# 프로젝트 구조
user 앱 : 사용자 로그인과 사용자 정보를 관리하는 앱
  - models.py : User모델, UserProfile모델, Hobby모델
  - views.py: UserLoginView -> 사용자 로그인 기능  
              (/login)
              UserInfoView -> 사용자 정보조회 기능 
              (/user_info)


blog 앱 : 게시글 작성을 관리하는 앱
  - models.py : Category모델, Article모델, Comment모델
  - views.py : WriteAfterThreeDaysOfSubscription클래스 -> permission관리 클래스 
                                                          (가입일기준 3일이상 지난 사용자만 접근가능하게 함)
               WriteArticleView -> 게시글 제목,카테고리, 게시글 내용을 사용자에게 받아서 게시글 생성    
               (/create/article/<int:id>)



#6월 13일 과제
  - 1번 : blog 앱에 <게시글, 작성자, 작성 시간, 내용>이 포함된 comment라는 테이블을 추가해주세요
    -> blog앱의 models.py 에 class Comment 생성
    
  - 2번 : Django Serializer 기능을 사용해 로그인 한 사용자의 기본 정보들을 response data에 넣어서 return 해주세요
    -> user앱의 serializer.py에 class LoginUserSerializer 생성
   
  - 3번 :사용자가 작성 한 게시글을 로그인 한 (2번)User의 serializer data에 포함시켜서 같이 return해주세요
    -> 아직 작성중
