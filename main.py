import os
from prefect import flow

@flow
def common_flow(config: dict):
    print("I am a subgraph that shows up in lots of places!")
    intermediate_result = 42
    return intermediate_result

@flow(name="My Example Flow", 
      description="An example flow for a tutorial.",
      version=os.getenv("GIT_COMMIT_SHA"))
def main_flow():
    # do some things
    # then call another flow function
    data = common_flow(config={})
    # do more things

main_flow()