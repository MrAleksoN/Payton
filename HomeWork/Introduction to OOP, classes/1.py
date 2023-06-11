class auto():
    def add(self, model, year, engine, color, price):
        self.model = model
        self.year = year
        self.engine = engine
        self.color = color
        self.price = price
    def print_(self):
        print(f'BMW {self.model} {self.year} 2022г,с объемом двигателя 2,5 {self.engine},{self.color},{self.price} ')
    def change_model(self, new_model):
        self.model = new_model
    def change_year(self, new_year):
        self.year = new_year
    def change_engine(self, new_engine):
        self.engine = new_engine
    def change_color(self, new_color):
        self.color = new_color
    def change_price(self, new_price):
        self.price = new_price