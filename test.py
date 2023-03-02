import unittest
from tasks import Tasks

def create_task(tasks,days):
    task = Tasks()
    task.create_task(tasks,days.capitalize())

# def fetch_all_task():
#     tasks = Tasks()
#     task = tasks.get_tasks()
#     return task

class TestTasks(unittest.TestCase):
    
    def test_saveTask(self):
        self.assertEqual(create_task("Test task1","Monday"),True)
        self.assertEqual(create_task("Test task2","Tuesday"),True)
        self.assertEqual(create_task("Test task3","Wednesday"),True)
        self.assertEqual(create_task("Test task4","Thursday"),True)
        self.assertEqual(create_task("Test task5","Weekly"),True)
        
    # def test_getTasks(self):
    #     self.assertIsInstance(fetch_all_task())
        
        
if __name__ == "__main__":
    test = TestTasks()
    unittest.main()