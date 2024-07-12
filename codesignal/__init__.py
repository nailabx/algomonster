
class Database:
    DATA = {}

    @classmethod
    def get(cls, key):
        if key in cls.DATA:
            return cls.DATA[key]
        return None

    @classmethod
    def delete(cls, key):
        if key in cls.DATA:
            del cls.DATA[key]
            return

    @classmethod
    def operations(cls, queries=None):
        results = []
        if queries is None:
            queries = []
        for query in queries:
            operation = query[0]
            key = query[1]
            subkey = query[2]
            if operation == "get":
                result = cls.get(key,)
                results.append(result)
            elif operation == "delete":
                cls.delete(key, subkey)
                results.append(None)  # Assuming delete operations do not return a value
            elif operation == "set" and len(query) == 4:
                cls.set(key, subkey, query[3])
                results.append(None)  # Assuming set operations do not return a value
        return results

    @classmethod
    def set(cls, key, timestamp, value):
        if key not in cls.DATA:
            cls.DATA[key] = {}
        if timestamp not in cls.DATA[key]:
            cls.DATA[key][timestamp] = {}
        cls.DATA[key][timestamp] = {'value': value, 'timestamp': timestamp}

def solution(queries):
    Database.operations(queries)
    