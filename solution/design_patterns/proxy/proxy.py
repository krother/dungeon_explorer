"""
Proxy Pattern

Questions:

- what is a typical usage profile?
- are the same documents retrieved multiple times?
-  is caching results an option?
"""
import random
from pydantic import BaseModel
import time



class Item(BaseModel):
    list_id: int
    position: int
    # add more fields here


class ItemRepository:
    """
    Contains logic for retrieving items
    """
    def __init__(self):
        self.sizes: dict[int, int] = {}

    def get_result_size(self, list_id):
        """retrieves the first page to determine size"""
        print(".. requesting first page to determine size")
        ... # do web stuff here
        size = random.randint(1, 50)  # random size for experimenting
        self.sizes[list_id] = size
        return size

    def request_single_item(self, items: dict[int, Item], list_id, index):
        """requests a single item.. should not be done too often"""
        # if not, request it
        print(f".. requesting item {list_id}:{index}")

        ... # do web stuff here

        # placeholder code
        time.sleep(1)
        items[index] = Item(list_id=list_id, position=index)

    def send_async_requests(self, list_id: int):
        """requests a whole batch"""
        print(".. dammit, we need all the items")
        
        ... # do async web stuff for multiple batches here
        # create multiple requests
        # call event loop
        # wait until everything finishes

        # placeholder code
        for chunk_start in range(0, self.sizes[list_id], 10):
            chunk_end = min(chunk_start + 10, self.sizes[list_id])
            print(f".. retrieving chunk from {chunk_start} to {chunk_end}")
            time.sleep(2)
            chunk = [
                Item(list_id=list_id, position=index)
                for index in range(chunk_start, chunk_end)
            ]
            yield chunk
            
    def get_item(self, items: dict[int, Item], list_id: int, index: int):
        """decides how to retrieve a given document and adds it to items dict"""
        # check if item is already there
        if index in items:
            return
        
        if len(items) <= 3:
            # up to 3 items: send single requests
            self.request_single_item(items, list_id, index)
        else:
            # more items: retrieve everything
            for chunk in self.send_async_requests(list_id):
                for item in chunk:
                    items[item.position] = item        


class ResultList:
    """Lazy-loading list of result items. Implments the Proxy Pattern"""

    def __init__(self, repo: ItemRepository, list_id: int, size: int):
        self.list_id = list_id
        self.size = size
        self.__repo = repo
        self.items = {}  # storage for caching results

    def __getitem__(self, index):
        """makes the class indexable like a list"""
        if index not in self.items:
            self.__repo.get_item(self.items, self.list_id, index)
        return self.items[index]

    def __iter__(self):
        """makes the class iterable like a list"""
        return iter(self[index] for index in range(self.size))
    

def get_result_list(repo: ItemRepository, list_id: int) -> ResultList:
    """toplevel function"""
    size = repo.get_result_size(list_id)
    return ResultList(repo=repo, list_id=list_id, size=size)


repo = ItemRepository()

r1 = get_result_list(repo, 42)
print(r1[3])
print(r1[5])

r2 = get_result_list(repo, 33)
for item in r2:
    print(item)
