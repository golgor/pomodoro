from __future__ import print_function
from typing import TypeVar
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


api_service = TypeVar('api_service')

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/tasks']


class Task():
    """[summary]
    """
    def __init__(self, task: dict, service: api_service) -> None:
        self.kind = task.get('kind')
        self.id = task.get('id')
        self.etag = task.get('etag')
        self.title = task.get('title')
        self.updated = task.get('updated')
        self.selfLink = task.get('selfLink')
        self.parent = task.get('parent')
        self.position = task.get('position')
        self.notes = task.get('notes')
        self.status = task.get('status')
        self.due = task.get('due')
        self.completed = task.get('completed')
        self.deleted = task.get('deleted')
        self.hidden = task.get('hidden')
        self.links = task.get('links')

        self.subtasks = []

    def print_info(self) -> None:
        print(f"{self.title.center(50, '=')}")

    def add_subtask(self, subtask: object) -> None:
        self.subtasks.append(subtask)

    def print_subtasks(self) -> None:
        for subtask in self.subtasks:
            print(subtask.title)


# Class that inherits from Task. Only used to seperate
# between subtasks and tasks. Both have the same kind
# of parameters.
class SubTask(Task):
    pass


class TaskList():
    """[summary]
    """
    def __init__(self, tasklist: dict, service: api_service) -> None:
        self.kind = tasklist.get('kind')
        self.id = tasklist.get('id')
        self.etag = tasklist.get('etag')
        self.title = tasklist.get('title')
        self.updated = tasklist.get('updated')
        self.selfLink = tasklist.get('selfLink')
        self.service = service
        self.tasks = self._create_items()

    def print_info(self) -> None:
        print(f"{self.title.center(50, '=')}")

    def print_tasks(self) -> None:
        for task in self.tasks:
            print(task.title)

    def _create_items(self) -> list:
        """Internal function to create and assign all for the list

        The Tasks API does not distinguish between a task and a subtask
        in any other way than the parameter "parent". I.e. all tasks
        and subtasks are at the same level. This is also taken care of
        here where tasks that have parents, will be added as subtasks
        to that specific task.

        :return: A list with all the tasks in this list.
        :rtype: list
        """
        results = self.service.tasks().list(tasklist=self.id).execute()

        # Add all tasks to the tasklist, but exclude tasks that has
        # parent as these should be added as subtasks instead.
        tasks = [
            Task(item, self.service)
            for item
            in results.get('items')
            if item.get('parent') is None
        ]

        # A list with all tasks that have parents, i.e. they are subtasks.
        subtasks = [
            SubTask(item, self.service)
            for item
            in results.get('items')
            if item.get('parent') is not None
        ]

        # Add subtasks to their specific parent.
        for subtask in subtasks:
            # For every subtask, get the parent id.
            parent = subtask.parent

            # Check all tasks for their id. If the subtasks parent id matches
            # with the tasks id, it is a subtask for that specific task. Then
            # add it as a subtask using the method add_subtask()
            for task in tasks:
                if parent == task.id:
                    task.add_subtask(subtask)

        return tasks


class google_tasks_api:
    """
    """
    def __init__(self):
        self.get_credentials()

    def get_stuff(self):
        # Call the Tasks API
        results = self.service.tasklists().list(maxResults=10).execute()

        # Create a list with taskList objects.
        # Also passing instance of api service, self.service
        tasklists = [
            TaskList(item, self.service)
            for item
            in results.get('items')
        ]

        # Testing printing some stuff...
        tasklists[0].print_info()
        tasklists[0].tasks[3].print_info()
        tasklists[0].tasks[3].subtasks[0].print_info()
        tasklists[0].tasks[3].subtasks[1].print_info()
        tasklists[0].tasks[3].subtasks[2].print_info()
        tasklists[0].tasks[3].subtasks[3].print_info()

    def get_credentials(self):
        """Shows basic usage of the Tasks API.
        Prints the title and ID of the first 10 task lists.
        """
        creds = None
        # The file token.pickle stores the user's access and
        # refresh tokens, and is created automatically when
        # the authorization flow completes for the first time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('tasks', 'v1', credentials=creds)


# For testing purposes only
if __name__ == '__main__':
    tasksApi = google_tasks_api()
    tasksApi.get_stuff()
