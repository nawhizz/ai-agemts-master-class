import time
from crewai.tools import tool
from crewai_tools import SerperDevTool
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

search_tool = SerperDevTool(
    n_results=30,   # 반환할 검색 결과의 개수
)


@tool
def scrape_tool(url: str):
    """
    Use this when you need to read the content of a website.
    Returns the content of a website, in case the website is not available, it returns 'No content'.
    Input should be a `url` string. for example (https://www.reuters.com/world/asia-pacific/cambodia-thailand-begin-talks-malaysia-amid-fragile-ceasefire-2025-08-04/)
    """

    print(f"Scrapping URL: {url}")

    # Playwright를 사용하여 브라우저 세션 시작
    with sync_playwright() as p:

        # chromium 브라우저를 headless 모드로 실행
        browser = p.chromium.launch(headless=True)

        # 새 페이지 생성
        page = browser.new_page()

        # 지정한 URL로 이동
        page.goto(url)

        # 페이지가 완전히 로드될 때까지 5초 대기
        time.sleep(5)

        # 페이지의 HTML 소스 가져오기
        html = page.content()

        # 브라우저 종료
        browser.close()

        # BeautifulSoup을 사용하여 HTML 파싱
        soup = BeautifulSoup(html, "html.parser")

        # 제거할 불필요한 태그 목록 정의
        unwanted_tags = [
            "header",
            "footer",
            "nav",
            "aside",
            "script",
            "style",
            "noscript",
            "iframe",
            "form",
            "button",
            "input",
            "select",
            "textarea",
            "img",
            "svg",
            "canvas",
            "audio",
            "video",
            "embed",
            "object",
        ]

        # 불필요한 태그를 모두 제거
        for tag in soup.find_all(unwanted_tags):
            tag.decompose()

        # 텍스트만 추출, 구분자는 공백
        content = soup.get_text(separator=" ")

        # 내용이 없으면 'No content' 반환
        return content if content != "" else "No content"