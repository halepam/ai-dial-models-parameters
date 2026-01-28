from task.app.main import run

# TODO:
#  Try `frequency_penalty` parameter.
#  Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's
#  likelihood to repeat the same line verbatim. Higher values == less repetitive text.
#       Range: -2.0 to 2.0
#       Default: 0.0
#  User massage: Explain the water cycle in simple terms for children


def run_deployment(deployment_name: str = "gpt-4o"):
    run(
        deployment_name=deployment_name,
        frequency_penalty=-2.0,
        print_request = False,
        print_only_content = False,
        # TODO:
        #  Use `frequency_penalty` parameter with different range (-2.0 to 2.0).
    )


# Pay attention that when we set for `gpt-4o` frequency_penalty as -2.0 - the request is running too long,
# and in the result we can get something strange (such as repetitive words in the end).
# Copy the results and then check with separate request and ask LLM where is more repetitive blocks in texts.
# For Anthropic and Gemini this parameter will be ignored

if __name__ == "__main__":
    # deployment_name = input("Enter the deployment name:\n> ")
    run_deployment()
