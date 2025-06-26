### [2025. 06.26] 기준 RAG python 예제 수록
- GPT-4 대신 HuggingFace, Gemini-2.5 적극 사용 (무료)
  - ollama로 기본 구성하려 했으나 PC 메모리 부족으로 일부만 사용
- `Anaconda3`, `VSCode`, `jupyter`로 개발 환경 구성
- `streamlit` 으로 클라이언트 구성
- 참고: [study/book/랭체인으로 LLM 기반의 AI 서비스 개발하기.md](https://github.com/hana2set/study/blob/main/%EA%B8%B0%ED%83%80/book/%EB%9E%AD%EC%B2%B4%EC%9D%B8%EC%9C%BC%EB%A1%9C%20LLM%20%EA%B8%B0%EB%B0%98%EC%9D%98%20AI%20%EC%84%9C%EB%B9%84%EC%8A%A4%20%EA%B0%9C%EB%B0%9C%ED%95%98%EA%B8%B0.md)

### 라이브러리 목록
- `python 3.11` 기준 라이브러리 최신버전 사용
    ```cmd
    pip install langchain

    pip install langchain_community
    pip install huggingface-hub
    pip install streamlit
    pip install langchain-ollama
    pip install langchain-google-genai
    
    pip install pypdf
    pip install tiktoken
    pip install faiss-cpu
    pip install sentence-transformers

    pip install wikipedia
    pip install numexpr
    
    pip install chromadb
    pip install unstructured
    pip install PyPDF2
    pip install streamlit-chat
    pip install langchain-experimental
    pip install pandas
    pip install tabulate
    ```
- 주요 라이브러리 버전
    ```cmd
    langchain==0.3.26
    langchain-community==0.3.26
    langchain-core==0.3.66
    langchain-google-genai==2.1.5
    langchain-ollama==0.3.3
    huggingface-hub==0.33.0

    streamlit==1.46.0
    faiss-cpu==1.11.0
    chromadb==1.0.13
    ```
--- 

출처   
`랭체인으로 LLM 기반의 AI 서비스 개발하기`, 서지영 지음
https://github.com/gilbutITbook/080413  
