# Interactive-AI-Hub

## Project Overview
Interactive-AI-Hub aims to develop a sophisticated chatbot system that leverages advanced NLP techniques and the LLaMA2 70B model to extract, synthesize, and present information from a company's annual public reports. This project addresses the inefficiencies and complexities involved in manually extracting valuable data from these reports, thereby enhancing accessibility and decision-making for stakeholders.

## Abstract
The Interactive-AI-Hub project focuses on creating an intelligent chatbot capable of understanding and interpreting complex annual reports. By utilizing advanced natural language processing (NLP) capabilities, specifically the LLaMA2 70B model, the chatbot will provide accurate and timely responses to frequently asked questions (FAQs), enabling stakeholders to access critical financial and operational information efficiently. This solution aims to streamline the extraction of insights from unstructured data, making it easier for investors, analysts, and other stakeholders to make informed decisions.

## Problem Statement

### Understanding of the Problem
Extracting valuable information from a company's annual public reports to answer FAQs is currently inefficient and complex. These reports contain extensive financial, sustainability, and operational data, often scattered across numerous pages and presented in various formats. Manually parsing this information is time-consuming and prone to errors, highlighting the need for an automated system that can accurately interpret and present this data.

### Most Challenging Aspect
The main challenge lies in the advanced NLP capabilities required to accurately understand and interpret the content of annual reports. These documents are highly technical and include unstructured text, tables, and charts. The chatbot must be capable of extracting relevant data and providing real-time FAQ generation and comparative analysis through sophisticated contextual understanding and information synthesis.

## Approach

1. **Data Collection**: Obtain digital formats of a company's annual public reports.
2. **Data Preprocessing**: Clean and structure the report data, extracting text, tables, and figures, and converting them into a structured format for analysis.
3. **Natural Language Processing (NLP)**: Utilize the LLaMA2 70B model for text analysis, entity recognition, and topic modeling to identify key data points.
4. **FAQ Generation**: Develop algorithms to generate FAQs based on the report's content, covering various aspects like finance, sustainability, and operations.
5. **User Interface**: Create a user-friendly interface (web or mobile application) for stakeholders to interact with the chatbot.
6. **Comparative Analysis**: Develop a module for comparative analysis, allowing users to compare the company's performance with industry benchmarks or historical data.
7. **Customization**: Implement features enabling users to customize their queries and insights.
8. **Data Visualization**: Generate data visualizations, such as charts and graphs, to represent complex financial and sustainability metrics.

## Key Features

- **Advanced NLP**: Utilizing LLaMA2 70B model for high-accuracy text understanding and interpretation.
- **Real-Time FAQ Generation**: Dynamic generation of FAQs from the report content.
- **User-Friendly Interface**: Interactive and intuitive interface for seamless user experience.
- **Comparative Analysis**: Tools for comparing company performance with benchmarks.
- **Customization**: User-defined queries and personalized insights.
- **Data Visualization**: Graphical representations of complex data for easier understanding.

## Methodology

1. **Data Collection and Preprocessing**
   - Collect digital annual reports.
   - Clean and structure the data for analysis.
2. **NLP Model Integration**
   - Implement LLaMA2 70B model for text analysis and entity recognition.
   - Utilize libraries like faiss-cpu, tiktoken, Ctransformers, and huggingface-hub.
3. **FAQ Generation and Comparative Analysis**
   - Develop algorithms for generating FAQs and conducting comparative analysis.
   - Integrate langchain-community for enhanced language processing.
4. **Interface Development**
   - Build a user-friendly interface using Streamlit.
5. **Customization and Visualization**
   - Implement customizable query features.
   - Use Seaborn, Matplotlib, and Plotly for data visualization.

## Technology Stack

- **NLP Model**: LLaMA2 70B
- **Programming Language**: Python
- **NLP Libraries**: NLTK, spaCy
- **Machine Learning Frameworks**: PyTorch
- **Web Development**: Streamlit for interface
- **Visualization Tools**: Seaborn
- **Additional Libraries**: faiss-cpu, tiktoken, Ctransformers, huggingface-hub, pypdf, python-dotenv, replicate, docx2txt, lida, lida[transformers], torch, langchain-community

## Demo

![Project Demo](https://path-to-your-image.png)

Watch the [demo video](https://path-to-your-video.mp4) to see the platform in action.

## Live Project

Check out the live project [here](https://interactive-ai.streamlit.app/).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
