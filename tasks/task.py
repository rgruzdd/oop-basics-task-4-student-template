class HistoryDict:
    my_dict = {}
    new_list = []
    def __init__(self, my_dict):
        self.new_dict = my_dict

    def set_value(self, key, value):
        self.my_dict[key] = value
        self.new_list.append(key)
        return

    def get_history(self):
        self.new_list.reverse()
        while len(self.new_list) > 5:
            self.new_list.pop()
        self.new_list.reverse()
        return self.new_list




