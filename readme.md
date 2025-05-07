0. installation requirements:
```shell
(.venv) ➜  browser-use git:(main) ✗ python --version    
Python 3.11.11 
```
1. Playwright 浏览器驱动：
```shell
(.venv) ➜  browser-use git:(main) ✗ playwright install chromium
```
2. 安装依赖：
```shell
(.venv) ➜  browser-use git:(main) ✗ pip install -r requirements.txt
```

- 主要依赖：
  - playwright
  - langchain_google_genai
  - browser_use

3. 更新prompt/task内容，`python crawl.py` 执行任务。

![1.jpg](docs%2F1.jpg)
![4.jpg](docs%2F4.jpg)
![2.jpg](docs%2F2.jpg)
![3.jpg](docs%2F3.jpg)
