# Project: State Statistics to ARV (Аналіз Регуляторного Впливу)

## Overview
This project automates the generation of statistical sections for "Analysis of Regulatory Impact" (ARV) documents. Lawyers can select a specific industry (KVED) and period to generate a DOCX document containing reliable statistical tables and LLM-facilitated descriptions.

## Goals
- **Empower Lawyers:** Simplify the data-heavy part of ARV drafting.
- **Data Reliability:** Ensure tables are strictly derived from official state statistics.
- **Facilitated Drafting:** Use LLMs to provide context and descriptions for the data, reducing manual writing time.
- **MVP Focus:** Process "number of companies by size by KVED" data.

## Proposed Architecture
- **Frontend:** A static web interface hosted on **GitHub Pages**. (React or Vanilla JS).
- **Backend:** **Python (FastAPI)** hosted on a **VPS**.
- **Data Management:** Conversion of source Excel data to **SQLite** for efficient querying.
- **Document Generation:** `python-docx` for creating the ARV draft.
- **LLM Integration:** Integration with Gemini/OpenAI API to generate descriptive text based on table data.
- **Reverse Proxy:** **Nginx** on the VPS for handling API requests and SSL.

## Foundational Mandates
- **Data Integrity:** Statistical tables in the DOCX must exactly match the source data.
- **Validation:** Clear error handling for missing KVEDs or invalid periods.
- **Security:** API keys and sensitive configuration must never be committed to GitHub.

## Current Context
- Source data: `active_enterprises - 2026-03-04.xlsx`
- Version Control: GitHub
- Hosting: GitHub Pages (FE), VPS (BE)
