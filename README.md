# LMNOP

LMNOP (LLM-based Microbial Metadata Notebook Processing) is a tool presented in the form of a jupyter notebook that allows users to easily clean and summarize metadata fields with support for attributes commonly relevant to microbiome studies, such as summary statistics and visualizations. Users can directly query an LLM within a jupyter notebook in ways that automatically provide context to queries based on the loaded metadata file. With automated improved prompt engineering, obtaining and running code suggestions from ChatGPT. The notebook also provides functions for anomaly detection and column name correcting are presented. Voice recognition is also supported through OpenAI's extremely accurate whisper voice transcription library.


## Installation

To use this notebook, clone the repository and create a new conda environment.
An environment file will set the name of your env to `lmnop`:

```bash
git clone https://github.com/dpear/LMNOP.git
cd LMNOP
conda env create -f environment.yml
```

If you wish to use within an existing conda environment:
```bash
conda env update --name existing_env_name --file environment.yml
```

Then, activate the environment to add a jupyter notebook kernel:
```bash
conda activate lmnop
python -m ipykernel install --user --name lmnop --display-name "Python (lmnop jupyter kernel)"
```

## Using the Notebook

First activate the environment, then actiate the jupyter notebook server (please note that you must activate the environment before starting the jupyter notebook server):
```bash
conda activate lmnop
jupyter notebook
```
Then navigate to the `proof_of_concept_template_ai_memorializing_DP.ipynb` notebook and run to see an example of the different supported summarization and cleaning functions.

## Cells that make a call to the LLM automatically disable themselves
Cells that make a call to the LLM will automatically disable themselves by switching from `code` cell type to `raw` cell type. This is because each call to the LLM may produce different results based on a probabilistic response generating scheme, which is re-trained each time a call is made (imagine asking ChatGPT the same question twice in a row, you would expect to get two similar but different results). Normal jupyter notebook behavior–code behavior in general–maintains that running the same code or cells from top to bottom produces the same result, which would not be the case for calls to the LLM. Unlike `np.random` or similar libraries that rely on stochasticity, there is no way of setting a seed when making calls to the LLM. Thus we will save both the call and the response to the LLM but disable the cells, which is especially helpful so that **an informative response from the LLM does not get deleted.**

## Re-Enabling cells that make a call to an LLM
Cells need only be switched back from `raw` cell type to `code` cell type. More information can be found at the following resources:

https://jupyter-notebook.readthedocs.io/en/stable/notebook.html
https://www.geeksforgeeks.org/markdown-cell-in-jupyter-notebook/
https://discourse.jupyter.org/c/notebook/31


## How to Obtain an API Key from OpenAI

To use OpenAI's API with this project, you will need an API key.
Navigate to OpenAI's Developer Quickstart page for instructions on how to create and export an API key:
https://platform.openai.com/docs/quickstart

#### Troubleshooting:
- If you encounter problems with your API key, it may require setting up an account that has a paid subscription plan. 
- Please see the [OpenAI website](https://platform.openai.com/) for more details.
