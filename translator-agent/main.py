import dotenv
"""
이 모듈은 .env 파일에서 환경 변수를 로드하기 위해 dotenv 패키지를 사용합니다.
dotenv.load_dotenv() 함수는 프로젝트 루트 디렉토리의 .env 파일을 찾아 환경 변수로 설정합니다.
Jupyter Notebook에서는 .env가 자동으로 로드된다.
"""

dotenv.load_dotenv()

from crewai import Crew, Agent, Task
from crewai.project import CrewBase, agent, task, crew
from tools import count_letters


@CrewBase
class TranslatorCrew:

    @agent
    def translator_agent(self):
        return Agent(
            config=self.agents_config["translator_agent"],  # config/agents.yaml
        )

    @agent
    def counter_agent(self):
        return Agent(
            config=self.agents_config["counter_agent"],
            tools=[count_letters],
        )
    
    @task
    def translate_task(self):
        return Task(
            config=self.tasks_config["translate_task"],  # config/tasks.yaml
        )

    @task
    def retranslate_task(self):
        return Task(
            config=self.tasks_config["retranslate_task"],   # config/tasks.yaml
        )

    @task
    def count_task(self):
        return Task(
            config=self.tasks_config["count_task"],
        )
    
    @crew
    def assemble_crew(self):
        return Crew(
            agents=self.agents,  # TranslatorCrew 클래스의 모든 agent(@agent 데코레이터가 있는 메서드)를 포함합니다.
            tasks=self.tasks,    # TranslatorCrew 클래스의 모든 task(@task 데코레이터가 있는 메서드)를 포함합니다.
            verbose=True,        # 디버그 정보를 출력합니다.
        )


# TranslatorCrew 인스턴스를 생성하고 assemble_crew()로 크루를 구성한 뒤 kickoff()로 작업을 시작합니다.
# kickoff()의 inputs 인자로 번역할 문장을 전달합니다.
TranslatorCrew().assemble_crew().kickoff(
    inputs={
        "sentence": "I'm Nico and I like to ride my bicicle in Napoli",
    }
)