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
    """
    Single processing task (decoding, encoding etc)
    Takes a render function provided by plugins and input data.
    """
    def __init__(self, render_function, input_data):
        self.input = input_data
        self.render_function = render_function

    def run(self):
        """
        Execute task
        """
        return self.render_function(self.input)


class RenderQueue():
    """
    Simple render queue for batch processing
    """
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """
        Adds RenderTask to this queue
        """
        assert isinstance(task, RenderTask), "RenderQueue.add_task only accepts RenderTasks"
        self.tasks.append(task)

    def run(self):
        """
        Renders all tasks in queue storing result data and returning as list
        """
        results = []
        for task in self.tasks:
            results.append(task.run())
        self.tasks = []
        return results
