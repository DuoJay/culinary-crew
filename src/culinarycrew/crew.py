from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from dotenv import load_dotenv

load_dotenv()


@CrewBase
class Culinarycrew():
    """Culinarycrew crew"""

    # Define paths to the configuration files for the agents and tasks
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # Define agents based on the configuration
    @agent
    def chef_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['chef_agent']
        )

    @agent
    def music_aficionado(self) -> Agent:
        return Agent(
            config=self.agents_config['music_aficionado']
        )

    @agent
    def recipe_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['recipe_agent']
        )

    # Define tasks based on the configuration
    @task
    def ingredient_enrichment_task(self) -> Task:
        return Task(
            config=self.tasks_config['ingredient_enrichment_task'],
        )

    @task
    def recipe_instruction_task(self) -> Task:
        return Task(
            config=self.tasks_config['recipe_instruction_task'],
        )

    @task
    def music_and_culture_recommendation_task(self) -> Task:
        return Task(
            config=self.tasks_config['music_and_culture_recommendation_task'],
        )

    # Define the crew, which binds the agents and tasks together
    @crew
    def crew(self) -> Crew:
        """Creates the Culinarycrew crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,  # Define the task processing order (sequential or hierarchical)
            verbose=True,  # Enable verbose output for debugging
        )
