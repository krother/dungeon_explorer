
import httpx

BASE = "http://localhost:8000"

def main():
    r = httpx.get(BASE)
    print(r.json())    
    print(r.status_code)    
    
    word_count_r = httpx.post(BASE + "/count_words", json={"text": "hello world"})   
    print(word_count_r.json())    
    
    print(word_count_r.status_code)
    
    if __name__ == "__main__":
        main()
