class Car():    def __init__(self,model= "no data",year= "no data",production= "no data",m_capacity= "no data",color = "no data",price = "no data"):
    self.__model = model        
    self.__year = year 
    self.__production = production        
    self.__m_capacity = m_capacity        
    self.__color = color        
    self.__price = price
    def set_model(self,new_data):        
        self.__model = new_data
    def set_year(self,new_data):        
        self.__year = new_data
    def set_production(self,prod):        
        self.__production = prod
    def set_m_capacity(self,cap):            
        self.__m_capacity = cap
    def set_color(self,color):            
        self.__color = color
    def set_price(self,pr):            
        self.__price = pr
    def get_model(self):        
        return self.__model
    def get_year(self):        
        return self.__year
    def get_production(self):        
        return self.__production
    def get_m_capacity(self):        
        return self.__m_capacity