# AutoStream – Social-to-Lead Agentic Workflow

## Overview
This project implements a stateful conversational AI agent for a fictional SaaS product called **AutoStream**, which provides automated video editing tools for content creators.

The agent is designed to:
- Understand user intent
- Answer pricing and product questions using RAG
- Detect high-intent users
- Collect lead details across multiple conversation turns
- Safely trigger backend actions for lead capture

This assignment demonstrates a **real-world agentic workflow**, not just a chatbot.

---

## Tech Stack
- Python 3.9+
- LangChain
- LangGraph (state management)
- GPT-4o-mini (LLM, pluggable)

---

## Agent Capabilities
- Intent classification (greeting, pricing, high-intent)
- RAG-powered knowledge retrieval using a local JSON knowledge base
- Multi-turn conversation state management (5–6 turns)
- Safe tool execution for lead capture
- Production-ready conversational flow

---

## Knowledge Base (RAG)
Pricing and policy information is stored locally in:
