# Final Project components

## store

### store

- movies

- rating

- image

## App

- router-view 사용

### HomeVIew

1. MyMovieImage

2. ChoiceList

3. MyMovieList

#### MyMovieImage

- store의 action 실행 후 state에 생긴 image 불러오기

#### ChoiceList

- store에서 rating의 인기 높은 것 8 개 가져와 filter로 보여주기

- 선택한 것들을 담아 store의 action 실행 -> 이미지 만들기 버튼 추가

#### MyMovieList

- router-view 사용

##### Genre1-6

- store에서 rating 데이터 filter 해서 보여주기

### MovieView

#### MovieNow, MoviePopular, MovieTopRated

- store에서 movies 전체 정보 중 api_categoty로 filter 해서 보여주기

##### MovieDetail

- `movies/<int:movie_pk>/`로 axios 요청

### LoginView

- `accounts/`로 axois 요청

### CommunityView

- router-view 사용

#### ArticleList

- `articles/index/`로 axios 요청

- 데이터 prop으로 ArticleItem 넘겨주기

##### ArticleItem

- v-for로 여러개 생성

- ArticleList에서 props 받아온 데이터로 구성

#### ArticleDetail

- `articles/<int:article_pk>/`로 axios 요청

###### Comments

- `articles/<int:article_pk>/comment_create/`로 요청 시 댓글 생성

- `articles/<int:article_pk>/comments/<int:comment_pk>/delete/` 댓글 삭제 요청


