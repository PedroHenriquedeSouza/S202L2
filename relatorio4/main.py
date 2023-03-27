from database import Database
from save_json import writeAJson
from ProductAnalyzer import ProductAnalyzer

db = Database(database="loja_de_roupas", collection="vendas")
db.resetDatabase()

result1 = ProductAnalyzer.total_expense_by_customer(db, "B")
writeAJson(result1, "total_gasto")

result2 = ProductAnalyzer.least_sold_product(db)
writeAJson(result2, "produto_menos_vendido")

result3 = ProductAnalyzer.customer_spent_less(db)
writeAJson(result3, "cliente_menos_gastou")

result4 = ProductAnalyzer.products_sold_greater_than_2(db)
writeAJson(result4, "produtos_mais_que_2")