
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

    def setproductCreate_Y(self,value):
        if value>1960:
                    self.productCreate_Y=value

    def getproductCreate_Y(self):

        return self.productCreate_Y
    def setprice(self,value):
        if value>200000:
            self.Price = value
    def getprice(self):
        return self.Price

    productCreate_Y=property(setproductCreate_Y,getproductCreate_Y)
    price=property(getprice,setprice)
class Nissan(Detail):
    creator=""
    def __init__(self,creator="", model="", productCreate_Y=0, Price=0, Company="" , Engine="", Option="", type=""):
        super().__init__(model, productCreate_Y, Price, Company, Engine,Option,type)
        self.creator = creator

class Lamborgini(Detail):
    def __init__(self, model="", productCreate_Y=0, Price=0, Company="" , Engine="", Option="", type=""):
        super().__init__(model,productCreate_Y,Price,Company,Engine,Option,type)



nis=Nissan(model="maxima",productCreate_Y=1396,Price=2000000,Company="NISSAN",Engine="V-8",Option="P",type="sport")







