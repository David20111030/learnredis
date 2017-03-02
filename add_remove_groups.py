def add_remove_groups(conn, article_id, to_add=[]):
	article = 'article:' + article_id
	for group in to_add:
		conn.sadd('group:' + group, article)
	for group in to_remove:
		conn.srem('group:' + group, article)
