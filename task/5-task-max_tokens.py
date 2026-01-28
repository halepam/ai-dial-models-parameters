from task.app.main import run

# TODO:
#  Try `max_tokens` parameter. It sets the maximum length of the AI's response. The AI will stop generating text once it hits this limit.
#  User massage: What is token when we are working with LLM?


def run_deployment(deployment_name: str = "gpt-4o"):
    run(
        deployment_name=deployment_name,
        # TODO:
        #  Use `max_tokens` parameter with value 10
        max_tokens=100,
    )


# Previously, we have seen that the `finish_reason` in choice was `stop`, but now it is `length`, and if you check the
# `content,` it is clearly unfinished.

if __name__ == "__main__":
    deployment_name = input("Enter the deployment name:\n> ")
    run_deployment(deployment_name)
