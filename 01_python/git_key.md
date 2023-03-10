# 명령어

## GIT 명령어

`git init` : git 하위 디렉토리 생성

`git clone (url)` : 기존 소스 코드 다운로드/복제

`git add (파일명)`: 커밋에 단일 파일의 변경 사항을 포함 (인덱스에 추가)

`git add -A` : 커밋에 파일의 변경 사항을 한 번에 모두 포함

`git commit -m "메세지"` : 커밋 생성, 실제 변경사항 확정

`git status` : 파일 상태 확인

`git push origin master` : 변경 사항을 원격 서버에 업로드

`git pull` : 원격저장소의 변경 내용 불러오기 및 병합

`git log` : 커밋 내용을 확인

## CLI 명령어

`ls` : 파일보기

`al` : 파일 세부내용 확인

`cd` : 디렉토리로 이동

`cd .` : 현재 디렉토리

`cd ..` : 부모 디렉토리

`touch` : 빈 파일 생성

`mkdir` : 디렉토리 생성

`mv` : 파일 및 디렉토리 옮기기

`rm` : 파일 삭제

`rm -r` : 폴더 삭제

## 설정

`git config --list` : 현재 설정 확인 

`git config --global user.name "이름"` : 이름 설정

`git config --global user.email "email@com"` : 이메일 설정

`git config --unset --global user.name` : 이름 삭제

`git config --unset --global user.email` : 이메일 삭제

origin 외에 다른 이름으로 사용할 곳

- `git remote -v` : 현재 디렉토리와 연결된 원격저장소 확인

- `git remote add (origin) (url)` :    연결 디렉토리 추가

windows 자격증명은 push 진행하면 완료됨

### 참고

vim 화면

원인 : 커밋 메세지 미입력

해결 방법

1. 상단에 ""없이 저장 메세지 입력

2. 인서트 모드로 변환

3. ESC 키

4. 아랫쪽 줄에 :wq 입력 후 엔터
