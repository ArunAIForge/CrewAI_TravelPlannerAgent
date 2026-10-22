# CrewAI Travel Planner Agent

A lightweight autonomous AI agent built with [CrewAI](https://github.com/crewAIInc/crewAI) that suggests three curated must-visit places for any destination city provided by the user.

---

## Overview

The Travel Planner Agent demonstrates core CrewAI architectural primitives in a clean single-script implementation (`travel_planner.py`):

- **Interactive User Input**: Captures the target city at runtime via standard input.
- **Dedicated Agent Profile**: Configured with a concrete role, goal, and backstory acting as a seasoned travel concierge.
- **Structured Task Definition**: Constrains agent output to exactly three destinations, requiring location highlights and practical visitor tips.
- **Secure Secret Management**: Automatically loads `OPENAI_API_KEY` from a local `.env` file via `python-dotenv` without hardcoding sensitive credentials.

---

## Architecture & Components

| Component | Class | Description |
| :--- | :--- | :--- |
| **Agent** | `Agent` | **Role**: Senior Travel Planner and Destination Guide<br>**Goal**: Curate top 3 recommendations for any city.<br>**Backstory**: Seasoned globetrotter with deep expertise in cultural highlights and local gems. |
| **Task** | `Task` | **Description**: Research and recommend 3 places in the target city.<br>**Expected Output**: Numbered list containing place name, highlight description, and insider tip. |
| **Crew** | `Crew` | Bundles the agent and task into a single execution unit triggered via `crew.kickoff()`. |

---

## Prerequisites

- **Python**: Version 3.10, 3.11, or 3.12 (Python 3.13 is not recommended due to upstream NumPy 1.x binary wheel constraints).
- **OpenAI API Key**: A valid key with access to OpenAI models.

---

## Setup & Installation

### 1. Clone or Navigate to the Project Directory

```powershell
cd E:\SocialEagle\CrewAI\TravelPlannerAgent
```

### 2. Set Up a Virtual Environment

```powershell
# Using Python 3.12 or 3.11
py -3.12 -m venv venv

# Activate on Windows PowerShell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install crewai python-dotenv
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

---

## Usage

Run the travel planner script:

```powershell
python travel_planner.py
```

### Example Interaction

```text
Enter a city to explore: Kyoto

[CrewAI] Initiating travel research for Kyoto...

============================================================
TRAVEL RECOMMENDATIONS FOR KYOTO:
============================================================
1. Fushimi Inari-taisha
   - Highlight: Famous for its thousands of vermilion torii gates winding up Mount Inari.
   - Visitor Tip: Visit at dawn or dusk to avoid crowds and experience the serene forest trail.

2. Kinkaku-ji (Golden Pavilion)
   - Highlight: Zen Buddhist temple whose top two floors are completely covered in gold leaf.
   - Visitor Tip: Morning sunlight offers the best reflection across the surrounding Mirror Pond.

3. Arashiyama Bamboo Grove
   - Highlight: Towering bamboo stalks that create an ethereal soundscape and visual experience.
   - Visitor Tip: Combine your walk with a visit to the nearby Tenryu-ji Temple gardens.
```

---

## Project Structure

```text
TravelPlannerAgent/
│
├── travel_planner.py     # Main application script with Agent, Task, and Crew definition
├── .env                  # Environment file storing OPENAI_API_KEY (git-ignored)
├── .env.example          # Sample environment template
├── .gitignore            # Git ignore file excluding venv and .env
└── README.md             # Project documentation
```
