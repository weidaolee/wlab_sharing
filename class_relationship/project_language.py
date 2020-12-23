from multipledispatch import dispatch


class Language:

    def __init__(self, name):
        self.name = name


class Project:

    def __init__(self, name):
        self.name = name
        self.participant_dict = {}

    def add_participant(self, person, language):
        self.participant_dict[person] = language


class Person:

    @dispatch(str)
    def __init__(self, name):
        self.name = name
        self.project = None
        self.language_set = set()

    @dispatch(str, Project, Language)
    def __init__(self, name, project, language):
        self.name = name
        self.set_project(project, language)

    def set_project(self, project, language):
        self.project = project
        project.add_participant(self, language)

    def add_language(self, language):
        self.language_set.add(language)


language = Language("Python")
project = Project("pxr")
person = Person("Weidao", project, language)
