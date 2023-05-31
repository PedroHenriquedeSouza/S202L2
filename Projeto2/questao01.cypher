MATCH (u:Usuario{nome:"Bob"})--(a:Usuario) RETURN a.nome AS nome

MATCH (u:Usuario)-[:POSTOU]->(p:Postagem{titulo: 'Memórias da Tarde'}) RETURN u.nome AS nome

MATCH (u:Usuario)-[:POSTOU]->(p:Postagem) WHERE u.idade > 35 RETURN u.nome