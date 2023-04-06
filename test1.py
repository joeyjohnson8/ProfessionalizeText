import os
os.environ["OPENAI_API_KEY"] = "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"
os.environ["SERPAPI_API_KEY"] = "62b10e97fbfc30dbed2aa6e094ba833f7c1a6a9be7786dfaeabd1cfae5919f1c"
from platform import python_version
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
llm = OpenAI(temperature=0.9)


from langchain.prompts import PromptTemplate
prompt2 = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)

from langchain.chains import LLMChain
chain = LLMChain(llm=llm, prompt=prompt2)
print(chain.run("colorful socks"))

tools = load_tools(["serpapi", "llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
agent.run("What was the high temperature in SF yesterday in Fahrenheit? What is that number raised to the .023 power?")