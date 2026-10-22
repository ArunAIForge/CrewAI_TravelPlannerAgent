"""
CrewAI Travel Planner Agent.

This script prompts the user for a destination city and coordinates
a Travel Planner Agent to recommend 3 standout places to visit.
"""

import os
import sys
from crewai import Agent, Crew, Task
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def main() -> None:
    # Verify OpenAI API key is configured
    if not os.environ.get("OPENAI_API_KEY"):
        print(
            "Error: OPENAI_API_KEY is not set in your environment or .env file.",
            file=sys.stderr,
        )
        print(
            "Please create a .env file with the following line:\n"
            "  OPENAI_API_KEY=your_api_key_here\n",
            file=sys.stderr,
        )
        sys.exit(1)

    # 1. Ask the user for a city
    city = input("Enter a city to explore: ").strip()
    if not city:
        print("Error: City name cannot be empty.", file=sys.stderr)
        sys.exit(1)

    # 2. Create the Travel Planner Agent
    travel_planner = Agent(
        role="Senior Travel Planner and Destination Guide",
        goal=(
            "Provide travelers with insightful, curated recommendations for "
            "the top 3 must-visit places in any specified city."
        ),
        backstory=(
            "You are a seasoned world traveler and professional travel concierge "
            "with over a decade of experience curating bespoke itineraries. "
            "You possess a deep appreciation for culture, architecture, and hidden "
            "gems, and you take pride in helping visitors experience the most "
            "authentic and memorable highlights of every destination."
        ),
        verbose=True,
    )

    # 3. Create the Task
    travel_task = Task(
        description=(
            f"Research and suggest exactly 3 places to visit in {city}. "
            "For each place, provide its name, a detailed explanation of why "
            "it is worth visiting, and a practical tip for travelers."
        ),
        expected_output=(
            "A numbered list of exactly 3 places to visit in the city. Each entry "
            "must include the attraction name, a descriptive highlight of why it is "
            "worth visiting, and one actionable visitor tip."
        ),
        agent=travel_planner,
    )

    # 4. Assemble the Crew
    crew = Crew(
        agents=[travel_planner],
        tasks=[travel_task],
        verbose=True,
    )

    # 5. Execute the Crew and print the result
    print(f"\n[CrewAI] Initiating travel research for {city}...\n")
    result = crew.kickoff()

    print("\n" + "=" * 60)
    print(f"TRAVEL RECOMMENDATIONS FOR {city.upper()}:")
    print("=" * 60)
    print(result)


if __name__ == "__main__":
    main()