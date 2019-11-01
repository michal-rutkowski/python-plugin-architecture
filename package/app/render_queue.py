# -*- Coding: utf-8 -*-
#!/usr/bin/python
# render_queue.py
"""
    RenderQueue
    ~~~~~~~~~~~~~~~~~~

    Simple processing queue and task classes.

    Based on article "Fundamental concepts of plugin infrastructures"
    by Eli Bendersky (eliben@gmail.com)

    :Author: Michal Adam Rutkowski
    :Created: 2019/10/31
    :Python Version: 3.7
"""


class RenderTask():
    def __init__(self, render_function, input_data):
        self.input = input_data
        self.render_function = render_function

    def run(self):
        return self.render_function(self.input)


class RenderQueue():
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def run(self):
        print("Rendering all tasks in queue..")
        results = []
        for task in self.tasks:
            results.append(task.run())
        print("Finished rendering all tasks!")
        return results
