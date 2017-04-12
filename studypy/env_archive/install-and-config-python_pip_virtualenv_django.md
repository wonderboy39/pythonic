# python, pip, virtualenv, django 환경설정
설치 및 환경설정 과정은 PC개발환경, 원격 서버 개발환경으로 나누어 정리할 것이며, 원격 서버 개발환경 설정은 차후 AWS t2 micro를 발급받아 정리해보려 한다.  

## 0) mac os x 에서의 선행사항
명령어 도구(command line tool)를 설치하지 않으면 python빌드시 가끔 python소스코드를 보여주면서 에러가 났다는 메시지를 자주 접할 수 있다. 이 경우 아래의 명령어를 Terminal에서 수행하여 해결할 수 있다.(나의 경우는 $pyenv install 2.7.10을 하는동안 에러가 발생했다.)   
// 설치되어있는지, 버전은 몇인지 확인  
$ xcode-select --version  
// 명령어 도구 설치  
$ xcode-select --install  

## 1) python설치
mac에는 python2.7이 기본으로 설치 되어있다. python 2.7.x버전의 python을 사용할 것이므로 python설치에 대한 정리는 넘어가기로 한다.  
![1](img/1.png)

## 2) pip설치
pip는 python에 사용되는 각종 패키지를 설치, 업그레이드,삭제하도록 하는 패키지 매니저다. pip는 django를 비롯해 python에 관련된 패키지를 쉽고 편하게 관리할 수 있도록 해준다.  
get-pip.py를  https://pip.pypa.io/en/stable/installing/ 에서 다운받아 터미널에서 실행해서 pip를 설치할 수 있다.  


##### pip이 설치되어 있는지 확인
$ pip --version

##### 처음 설치하는 경우
$ cd [다운로드 받은 디렉터리]
$ python get-pip.py
(만약 python3를 사용하고 있을 경우는 $ python3 get-pip.py)  

##### 이미 설치되어 있고, 오래된 버전의 pip을 사용하고 있는 경우  
$ sudo pip install --upgrade pip

