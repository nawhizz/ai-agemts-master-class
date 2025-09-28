# 프로젝트 구조:
translator-agent/
├── README.md
├── main.py
├── tools.py
├── pyproject.toml
└── config/
    ├── agents.yaml
    └── tasks.yaml

# 파일 설명
translator-agent/README.md - 프로젝트 문서
translator-agent/main.py - CrewAI 기반 번역 에이전트 메인 코드
translator-agent/tools.py - 글자 수 세기 도구 함수
translator-agent/pyproject.toml - 프로젝트 설정 및 의존성
translator-agent/config/agents.yaml - 에이전트 설정 (번역가, 카운터)
translator-agent/config/tasks.yaml - 작업 설정 (번역, 재번역, 카운팅)
