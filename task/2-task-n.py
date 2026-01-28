from task.app.main import run

# TODO:
#  Try the `n` parameter with different models (`deployment_name`). With the parameter `n`, we can configure how many
#       chat completion choices to generate for each input message
#  User massage: Why is the snow white?

# Models to try:
# - gpt-4o
# - claude-3-7-sonnet@20250219
# - gemini-2.5-pro


def run_deployment(deployment_name: str = "gpt-4o", n: int = 2):
    run(deployment_name=deployment_name, n=n)

# Pay attention to the number of choices in the response!
# If you have worked with ChatGPT, you have probably seen responses where ChatGPT offers you a choice between two
# responses to select which one you prefer. This is done with the `n` parameter.

if __name__ == "__main__":
    deployment_name = input("Enter the deployment name:\n> ")
    run_deployment(deployment_name)
