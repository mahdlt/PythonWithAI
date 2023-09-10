
import pickle


class FileDict:
    """
    class name: FileDict

    task:receiving keys and values
        writing keys and values if they are in the list below:
        [name, family, age]
        giving values if they are in one of the above keys
        saving the dictionary as .pkl file

    args:
        fine_name:the name of file which has to be saved
        name, family, age: the keys of dict
        dictionary: dict
    """

    dictionary = {}
    file_name = None
    name = None
    family = None
    age = None

    def __init__(self, file_name):
        self.file_name = file_name
    try:
        file = open(file_name + ".pkl","rb")
        dictionary = pickle.load(file)
    except:
        pass



    def __setitem__(self, key0, value):
        if key0 == "name":
            self.name = value
            self.dictionary['name'] = self.name
        if key0 == "family":
            self.family = value
            self.dictionary['family'] = self.family
        if key0 == "age":
             self.age = value
             self.dictionary['age'] = self.age


    def __getitem__(self, key1):
        if key1 == "name":
             return self.name
        if key1 == "family":
            return self.family
        if key1 == "age":
             return self.age
        else:
             return None

    def __str__(self):
        return self.dictionary.__str__()

    def __del__(self):
        file = open(self.file_name + ".pkl", "wb")
        pickle.dump(self.dictionary, file)
        file.close()


'''
    def __getstate__(self):
    return self.__dict__.copy()
  
  def __setstate__(self, state):
    self.__dict__.update(state)

  def __iter__(self):
    for key in self.name:
      yield(key, 'value for {}'.format(key))
  def pic(self):
    #if self.name  in dict.pkl:
    pickle.dump(self.name,open("dict.pkl", "wb"))

  
  def salam(self):
    print("salam %s"%self.name)

  def __str__(self):
    return "%s %s"%(self.name,self.family)


class Point:
  def __init__(self,x=0,y=0):
    self.x=x
    self.y=y


  def __str__(self):
    return "x:%d y:%d"%(self.x,self.y)


'''
