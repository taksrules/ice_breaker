from langchain.chains import AnalyzeDocumentChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.agents import initialize_agent,Tool,AgentType
from langchain.chains.question_answering import load_qa_chain 
import docx2txt
from tools.tools import get_profile_url


def  lookup(name:str)->str:
    llm= ChatOpenAI(model='gpt-3.5-turbo', temperature=0)
    template ="""given the full name {name_of_person} I want you to get it me a link to their Linkedin profile page
                    Your answer shoould contain only a URL"""
    tools_for_agent= [Tool(name="Crawl Google for linkedin profile page", func="?" , description="useful for when you get the Linkedin Page URL ")]
    
    agent = initialize_agent(tools= tools_for_agent,llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    prompt_template= PromptTemplate(template=template,input_variables=['name_of_person'])
    linkedin_profile_url= agent.run(prompt_template.format_prompt(name_of_person=name))
    # doc_path="C:/Users/tadiw/Downloads/Documents/1909.01792.docx"
    # llm= ChatOpenAI(model='gpt-3.5-turbo', temperature=0)
    # state_of_the_union = docx2txt.process(doc_path)
    # qa_chain= load_qa_chain(llm,chain_type="map_reduce")
    # qa_documents_chain = AnalyzeDocumentChain(combine_docs_chain=qa_chain)
    # print(qa_documents_chain.run(
    #     input_document=state_of_the_union,
    # question="Summarize the paper ? "
    # ))
    return  linkedin_profile_url

