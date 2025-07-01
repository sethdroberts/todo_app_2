from werkzeug.exceptions import NotFound

def error_for_list_title(title, lists):
    if any(lst['title'] == title for lst in lists):
        return "The title must be unique."
    elif not 1 <= len(title) <= 100:
        return "The title must be between 1 and 100 characters"
    else:
        return None
        
def error_for_todo_title(todo_title):
    if not todo_title:
        return "The todo must contain a title"
    elif not 1 <= len(todo_title) <= 100:
        return "The title must be between 1 and 100 characters"
    else:
        return None
        
def find_list_by_id(list_id, lists):
    lst = next((lst for lst in lists if lst['id'] == list_id), None)
    if not lst:
        raise NotFound(description="List not found")
    return lst

def find_todo_by_id(todo_id, todos):
    return next((todo for todo in todos if todo['id'] == todo_id), None)
    
def toggle(todo):
    if todo['completed']:
        todo['completed'] = False
        return "The todo has been marked incomplete!"
    else:
        todo['completed'] = True
        return "The todo has been marked complete!"
        
def todos_remaining(lst):
    return sum(1 for todo in lst['todos'] if not todo['completed'])

def is_list_completed(lst):
    return len(lst['todos']) > 0 and todos_remaining(lst) == 0
    
def is_todo_completed(todo):
    return todo['completed']

def sort_items(items, select_completed):
    sorted_items = sorted(items, key=lambda item: item['title'].lower())

    incomplete_items = [item for item in sorted_items
                        if not select_completed(item)]
    complete_items = [item for item in sorted_items
                      if select_completed(item)]

    return incomplete_items + complete_items