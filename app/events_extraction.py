"""
Example : Data Extraction

This example demonstrates how to:
- Navigate to a website with structured data
- Extract specific information from the page
- Process and organize the extracted data
- Return structured results

This builds on previous examples by showing how to get valuable data from websites.
"""

import asyncio
import os
import sys
from dotenv import load_dotenv

load_dotenv()

from browser_use import Agent
from browser_use.llm.openai.chat import ChatOpenAI


async def main():
	# Initialize the model
	llm = ChatOpenAI(model=os.getenv('model','gpt-4o-mini'), \
				    api_key=os.getenv('DEEPSEEK_API_KEY'), \
				    base_url=os.getenv('base_url', 'https://api.deepseek.com/v1') \
					)

	# Define a data extraction task
	task = """
    Go to https://www.austinhindutemple.org/events/list/ and extract a list of upcoming events.:
    For each event, perform the following steps:
	1.	Locate the section or page where upcoming events are listed.
	2.	For each event in the list, click on the event name to open its detailed page.
	3.	On the event detail page, extract the following information:
	    •	Event Name
	    •	Date and Time
	    •	Venue or Address
	    •	City
	    •	State
	    •	Booking Website Link (if available)
	    •	Event Website Link (if available)

    Present the extracted data in a clear and structured format such as JSON appropriate field names for each event.
	[
    {
        "event_name": "Bollywood Night",
        "date_time": "August 10, 2025, 7:00 PM",
        "venue": "Downtown Event Hall",
        "city": "Austin",
        "state": "Texas",
        "booking_link": "https://booktickets.com/bollywood-night",
        "event_website": "https://events.example.com/bollywood-night"
    },
    {
        "event_name": "Yoga Retreat",
        "date_time": "August 15, 2025, 9:00 AM",
        "venue": "Serenity Park",
        "city": "Austin",
        "state": "Texas",
        "booking_link": "https://booktickets.com/yoga-retreat",
        "event_website": "https://events.example.com/yoga-retreat"
    }
    ]
    """

	# Create and run the agent
	agent = Agent(task=task, llm=llm)
	result = await agent.run()
	# Print the structured results
	print(result.extracted_content())


if __name__ == '__main__':
	asyncio.run(main())
