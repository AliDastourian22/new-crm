
class Detail():
    model = ""
    productCreate_Y = 0
    Price = 0
    Company = ""
    Engine =""
    Option=""
    type=""
    def __init__(self, model="", productCreate_Y=0, Price=0, Company="" , Engine="", Option="", type=""):
        self.model = model
        self.productCreate_Y = productCreate_Y
        self.Price = Price
        self.Company = Company
        self.Engine = Engine
        self.Option = Option
        self.type = type
        
class Nissan(Detail):
    def __init__(self, model="", productCreate_Y=0, Price=0, Company="" , Engine="", Option="", type=""):
        super().__init__(model, productCreate_Y, Price, Company, Engine,Option,type)


class Lamborgini(Detail):
    def __init__(self, model="", productCreate_Y=0, Price=0, Company="" , Engine="", Option="", type=""):
        super().__init__(model,productCreate_Y,Price,Company,Engine,Option,type)




nis=Nissan(model="maxima",productCreate_Y=1396,Price=20000,Company="NISSAN",Engine="V-8",Option="P",type="sport")







