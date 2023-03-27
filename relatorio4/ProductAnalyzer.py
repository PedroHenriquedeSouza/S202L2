from database import Database

class ProductAnalyzer:

    def total_expense_by_customer(db, customerID):
        result = db.collection.aggregate([
            {"$match": {"cliente_id": customerID}},
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
        ])
        return result

    def least_sold_product(db):
        result2 = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.nome", "quantidade": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"quantidade": 1}},
            {"$limit": 1}
        ])
        return result2
    
    def customer_spent_less(db):
        result3 = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"compra": "$_id", "cliente": "$cliente_id"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total": 1}},
            {"$limit":1}
        ])
        return result3

    def products_sold_greater_than_2(db):
        result4 = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.nome", "quantidade": {"$sum": "$produtos.quantidade"}}},
            {"$match": {"quantidade": {"$gt": 2}}}
        ])
        return result4