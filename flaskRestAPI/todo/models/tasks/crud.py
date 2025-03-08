collection = []
_id = 0

class collection:
    @staticmethod
    def get():
        return collection[:] # return a copy of the list
    
    @staticmethod
    def post(task):
        global _id
        _id += 1
        task['id'] = _id
        collection.append(task)
        return task
    
class item:
    @staticmethod
    def get(id):
        for task in collection:
            if task['id'] == id:
                return task
        return None
    
    @staticmethod
    def delete(id):
        for i, t in enumerate(collection):
            if t['id'] == id:
                del collection[i]
                return True
        return False 
    
    @staticmethod
    def update(id, task):
        for t in enumerate(collection):
            if t['id'] == id:
                t.update(task)
                return t
        return None 
    