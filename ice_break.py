import os
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from third_parties import scrape_linkedin_profile
from agents import lookup
 
from dotenv import load_dotenv

if __name__=='__main__':
    load_dotenv()
    lookup()
    # linkein=scrape_linkedin_profile(linkedin_profile_url='https://www.linkedin.com/in/jamesmanyika/')
#    #  print(linkein)
#     load_dotenv()
#     print("hello")
#     information={'information':"""
# Dennis Keith Rodman (born May 13, 1961) is an American former professional basketball player. Renowned for his fierce defensive and rebounding abilities, his biography on the official NBA website states that he is "arguably the best rebounding forward in NBA history". Nicknamed "the Worm",[2] he played for the Detroit Pistons, San Antonio Spurs, Chicago Bulls, Los Angeles Lakers, and Dallas Mavericks of the National Basketball Association (NBA). Rodman played at the small forward position in his early years before becoming a power forward.
# He earned NBA All-Defensive First Team honors seven times and won the NBA Defensive Player of the Year Award twice. He also led the NBA in rebounds per game for a record seven consecutive years and won five NBA championships. On April 1, 2011, the Pistons retired Rodman's No. 10 jersey,[3] and he was inducted into the Naismith Memorial Basketball Hall of Fame later that year.[4] In October 2021, Rodman was honored as one of the league’s greatest players of all-time by being named to the NBA 75th Anniversary Team.[5]
# Rodman experienced an unhappy childhood and was often described as shy and introverted in his early years. After aborting a suicide attempt in 1993, he reinvented himself as a "bad boy" and became notorious for numerous controversial antics. He repeatedly dyed his hair in artificial colors, had many piercings and tattoos, and regularly disrupted games by clashing with opposing players and officials. He famously wore a wedding dress to promote his 1996 autobiography Bad as I Wanna Be. Rodman pursued a high-profile affair with singer Madonna and was briefly married to actress Carmen Electra. Rodman also attracted international attention for his visits to North Korea and his subsequent befriending of North Korean leader Kim Jong Un in 2013.
# In addition to being a former professional basketball player, Rodman has appeared in professional wrestling. He was a member of the nWo and fought alongside Hulk Hogan in the main event of two Bash at the Beach pay-per-views. In professional wrestling, Rodman was the first-ever winner of the Celebrity Championship Wrestling tournament. He had his own TV show, The Rodman World Tour, and had lead roles in the action films Double Team (1997) and Simon Sez (1999). Both films were critically panned, with the former earning Rodman a triple Razzie Award. He appeared in several reality TV series and was the winner of the $222,000 main prize of the 2004 edition of Celebrity Mole.
# Early life Rodman was born in Trenton, New Jersey, the son of Shirley and Philander Rodman, Jr., an Air Force enlisted member, who later fought in the Vietnam War. When he was young, his father left his family, eventually settling in the Philippines.[6] Rodman has many brothers and sisters: according to his father, he has either 26 or 28 siblings on his father's side. However, Rodman has stated that he is the oldest of a total of 47 children.[6][7][8]
# After his father left, Shirley took many odd jobs to support the family, up to four at the same time.[9] In his 1996 biography Bad As I Wanna Be, he expresses his feelings for his father: "I haven't seen my father in more than 30 years, so what's there to miss ... I just look at it like this: Some man brought me into this world. That doesn't mean I have a father".[6] He would not meet his father again until 2012.[10]
# Rodman and his two sisters, Debra and Kim,[11] grew up in the Oak Cliff section of Dallas,[12] at the time one of the most impoverished areas of the city.[13] Rodman's mother gave him the nickname "The Worm" for how he wiggles while playing pinball.[14] Rodman was so attached to his mother that he refused to move when she sent him to a nursery when he was four years old. According to Rodman, his mother was more interested in his two sisters, who were both considered more talented than he was in basketball and made him a laughingstock whenever he tagged along with them. He felt generally "overwhelmed" by the all-female household.[15] Debra and Kim would go on to become All-Americans at Louisiana Tech and Stephen F. Austin, respectively. Debra won two national titles with the Lady Techsters.[11]
# While attending South Oak Cliff High School, Rodman was a gym class student of future Texas A&M basketball coach Gary Blair.[16] Blair coached Rodman's sisters Debra and Kim, winning three state championships.[17] However, Rodman was not considered an athletic standout. According to Rodman, he was "unable to hit a layup" and was listed in the high school basketball teams but was either benched or cut from the squads. Measuring only 5 ft 6 in (1.68 m) as a freshman in high school,[9] he also failed to make the football teams and was "totally devastated".[15]
# """}
#     summary_template = """
#                         given the Linkedin information {information} about a person from I want yout to create :
#                         1. a short summary
#                         2. two interesting facts about them

#                        """
#     summary_prompt_template= PromptTemplate(input_variables=['information'] , template=summary_template)

#     llm= ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')

#     chain = LLMChain(llm=llm, prompt=summary_prompt_template)
#     # print(chain.run(information=linkein))