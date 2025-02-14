# AI Agent-Based Projects

## Overview
This repository contains three AI-powered agent-based projects leveraging Autogen, Streamlit, and CrewAI to provide interactive AI experiences. These projects include:

1. **Autogen** - An AI agent framework for coding and theoretical problem-solving.
2. **Autogen UI** - A Streamlit-based UI for user-friendly AI interactions.
3. **CrewAI** - A multi-agent system for collaborative task execution.

## 1. Autogen
### Description
Autogen is a Python-based AI assistant that enables automated problem-solving using Conversable Agents. It supports both theoretical discussions and coding tasks using DeepSeek models.

### Features
- AI-powered code execution using local environments.
- Conversational AI with predefined agents (Teacher, Student, Code Writer, and Executor).
- Dynamic task selection for coding and theoretical tasks.

### Installation
```bash
pip install autogen
```

### Usage
Run the script and select the desired task:
```bash
python autogen.py
```

## 2. Autogen UI
### Description
Autogen UI is a Streamlit-based interface for interacting with AI agents in an intuitive way.

### Features
- User-friendly UI for AI task selection.
- Theoretical and coding task execution with instant responses.
- Streamlit-powered design for easy interaction.

### Installation
```bash
pip install streamlit autogen
```

### Running the UI
```bash
streamlit run autogen_ui.py
```

## 3. CrewAI
### Description
CrewAI is a multi-agent AI system designed for collaboration among specialized agents to execute tasks efficiently.

### Features
- Agents for coding, teaching, and AI research.
- Uses CrewAI framework for structured agent workflows.
- Integrated search and code execution capabilities.

### Installation
```bash
pip install crewai langchain_ollama crewai-tools
```

### Running the System
```bash
python crewai.py
```

## Requirements
- Python 3.8+
- Autogen
- Streamlit
- CrewAI
- LangChain
- Ollama API

## Contributing
Contributions are welcome! Feel free to submit a pull request or raise an issue.