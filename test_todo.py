from todo import TodoList

def test_add_task():
    todo = TodoList()
    todo.add("Comprar leche")
    assert len(todo.tasks) == 1
