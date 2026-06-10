# State Statistics to ARV

*A tool that turns official Ukrainian state statistics into ready-to-use sections of a Regulatory Impact Analysis.*

## What is this?

In Ukraine, before a new regulation or law affecting business can be adopted, its authors must prepare a **Regulatory Impact Analysis** — *Аналіз Регуляторного Впливу* (**ARV / АРВ**). Part of that document has to describe, with hard numbers, how many enterprises operate in the affected industry and how that figure has changed over time.

Gathering this data by hand is slow and error-prone: an author has to dig through large spreadsheets published by the State Statistics Service of Ukraine, find the right industry, copy the numbers into a table, and then write a few paragraphs describing the trend.

**This app does that work automatically.** A lawyer or analyst picks an industry and a time period in a simple web form and receives, in seconds, a ready-made Word (`.docx`) document containing an accurate statistical table and a short written description of the trend.

## Who is it for?

- **Lawyers and regulatory specialists** who draft ARV documents for ministries, agencies, or local authorities.
- **Analysts and consultants** who need a quick, reliable snapshot of how many companies operate in a given sector.

No technical knowledge is required — if you can fill in a web form, you can use it.

## How it works

1. **Choose an industry.** Industries are identified by their official **KVED** code (the Ukrainian classifier of economic activities, *Класифікація видів економічної діяльності*). You can search and select one or several codes at once.
2. **Choose a period.** Pick the start and end year. Data is currently available for **2012–2024**.
3. **Generate.** The app builds a Word document containing:
   - A clearly titled **statistics table** — the number of enterprises broken down by company size (small, medium, large) for each year in your range.
   - A short, factual **written description** of the trend (growth, decline, or stability), produced automatically to save you the manual write-up.
   - A **citation** of the official source, so the document is ready to stand up to scrutiny.

The resulting file downloads straight to your computer, ready to be pasted into your full ARV draft.

## Where the data comes from

All figures come directly from the official publication of the **State Statistics Service of Ukraine** — *"Структурні зміни в економіці України та її регіонів: Показники діяльності підприємств (2012–2024)"*. The numbers in every generated table are taken verbatim from this source; the app never invents or estimates figures. This guarantees that your document rests on reliable, citable government data.

## What's in this repository

- **`backend/`** — a Python (FastAPI) service that queries the statistics and assembles the Word document.
- **`docs/`** — the web interface (a single page) that users interact with, hosted via GitHub Pages.
- **`data/`** — the source statistics and the script that loads them into a fast local database.

## Current status

This is an early version (**0.1 / MVP**). It focuses on a single, high-value dataset: **the number of enterprises by size, by industry (KVED), per year.** Additional datasets and document sections may be added over time.

---

*This is a productivity aid for drafting ARV documents. The author of an ARV remains responsible for reviewing the generated content and the final analysis.*
