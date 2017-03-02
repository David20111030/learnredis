def get_group_articles(conn, group, page, order='score:'):
	key = order + group
	if not conn.exists(key):
		conn.zinterstore(key,
			['group:' + group, order],
			aggregate='max',
		)
		conn.expire(key,60)
	return get_articles(conn, page, key)
