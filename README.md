# KaironAI - AI Research Assistant  
**A Production-Grade Dual-Agent System for Intelligent Web Research**  

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/UI-Framework-FF4B4B?logo=streamlit)](https://streamlit.io/)
[![LangGraph](https://img.shields.io/badge/Workflow-LangGraph-01BEF2)](https://langchain.com/langgraph)

## 🚀 Project Overview  
A sophisticated AI system demonstrating modern LLM orchestration capabilities, featuring:  
✅ **Dual-Agent Architecture** (Research + Answer Drafting Agents)  
✅ **Web Crawling** with Tavily API integration  
✅ **AI-Powered Analysis** using Google Gemini Pro  
✅ **Production-Ready Workflow** with LangGraph  
✅ **Interactive Web UI** built with Streamlit  

**Key Technical Showcases**:  
- Clean separation of concerns between agents  
- Robust error handling and API management  
- Environment configuration best practices  
- Modular and extensible architecture  

---

## 🛠 Technical Stack  
| Component              | Technology           | Purpose                          |
|------------------------|----------------------|----------------------------------|
| **Core Framework**     | Python 3.10          | Base programming language        |
| **Workflow Engine**    | LangGraph            | Agent orchestration              |
| **AI Models**          | Google Gemini Pro    | Research analysis & answer generation |
| **Web Interface**      | Streamlit            | User interaction layer           |
| **Web Crawling**       | Tavily API           | Real-time web research           |
| **Configuration**      | python-dotenv        | Secure credential management     |

---

## 🧠 System Architecture  
```mermaid
graph TD
    A[User Input] --> B(Streamlit UI)
    B --> C{Research Agent}
    C --> D[Tavily API]
    D --> E[Raw Web Data]
    E --> F[Gemini Analysis]
    F --> G{Answer Drafter}
    G --> H[Structured Output]
```
# Key Components

## Research Agent (`research_agent.py`)
- **Web Crawling and Data Aggregation**: Handles the crawling of web pages and aggregates data from various sources.
- **Data Preprocessing and Validation**: Preprocesses and validates data to ensure accuracy and quality.
- **Error Handling for API Failures**: Implements robust error handling to manage API failures gracefully.

## Answer Drafter (`answer_drafter.py`)
- **LLM-Powered Response Generation**: Generates responses using a large language model.
- **Markdown Formatting**: Formats the generated content in Markdown.
- **Quality Assurance Checks**: Conducts quality assurance checks to maintain response standards.

