import requests
from bs4 import BeautifulSoup

def get_news_titles(search_keyword):
    # 검색 URL 생성
    url = f"https://search.naver.com/search.naver?where=news&sm=top_hty&fbm=0&ie=utf8&query={search_keyword}"
    
    # User-Agent 설정
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    # 웹 페이지 요청
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        # HTML 파싱
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 뉴스 제목 요소 찾기
        news_titles = soup.select("a.news_tit")
        
        # 제목 텍스트 추출
        titles = []
        for title in news_titles:
            titles.append(title.get_text())
            
        return titles
    else:
        print(f"Error: {response.status_code}")
        return []

if __name__ == "__main__":
    # 검색어 설정
    search_keyword = "아이폰17"
    
    # 뉴스 제목 가져오기
    titles = get_news_titles(search_keyword)
    
    # 결과 출력
    print(f"'{search_keyword}' 관련 뉴스 제목:")
    print("-" * 50)
    for i, title in enumerate(titles, 1):
        print(f"{i}. {title}")