from __future__ import annotations
from typing import List
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from utils import llm , _prompt
from pydantic import BaseModel , Field
from kvsecrets import prime_langfuse_env

prime_langfuse_env()

#--------------------------- Input Guardrail-----------------------------#
class _inputguardrailresp (BaseModel):
    code : bool = Field (description = "True if code meets condition and False otherwise")
    condition : str 

def input_guardrail(code:str) -> (bool,str):
    print(code)
    p = _prompt("input_guardrail")
    parser = JsonOutputParser(pydantic_object= _inputguardrailresp)
    chain = (PromptTemplate(
                template = p.prompt,
                input_variables= p.variables, 
                partial_variables= {"format_instructions" : parser.get_format_instructions()},
                template_format= "mustache")
             | _llm(p.config ['model'] , float(p.config ['temperature']))
             | parser
             )
    result : _inputguardrailresp = chain.invoke({"code":code})
    print (result)
    return result['code'], result['condition']

# ──────────────────────── Output guardrail ──────────────────────────
class _OutputGuardrailResp(BaseModel):
    response: bool


def output_guardrail(optimized_code: str, human_feedback_list: List[str]) -> bool:
    p = _prompt("output-guardrail")
    print(optimized_code)
    parser = JsonOutputParser(pydantic_object=_OutputGuardrailResp)

    chain = (
        PromptTemplate(
            template=p.prompt,
            input_variables=p.variables,
            partial_variables={"format_instructions": parser.get_format_instructions()},
            template_format='mustache'
        )
        | _llm(p.config["model"], float(p.config["temperature"]))
        | parser
    )

    return chain.invoke(
        {"optimized_code": optimized_code, "human_feedback_list": human_feedback_list}
    )['response']

