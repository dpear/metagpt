# OpenAI Jupyter Notebook Wrapper

A simple and intuitive wrapper that allows users to easily interact with the OpenAI API directly within Jupyter Notebooks. This wrapper simplifies the process of querying the OpenAI models and makes it more accessible for researchers, developers, and data scientists working in a notebook environment.

## Key Features

- 🤝 **Seamless Integration**: Designed specifically for Jupyter Notebooks, ensuring a smooth user experience.
- 🗣 **Simplified API Calls**: Reduces boilerplate code, making it easier to query OpenAI models.
- 💥 **Customizable**: Provides flexibility to fine-tune parameters for your specific needs.
- 🚨 **Error Handling**: Built-in error handling for common OpenAI API issues.

## Requirements

This package requires the following dependencies:

- `pandas` - For data handling and manipulation.
- `numpy` - For numerical operations.
- `openai` - Official OpenAI Python client.

## Installation

To use this wrapper, clone the repository and install it directly from GitHub:

```bash
pip install git+https://github.com/dpear/metagpt.git
```

## Example Code Snippet

Here's an example of how to use `metagpt`:

```python
from metagpt import ask
from openai import OpenAI

OPEN_AI_KEY='sk-proj-gGRfNmVPcDq7jpyegFcNIjKsJQ_AZr1P6hQH7bu-...'
c = OpenAI(api_key=OPEN_AI_KEY)
ask('what is a bagel', client=c)
```
## Multilingual Voice Recognition
![here](examples/multilingual-voice.png)

## How to Obtain an API Key from OpenAI

To use OpenAI's API with this project, you will need an API key. Follow these steps to obtain your key:

#### Step 1: Sign Up or Log In
1. Go to the [OpenAI website](https://platform.openai.com/).
2. Click **Sign Up** to create an account or **Log In** if you already have one.

#### Step 2: Access the API Key Page
1. After logging in, navigate to the [API Keys page](https://platform.openai.com/account/api-keys).
2. This is where you can manage your API keys.

#### Step 3: Generate a New API Key
1. Click the **+ Create new secret key** button.
2. A new API key will be displayed. **Copy it immediately**, as it will not be shown again.
   - If you lose it, you’ll need to create a new key.

#### Step 4: Secure Your API Key
- **Do not share your API key publicly.**
- Use environment variables or a configuration file to manage your key securely.

#### Troubleshooting:
- If you encounter problems with your API key, it may require setting up an account that has a paid subscription plan. 
- Please see the [OpenAI website](https://platform.openai.com/) for more details.
