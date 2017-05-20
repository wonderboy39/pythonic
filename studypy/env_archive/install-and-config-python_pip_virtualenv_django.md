# python, pip, virtualenv, django 환경설정
설치 및 환경설정 과정은 PC개발환경, 원격 서버 개발환경으로 나누어 정리할 것이며, 원격 서버 개발환경 설정은 차후 AWS t2 micro를 발급받아 정리해보려 한다.  
## 0) mac os x 에서의 선행사항
### Command Line Tools 설치
명령어 도구(command line tool)를 설치하지 않으면 python빌드시 아래와 같은 메시지를 접하게 된다.(나의 경우는 $pyenv install 2.7.10을 하는동안 에러가 발생했다.)   
```
BUILD FAILED (OS X 10.12 어쩌구)
...
...
파이썬 소스코드 중 몇 라인이 에러다 하고 보여준다...
...
```
이 경우 아래의 명령어를 Terminal에서 수행하여 해결할 수 있다.  
// 설치되어있는지, 버전은 몇인지 확인  
$ xcode-select --version  
// 명령어 도구 설치  
$ xcode-select --install  
### bash 버전 업그레이드
```bash
dyld: Library not loaded: /usr/local/opt/readline/lib/libreadline.6.dylib Referenced from: /usr/local/bin/bash
```
와 같은 메시지를 출력하면서 진행이 안된다면 bash가 너무 오래된 버전이어서 생기는 오류다. 따라서 아래의 명령어를 수행한다.  
```bash
$ brew upgrade bash
```
([참고자료](https://github.com/Homebrew/homebrew-core/issues/5799))  
## 1) python설치
mac에는 python2.7이 기본으로 설치 되어있다. 개발환경으로 python 2.7.x버전의 python을 사용할 것이므로 python설치에 대한 정리는 넘어가기로 한다.  
![screenshot-pythonversion](img/1.png)

## 2) pip설치
pip는 python에 사용되는 각종 패키지를 설치, 업그레이드,삭제하도록 하는 패키지 매니저다. pip는 django를 비롯해 python에 관련된 패키지를 쉽고 편하게 관리할 수 있도록 해준다.  
get-pip.py를  https://pip.pypa.io/en/stable/installing/ 에서 다운받아 터미널에서 실행해서 pip를 설치할 수 있다.  

### pip이 설치되어 있는지 확인
$ pip --version  

### 처음 설치하는 경우
$ cd [다운로드 받은 디렉터리]  
$ python get-pip.py  
(만약 python3를 사용하고 있을 경우는 $ python3 get-pip.py)  

### 이미 설치되어 있고, 오래된 버전의 pip을 사용하고 있는 경우  
$ sudo pip install --upgrade pip  

## 3) python version manager 설치
작업하고 있는 PC또는 서버의 개발환경이 변하거나 python의 버전이 업그레이드 되거나 변하더라도 이전에 지정해놓은 버전 위에서 계속 돌아갈 수 있도록 가상환경을 구축하는 방법은 여러가지가 있다.  
 1. **vertualenv** - "Virtual Python Environment builder"  
   python3에 내장된 도구다. python3 -m venv 명령을 통해 설치되어 있는지 확인 가능하다.  
 2. **pyenv** - "Simple Python Version Management"  
   pyenv로 virtualenv까지도 관리할 수 있다. pyenv는 bash를 기반으로 한 환경이다. MS Window에서는 동작하지 않는다. 대신 MS Window에서는 pip install virtualenv를 통해 간단히 설정할 수 있다.   
[difference between pyenv and virtualenv](http://stackoverflow.com/questions/29950300/what-is-the-relationship-between-virtualenv-and-pyenv)  
[ MS윈도우에서 virtualenv 설치하는 방법 ](http://ssse.tistory.com/36)
 3. **autoenv**  
   pyenv와 virtualenv를 통해 의존성을 해결할 수 있다. 하지만 작업할 때마다 설정을 일일이 설정해주어야 한다. 프로젝트 디렉터리로 이동할 경우 자동으로 개발환경을 설정해주는 스크립트 방식이 있는데 이것이 autoenv다.  

### pyenv설치
#### pyenv 버전확인
$ pyenv --version  

#### 존재하지 않는다면...
$sudo chown -R $(whoami) /usr/local
참고자료 :  
[Elcapitan 보안 강화때문에 brew update안되는 현상해결법](http://hssuh.tistory.com/469)  
[Homebrew 설치 및 Sierra 관련 이슈들](https://xho95.github.io/macos/sierra/package/homebrew/issues/2017/01/13/Using-Homebrew-and-some-Issues.html)  
$ brew update  
$ brew install pyenv  
\# 권한 원상복구
$ sudo chmod 0755 /usr/local  
$ sudo chown root:wheel /usr/local  
### 현재 사용하고 있는 파이썬 버전 확인
$ pyenv versions  
\* system (set by /Users/soon/.pyenv/version)  
기본으로 설치되어 있는 python을 사용하고 있다고 알려준다.  

#### 특정버전의 파이썬을 pyenv위에 설치하는 방법
설치 가능한 모든 버전의 파이썬 리스트 출력  
$ pyenv install --list  
만약 2.7.10을 설치하고 싶다면  
$ pyenv install 2.7.10  
$ python --version  

### virtualenv 설치
pyenv로 virtualenv의 버전도 관리할 수 있도록 pyenv-virtualenv를 설치하는 과정을 정리하고자 한다.  
$ brew install pyenv-virtualenv  
$ vim ~/.zshrc  
...  
\# 아래의 내용을 입력하고 저장한다.  
\# 만약 bash쉘을 쓴다면 ~/.bashrc나 ~/.bash_profile에 입력한 후 저장한다.  
\# 내 경우는 zsh을 사용하고 있어서 ~/.zshrc를 열어서 수정했다.  
```bash
export PATH="$HOME/.pyenv/bin:$PATH"  
eval "$(pyenv init -)"  
eval "$(pyenv virtualenv-init -)"  
```
ess + :wq 입력후 저장하고 종료후 아래의 명령을 내린다.
$ exec $SHELL  
  또는  
$ source ~/.zshrc  

```
참고)  
만약 dyld: Library not loaded: /usr/local/opt/readline/lib/libreadline.6.dylib Referenced from: /usr/local/bin/bash 와 같은 메시지를 출력하면서 진행이 안된다면  
$ brew upgrade bash  
를 수행한다. bash가 너무 오래된 버전이어서 생기는 오류다.  
```
([참고자료](https://github.com/Homebrew/homebrew-core/issues/5799))  
## 4) pyenv에 python환경 설치
$ pyenv version  
$ pyenv install --list  
$ pyenv install 2.7.10  
(mac os x를 사용하고 있는 경우 커맨드 라인 도구를 설치하지 않을 경우 에러를 낸다. 0)에서 정리해놓은 내용 참고해서 설치할 것)  
  
// 현재 pyenv 버전설정  
$ pyenv versions  
  
// [참고자료 - pystagram만들기 강좌](http://blog.hannal.com/2014/8/start_with_django_webframework_02/)의 내용중 잘못된 내용이 있다. - (pyenv shell 버전명 은 올바른 명령어가 아니다....)   
  
## 5) virtualenv로 가상환경 설정
// test-env-2.7.10이라는 이름의 가상환경을 python-2.7.10기반으로 구성  
$ pyenv virtualenv 2.7.10 test-env-2.7.10  
  
// test-env-2.7.10 이라는 가상환경을 활성화  
$ pyenv activate test-env-2.7.10  
  
// pyenv에 설정된 모든 가상환경들 확인  
$ pyenv versions  
 system  
  2.7.10  
  2.7.10/envs/test-env-2.7.10  
\* test-env-2.7.10 (set by PYENV_VERSION environment variable)  
$ pyenv deactivate test-env-2.7.10  

#### 참고 : $ pyenv activate [사용자 정의 버전] 이 제대로 수행되지 않을때
Failed to activate virtualenv.라는 에러메시지를 내는 경우가 있다. 이것은
  > * ~/.zshrc  
  > * ~/.bashrc  
  > * ~/.bash_profile  

에 pyenv관련 환경설정을 추가하지 않았기 때문에 생기는 문제다. 위의 세 파일 중 하나를 열어서 아래의 내용을 제일 아래에 입력해준다.  
```
export PATH="$HOME/.pyenv/bin:$PATH"  
eval "$(pyenv init -)"  
eval "$(pyenv virtualenv-init -)"  
```
나의 경우는 eval "$(pyenv init -)", export PATH="$HOME/.pyenv/bin:$PATH"를 적지 않아서 위와 같은 에러가 발생했었다.  
  
저장한 후 shell에 아래와 같은 명령을 내린다.  
$ source ~/.zshrc  
  또는  
$ exec "$SHELL"  
[참고자료 : PYTHON 3.4.3 설치하기](http://yoonkiwoong.net/archives/tag/pyenv)  
  
설정해놓은 개발환경들은  
> * $ pyenv versions  
>   또는 
> * $ ls ~/.pyenv/versions  

명령을 통해 확인가능하다.  

## 6) requirements.txt - pip 의존성 패키지 버전 명시 문서 작성
#### 버전관리 문서, requirements.txt
> 딱히 제목으로 지정할 만한 단어가 떠오르지 않아 제목을 버전명시 문서작성이라고 썼다. 버전명시 문서라고 해서 거창한것을 의미하는 것이 아니다. 스프링의 pom.xml,maven Node.js의 package.json,npm 등을 이용해 버전이 명시된 pom.xml, package.json이 존재해야 팀 프로젝트시 팀원들과 사용하고 있는 팀 프로젝트가 동일한 환경, 동일한 버전, 동일한 라이브러리,모듈 속에서 패키지가 관리되어 의존성 문제가 발생하지 않는다.  
레일즈에서는 프로젝트별로 Gemfile이라는 파일이 있어서 라이브러리, 모듈을 관리하고 있다고 한다...  

django, flask에서는 이 문제를 해결해줄 수 있는 자체적인 내장 기능은 없는 것으로 보인다. 따라서 아래와 같은 방식으로 환경을 맞춰주는 편이라고 한다. ([참고자료 - pyenv,pip,virtualenv설치](https://dobest.io/how-to-set-python-dev-env/))  
#### requirements.txt 문서 생성 (like pom.xml, package.json)
\# 처음으로 프로젝트를 생성하고 개발환경을 구축한 사용자는 아래와 같은 명령어로 requirements.txt를 정의한다.  
$ pip list --format=legacy > requirements.txt  
  
\# 프로젝트를 공유하는 협업 사용자들은 아래와 같은 명령을 통해 의존성 패키지들을 다운로드 한다.  
$ pip install -r requirements.txt  

#### (*참고) pip list>requirements시 에러
([참고자료](https://hyesun03.github.io/2016/11/28/piplist/))  
$ pip list > requirements.txt 수행시  
```
DEPRECATION: The default format will switch to columns in the future. You can use --format=(legacy|columns) (or define a format=(legacy|columns) in your pip.conf under the [list] section) to disable this warning.  
```
와 같은 에러가 발생하면서 수행되지 않는 경우가 있다. 이 같은 문제는 두가지 방식으로 해결 가능하다. 
> * CLI명령시 옵션을 주어 명령을 주는 방식 
> * 옵션 자체를 ~/.pip/pip.conf에 지정해놓는 방식 
> (홈 디렉터리의 .pip/pip.conf에 옵션을 명시해 저장)

#### CLI명령시 옵션을 주어 해결하는 방식
column형식(표,테이블형식)으로 표시할지 legacy형식(단순나열)형식으로 표시할지 여부를 옵션으로 지정해주고 명령을 내리면 된다.   
$ pip list --format=columns  
   or
$ pip list --format=legacy  

#### ~/.pip/pip.conf에 옵션을 지정해 저장하는 방식
~/.pip/pip.conf파일의 [list] 섹션 아래에 format=legacy 또는 format=columns를 정의해줌으로서 해결 가능하다.([참고자료](http://stackoverflow.com/questions/40477335/where-is-pip-conf-in-my-mac-which-python-was-installed-via-homebrew))  
  
pip가 설치되어 있어도현재 사용자의 홈디렉터리에 .pip디렉터리(~/.pip)가 존재하지 않는 경우가 있다. 이 경우 홈 디렉터리에 .pip디렉터리를 생성하고, 그 안에 pip.conf파일을 생성하여 아래의 내용을 입력하고 저장하면 된다.  
```
[list]  
format=columns  
```
## 7) autoenv 설치
### autoenv는...
autoenv를 설치하는 이유는 새로운 세션의 터미널을 열때마다, 디렉터리를 이동해 디렉터리가 변경될 때마다 디렉터리마다 디렉터리 내에 존재하는 .env라는 hidden 파일을 자동으로 찾아서 그 프로젝트 디렉터리의 환경에 맞게끔 개발할 수 있도록 하는 편리한 도구이기 때문이다.  

Homebrew를 통해 autoenv를 설치했을 때 이러한 동작을 수행하는 것은  
/usr/local/opt/autoenv/activate.sh 파일이다.   
autoenv의 오픈소스 리포지터리는 [github>kennethreitz>autoenv](https://github.com/kennethreitz/autoenv/blob/master/activate.sh) 이다. 오픈소스 만세!!!  

### autoenv 설치
$ brew install autoenv  
\# 매 세션마다 autoenv를 자동으로 실행할 수 있도록 설정
\# bash를 사용할 경우 ~/.bashrc 또는 ~/.bash_profile에 >>을 통한 리다이렉션으로 저장할 것 (맨 마지막에 적혀있는 ~/.zshrc를 ~/.bashrc또는 ~/.bash_profile로 지정해 명령내릴 것)  

$ echo 'source /usr/local/opt/autoenv/activate.sh' >> ~/.zshrc  
$ source ~/.zshrc  

### autoenv 사용하기  
.env파일을 생성해서 그 안에 bash쉘 또는 zsh의 명령을 기록해놓으면 activate.sh가 자동으로 그 명령을 수행해준다. 자세한 내용은 예를 들어서 정리해보고자 한다.  
$ mkdir test-autoenv  
$ cd test-autoenv  
$ echo 'echo "Hello, this is test-autoenv/.env file. Nice to meet you!!!"' > .env  
$ cd ..  
$ cd test-autoenv  
Hello, this is test-autoenv/.env file. Nice to meet you!!!  

### autoenv의 실제 사용예
$ cd test-autoenv  
$ vim .env 
echo ""  
echo "Python Virtual Env , pyenv : test-env-2.7.10"  
echo ""  

pyenv shell test-env-2.7.10  
pyenv activate  
$ cd ..
$ cd test-autoenv
특정 디렉터리에 진입할때마다 수행하도록 하는 방식이다.  

## 8) 설정해놓은 가상개발환경 위에 django 설치
$ pyenv install -list | grep 2.7.11  
$ pyenv install 2.7.11  
$ pyenv virtualenv 2.7.11 pysta-2.7.11  
$ pyenv shell pysta-2.7.11  
$ pyenv activate  
$ mkdir pysta && cd pysta  
$ touch .env  
$ vim .env  
echo "------------------------------------------------"  
echo "| Python Virtual Env , pyenv : test-env-2.7.10 |"  
echo "------------------------------------------------"  

pyenv shell pysta-2.7.11  
pyenv activate  


wq를 눌러 저장하고 빠져나온다.  
$ pip install django  
\# django를 pysta-2.7.11이라는 가상환경에 설치하는 명령  
$ python -c "import django; print(django.\_\_file\_\_)"  
/Users/soon/.pyenv/versions/pysta-2.7.11/lib/python2.7/site-packages/django/\_\_init\_\_.pyc  
\# 내 경우는 홈디렉터리/.pyenv/versions/pysta-2.7.11 밑에 lib/python2.7/site-packages 라는 곳에 django가 설치된 것을 확인가능하다.  
\# pyenv-virtualenv를 통해 설치되는 모든 패키지는 [홈디렉터리]/.pyenv/versions/[가상환경명]/밑에 설치되는 것을 확인가능하다.  

### 설치한 django의 버전 확인
\# 파이썬 명령 모드 진입  
$ python  
\# django 모듈 import  
\>\>\> import django  
\# django 모듈 print  
\>\>\> print(django.get_version());  
1.11  
참고자료 [Checking Django Version in a Command Prompt](http://www.dark-hamster.com/programming/checking-django-version-in-a-command-prompt/)  

### 특정 버전의 django를 설치하고자 할때 
직접 수행해본 적은 없지만 "Lightweight Django - Julia Elman & Mark Lavin"의 Prerequisites>Python>Python>Python Packages에서 설명하는 방식은 아래와 같드아..  
$ pip install Django==1.8  

## 9) jupyter notebook설치

  

======
