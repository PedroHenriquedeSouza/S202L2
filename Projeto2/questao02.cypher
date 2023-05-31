MATCH(u:Usuario) RETURN u.nome AS nome ORDER BY u.idade DESC LIMIT 1

MATCH(u:Usuario) WHERE u.idade > 30 RETURN COUNT(*)

MATCH(u:Usuario) RETURN AVG(u.idade)