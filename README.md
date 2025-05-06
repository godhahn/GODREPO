# AI Playground: Fun Streamlit WebApps with Groq + LLaMA

## Project Overview

This repository is a collection of interactive and experimental AI web applications built using **Python**, **Streamlit**, and the **Groq API** (powered by **LLaMA models**). The goal is to have fun while building lightweight tools that demonstrate practical and playful uses of large language models (LLMs).

Each app is designed to be engaging, intuitive, and user-friendly—even for users with minimal technical background.

## Apps Overview (in `/pages`)

### 1. Sticky Note AI

An AI-enhanced productivity tool that functions like a digital sticky note wall.

#### Features
- Create and manage tasks with names, descriptions, and priority levels
- AI-generated planning breakdown using Groq + LLaMA
- Checkbox-like task points with strikethrough ability
- Sort tasks by priority
- Edit and update sticky notes
- All tasks are saved in `misc/sticky_note_ai_tasks.json`

#### Use Case
Ideal for planning, prioritizing, and organizing personal or work tasks with smart suggestions.

---

### 2. Vibe Checker AI

A fun app that analyzes the "vibe" of a user-submitted sentence.

#### Features
- Enter any sentence (e.g., "Describe Yi Hahn in one sentence")
- AI classifies it as **Positive** or **Negative**
- Returns a random matching response from a curated CSV dataset
- Background music plays during use

#### Use Case
Great for mood checks, icebreakers, or just having fun with AI interactions.

## Repository Contents

- `/pages`: Contains Streamlit app files
- `/misc`: Contains:
  - `sticky_note_ai_tasks.json`: Sticky Note AI saved tasks
  - `vibe_checker_ai_data.csv`: Response data for Vibe Checker AI
  - `music.mp3`: Background audio for Vibe Checker AI
- `main.py`: Entry point for launching the Streamlit app

## Getting Started

To run in Streamlit Cloud, simply deploy your app on [Streamlit Cloud](https://share.streamlit.io/).

To run the apps locally:

```bash
pip install streamlit groq pandas
streamlit run main.py