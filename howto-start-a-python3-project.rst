How to start a python3 project
********************************


:date: 2017-05-05
:modified: 2017-05-05
:slug: howto-start-a-python3-project
:tags: howto, start
:category: software
:author: Dormouse Young
:summary: If we want to start a new python3 project, What we should do
          first?

If we want to start a new python3 project, What we should do first?

- start a git project online
- git clone your_git_project_url
- mkvirtualenv -p python3 project_name
- pip install your_project_need_package
- pip freeze > requirements.txt(use ``pip install -r requirements.txt`` to
  restore)