## 3) python version manager 설치
작업하고 있는 PC또는 서버의 개발환경이 변하거나 python의 버전이 업그레이드 되거나 변하더라도 이전에 지정해놓은 버전위에서 계속 돌아갈 수 있도록 가상환경을 구축하는 방법이 여러가지 있다.
 1. vertualenv - "Virtual Python Environment builder"
   python3에 내장된 도구다. python3 -m venv 명령을 통해 설치되어 있는지 확인 가능하다.
 2. pyenv - "Simple Python Version Management"
   pyenv로 virtualenv까지도 관리할 수 있다. pyenv는 bash를 기반으로 한 환경이다. window에서는 동작하지 않는다. (pyenv에 대한 자세한 설명은 [difference between pyenv and virtualenv](http://stackoverflow.com/questions/29950300/what-is-the-relationship-between-virtualenv-and-pyenv) 를 참고.)
 3. autoenv
   pyenv와 virtualenv를 통해 의존성을 해결할 수 있다. 하지만 작업할 때마다 설정을 일일이 설정해주어야 한다. 프로젝트 디렉터리로 이동할 경우 자동으로 개발환경을 설정해주는 스크립트 방식이 있는데 이것이 autoenv다.  

### pyenv설치
##### pyenv 버전확인
$ pyenv --version

##### 존재하지 않는다면...
$ sudo chown -R $(whoami):admin /usr/local  
참고자료 : [Elcapitan 보안 강화때문에 brew update안되는 현상해결법](http://hssuh.tistory.com/469)  
$ brew update  
$ brew install pyenv  

##### 현재 사용하고 있는 파이썬 버전 확인
$ pyenv version  
\* system (set by /Users/soon/.pyenv/version)  
기본으로 설치되어 있는 python을 사용하고 있다고 알려준다.  

##### 특정버전의 파이썬 설치
설치 가능한 모든 버전의 파이썬 리스트 출력  
$ pyenv install --list  
만약 2.7.10을 설치하고 싶다면  
$ pyenv shell 2.7.10  
$ python --version  

### virtualenv 설치
pyenv로 virtualenv의 버전도 관리할 수 있도록 pyenv-virtualenv를 설치하는 과정을 정리하고자 한다.  
$ brew install pyenv-virtualenv  
$ echo $(pyenv init -)  
$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc  
$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc  
$ exec $SHELL


참고)
만약 dyld: Library not loaded: /usr/local/opt/readline/lib/libreadline.6.dylib Referenced from: /usr/local/bin/bash 와 같은 메시지를 출력하면서 진행이 안된다면   
$ brew upgrade bash  
를 수행한다. bash가 너무 오래된 버전이어서 생기는 오류다.  
([참고자료](https://github.com/Homebrew/homebrew-core/issues/5799))
  

### pyenv에 python환경 설치
$ pyenv version  
만약 버전명과 같은것이 안뜨고 System 어쩌구가 뜬다면 사용하려는 버전의 python을 시스템이 아닌 pyenv에 설치해야한다.  
$ pyenv install --list  
$ pyenv install 2.7.10  
(mac os x를 사용하고 있는 경우 커맨드 라인 도구를 설치하지 않을 경우 에러를 낸다. 0)에서 정리해놓은 내용 참고해서 설치할 것)  

// 현재 pyenv 버전설정  
$ pyenv versions  

// [참고자료 - pystagram만들기 강좌](http://blog.hannal.com/2014/8/start_with_django_webframework_02/)의 내용중 잘못된 내용이 있다. - (pyenv shell 버전명 은 올바른 명령어가 아니다....)   
  
## 5) virtualenv로 가상환경 설정
$ pyenv virtualenv 2.7.10 test-env-2.7.10  
$ pyenv activate test-env-2.7.10  
$ pyenv versions  
 system  
  2.7.10  
  2.7.10/envs/test-env-2.7.10  
\* test-env-2.7.10 (set by PYENV_VERSION environment variable)  
$ pyenv deactivate test-env-2.7.10  
  
#### 참고 : $ pyenv activate [사용자 정의 버전] 이 제대로 수행되지 않을때
$ pyenv activate [사용자 정의 환경]이 제대로 수행되지 않고 Failed to activate virtualenv.라는 메시지를 접할수 있다. 이 경우 ~/.zshrc나 ~/.bashrc또는 ./bash_profile에 아래의 내용을 적어준후 저장해야 한다.  
export PATH="$HOME/.pyenv/bin:$PATH"  
eval "$(pyenv init -)"  
eval "$(pyenv virtualenv-init -)"  
나의 경우는 eval "$(pyenv init -)"과 export PATH="$HOME/.pyenv/bin:$PATH"를 적지 않아서 위와 같은 에러가 발생했었다.  
  
저장한 후 shell에 아래와 같은 명령을 내린다.  
$ source ~/.zshrc  
  또는  
$ exec "$SHELL"  
[참고자료 : PYTHON 3.4.3 설치하기](http://yoonkiwoong.net/archives/tag/pyenv)  
  
설정해놓은 개발환경들은 $pyenv versions로 확인할 수도 있고, $ ls ~/.pyenv/versions 명령을 통해 확인가능하다.  

## 6) autoenv 설치
  
  
## 7) 설정해놓은 가상개발환경 위에 django 설치
  
  
  
  
======



## 4) virtualenv로 가상환경 설정
[참고자료 - pystagram만들기 강좌](http://blog.hannal.com/2014/8/start_with_django_webframework_02/)
django를 설치하기 전에 virtualenv를 통해 가상환경 설정을 진행후에 하도록 한다. 실습 프로젝트용 가상환경을 생성하여 그 환경내에서 django를 운영하도록 하기 위해서다. virtualenv로 하나의 프로젝트용 가상환경을 만들기 위해서는 아래와 같이 명령어를 입력하면 된다.  
// python3 에서...
$ python3 -m venv env_planner
// python2.7.x 에서...

## 5) django설치