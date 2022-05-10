GIT 학습 중

1. 폴더 생성 후 git init  -> .git 폴더 등장

2. git config --global user.email "phantom0119@daum.net"   -> 계정(email) 등록

3. git config --global user.name "phantom0119"   -> 계정(ID) 등록

4. 파일 추가 해보기.  git add README.txt

5. 추가(수정)한 파일에 대한 설명 넣기.   git commit -m "설명 내용"

6. commit한 내용 등의 로그 기록 확인    git log   -> commit 920491d934... (HEAD -> master) 형태 출력.

 
7. 이전 버전으로 checkout 하기 위해서는 git log를 통해 해당 커밋의 고유 번호를 알아야 한다.
   이후에 git checkout [커밋번호]   ->  커밋번호는 앞자리에서 7자리만 입력해도 무관.
 
   git checkout -    :  가장 최근의 commit 버전으로 checkout


8. Github에 올리기.  
   git remote add origin https://github.com/phantom0119/Baekjoon.git
   접근 허가 (로그인)
   git push origin master

9. 타 PC에서 clone으로 다운
   git clone https://github.com/phantom0119/Baekjoon.git .     ->  마지막 마침표 = 현재 위치(폴더)
   
10. 원격 저장소에 새로운 Commit이 있으면 가져오기.
     gir pull origin master