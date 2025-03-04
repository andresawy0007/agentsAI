from app.Agents import EmailAgents
from app.Tasks import EmailTasks
from crewai import Crew

class EmailCrew:
    def __init__(self,email):
        self.email = email
    def run(self):
        # Agents
        classifierAgent = EmailAgents.classifierAgent()
        writerAgent = EmailAgents.emailWriterAgent()
        # Tasks
        classifierTask = EmailTasks.classification(agent=classifierAgent,email=self.email)
        writerTask = EmailTasks.writer(agent=writerAgent,email=self.email)
        # Create crew
        crew = Crew(
            agents=[classifierAgent,writerAgent],
            tasks=[classifierTask,writerTask],
            verbose=True, # Set to True for verbose logging
        )
        # Run the crew
        result = crew.kickoff()
        return result