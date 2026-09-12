# Generative AI Masterclass (Part 1): LangChain, LLMs & Prompt Engineering

An end-to-end hands-on repository covering LLM fundamentals, prompt engineering frameworks, LangChain Expression Language (LCEL), and structured output parsing. Based on the foundational curriculum from Sheryians AI School.

---

## 📌 Overview

This repository contains modular code implementations, Jupyter notebooks, and utility pipelines designed to bridge the gap between raw API calls and production-ready LLM application engineering. 

### Key Highlights
* **Foundations First**: Understand tokenization, vector embeddings, high-dimensional similarity spaces, and autoregressive generation mechanics.
* **Provider Agnostic**: Implement workflows across proprietary providers (OpenAI, Google Gemini, Anthropic) and open-weights models (Meta LLaMA, Mistral, DeepSeek via Hugging Face).
* **LangChain & LCEL**: Build modular, reusable chains decoupling prompt preparation, inference, and response transformation.
* **Production Parsers**: Enforce deterministic, structured schema extraction (Pydantic, JSON) from inherently non-deterministic LLMs.

---

## 🗂️ Repository Structure

```text
├── 01_foundations/
│   ├── embeddings_demo.py        # Tokenization & vector embedding visualizations
│   └── model_providers.py        # Setting up OpenAI, Gemini, HuggingFace APIs
├── 02_prompt_engineering/
│   ├── zero_few_shot.py          # Zero-shot vs Few-shot in-context learning
│   └── chain_of_thought.py       # CoT reasoning prompts for deterministic logic
├── 03_langchain_core/
│   ├── prompt_templates.py       # Dynamic ChatPromptTemplates & System Messages
│   ├── simple_lcel_chains.py     # Pipe syntax (`prompt | model | parser`)
│   └── memory_management.py      # Conversation history tracking
├── 04_structured_outputs/
│   ├── json_parsers.py           # Extracting clean JSON objects from text
│   └── pydantic_validation.py    # Schema validation with PydanticOutputParser
├── requirements.txt
├── .env.example
└── README.md
