# DEEPRESEARCHER 

### A Multi Agent AI Research System

**DEEPRESEARCHER** is a multi-agent AI project that automates the process of researching a topic and generating a structured research report.

Instead of relying on a single **LLM** to do everything, the project uses specialized agents and chains, each responsible for a different stage of the research process. It searches the web, extracts useful information from relevant websites, prepares a detailed report, and reviews the final output.

The project demonstrates the basic working of a **Deep Research workflow used in AI systems**, where multiple steps work together to turn a simple question into meaningful research.

## 🚀 How It Works

The entire research process is divided into four stages:

**1. Search Agent**

The Search Agent uses the Tavily **API** to search the web for recent and relevant information about the given topic. It collects page titles, URLs, and short content snippets.

**2. Reader Agent**

The Reader Agent identifies a relevant **URL** from the search results and uses the scraping tool to extract deeper content from the webpage. BeautifulSoup helps clean the webpage content by removing unnecessary elements such as scripts, navigation, and footers.

**3. Writer Chain**

Once the research information is collected, it is passed to the Writer Chain. Using Gemini, it combines the search results and extracted content into a structured report containing:

- Introduction
- Key Findings
- Conclusion
- Sources

**4. Critic Chain**

The generated report is passed to the Critic Chain for review. It evaluates the report, highlights its strengths, identifies areas for improvement, and provides an overall score with a short verdict.

##  Project Workflow

<img width="516" height="757" alt="Screenshot 2026-10-01 164826" src="https://github.com/user-attachments/assets/ead2390d-3f9e-4913-b34e-713e20d09cc2" />


##  Tech Stack & APIs Used

| Technology        | Purpose                                    |
| ----------------- | ------------------------------------------ |
| Python            | Core programming language                  |
| LangChain         | Building agents, tools, and LLM chains     |
| Google Gemini API | Powers the agents, writer, and critic      |
| Tavily API        | Web search and information retrieval       |
| BeautifulSoup     | Extracts and cleans webpage content        |
| Requests          | Sends HTTP requests to webpages            |
| Streamlit         | Builds the interactive user interface      |
| Python-dotenv     | Manages API keys and environment variables |

##  Key Features

- Multi-agent architecture with separate responsibilities.
- Automated web search using Tavily.
- Website content extraction using BeautifulSoup.
- AI generated structured research reports.
- Automated report evaluation and feedback.
- Interactive Streamlit interface.
- Modular code structure for agents, tools, and pipeline execution.



##  Project Objective

The main goal of **DEEPRESEARCHER** is to explore how multiple AI agents can collaborate to perform research tasks. It demonstrates how web search, information extraction, content generation, and AI-based review can be connected into a single automated workflow.

Rather than making one model handle every task, the project separates responsibilities into smaller stages, making the overall research process easier to understand, develop, and extend.

<img width="1353" height="940" alt="Screenshot 2026-10-01 163121" src="https://github.com/user-attachments/assets/6590d90a-1648-4294-b97d-41892f8c826a" />

<img width="1176" height="833" alt="Screenshot 2026-10-01 163133" src="https://github.com/user-attachments/assets/0b181910-9e37-414c-b279-83df0a125162" />

---

*Built as a exploration of Multi Agent AI Systems, LangChain, and Deep Research workflows.*
