from task.app.main import run

# HINT: All available models you can find here: https://ai-proxy.lab.epam.com/openai/models

# TODO:
#  Try different models (`deployment_name`) with such user request:
#  User massage: What LLMs can do?

# Models to try:
# - gpt-4o
# - claude-3-7-sonnet@20250219
# - gemini-2.5-pro


def run_deployment(
    deployment_name: str = "gpt-4o",
    print_request: bool = False,
    print_only_content: bool = False,
):
    run(
        deployment_name=deployment_name,
        print_request=print_request,  # Switch to False if you do not want to see the request in console
        print_only_content=print_only_content,  # Switch to True if you want to see only content from response
    )


# The main goal of this task is to explore the functional capabilities of DIAL to be able to work with different
# LLMs through unified API
if __name__ == "__main__":
    deployment_name = input("Enter the deployment name:\n> ")
    run_deployment(deployment_name)