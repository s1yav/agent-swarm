from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model="gemini-2.5-flash",
    name="director_agent",
    description="A helpful assistant for user questions.",
    instruction="Answer user questions to the best of your knowledge",
)


# import asyncio
# from google.adk.agents.llm_agent import Agent
# from google.adk.runners import Runner
# from google.adk.sessions import InMemorySessionService
# from google.genai.types import Content, Part
#
# # Define root agent for ADK CLI & programmatic usage
# # root_agent = Agent(
# #     model='gemini-2.5-flash',
# #     name='director',
# #     instruction="""You are a patient math tutor.
# # Guide students through problems step-by-step.
# # Don't just give answers - help them discover solutions."""
# # )


# # Set up session and runner for programmatic execution
# APP_NAME = "director"
# USER_ID = "student_1"
# SESSION_ID = "session_001"
#
# session_service = InMemorySessionService()
# runner = Runner(
#     agent=root_agent,
#     app_name=APP_NAME,
#     session_service=session_service
# )
#
#
# async def run_agent():
#     # Create session
#     session = await session_service.create_session(
#         app_name=APP_NAME,
#         user_id=USER_ID,
#         session_id=SESSION_ID
#     )
#     print(f"Session created: {SESSION_ID}\n")
#
#     # Prepare user message
#     user_message = Content(
#         role="user",
#         parts=[Part(text="How do I solve 2x + 5 = 13?")]
#     )
#
#     # Run agent and collect response
#     print("User: How do I solve 2x + 5 = 13?\n")
#     print("Agent: ", end="")
#     async for event in runner.run_async(
#         user_id=USER_ID,
#         session_id=SESSION_ID,
#         new_message=user_message
#     ):
#         # Print final response
#         if event.is_final_response() and event.content and event.content.parts:
#             print(event.content.parts[0].text)
#
#
# if __name__ == "__main__":
#     asyncio.run(run_agent())
