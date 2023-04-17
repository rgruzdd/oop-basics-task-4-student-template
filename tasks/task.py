class HistoryDict:
    my_dict = {}
    new_list = []
    def __init__(self, my_dict ):
        self.new_dict = my_dict
        self.new_list = []

    def set_value(self, key, value):
        self.my_dict[key] = value
        self.new_list.append(key)
        if len(self.new_list) > 5:
            self.new_list.pop(0)

    def get_history(self):
        return self.new_list





