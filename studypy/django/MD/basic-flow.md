# Django개발의 일반적인 순서
## 프로젝트 생성
```bash
$ django-admin.py startproject basic_prj
$ tree
.
└── basic_prj
    ├── basic_prj
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── manage.py
```
## 프로젝트 기본 구조
$ django-admin.py startproject [프로젝트명]으로 프로젝트를 생성하면 [프로젝트명]으로 디렉터리가 생기고 그 내부에도 [프로젝트명] 디렉터리가 생기는 것을 볼 수 있다. 추후 상위 디렉터리의 [프로젝트명]과 하위디렉터리의 [프로젝트명]을 지칭할때 혼동될 여지가 있기 때문에 상위 디렉터리의 [프로젝트명]을 수정해주는 것이 정신건강상 이롭다.  
```bash
$ mv basic_prj helloworld
```
  
## 어플리케이션 생성, 샘플어플리케이션 작성 
보통 django 프로젝트 진행시 어떠한 기능을 추가해서 개발하고자 할 때 그 단위를 어플리케이션이라는 개념으로 따로 분류해서 개발한다. 여기서 말하는 어플리케이션은 하나의 디렉터리다. 즉, 무언가 신기능을 독립적으로 추가하고자 할때 디렉터리를 생성해 그곳에서 독립적으로 개발하는 방식이다.  
### 어플리케이션 생성
```bash
$ cd helloworld
$ python manage.py startapp sample_app
$ ls
basic_prj  manage.py  sample_app
$ tree
.
├── basic_prj
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── settings.py
│   ├── settings.pyc
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── sample_app
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py

3 directories, 14 files

```

