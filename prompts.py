from llama_index.core import PromptTemplate

# Tells agent what do with pandas df and how to respond
instruction_str = """\
    1. Convert the query to executable Python code using Pandas.
    2. The final line of code should be a Python expression that can be called with the `eval()` function.
    3. The code should represent a solution to the query.
    4. PRINT ONLY THE EXPRESSION.
    5. Do not quote the expression."""

# Specify context for agent to know what data it is working with - templating what we want prompt to look like
new_prompt = PromptTemplate(
    """\
    You are working with a pandas dataframe in Python.
    The name of the dataframe is `df`.
    This is the result of `print(df.head())`:
    {df_str}

    Follow these instructions:
    {instruction_str}
    Query: {query_str}

    Expression: """
)

# Context for agent to know what it is working with
context = """Purpose: The primary role of this agent is to assist users who are aiming to be informed on different 
            stocks in the stock market. They want to know the price action of the stock and different metrics. 
            They want to know sentiment about the stock. Do not give clear financial advice, whether or not to buy or sell, 
            to the user about a stock, but give some helpful recommendations about a stock. """
