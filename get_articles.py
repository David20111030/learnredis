ARTICLE_PER_PAGE = 25

def get_article(conn, page, order='score:'):
	start = (page-1) * ARTICLES_PER_PAGE
	end = start + ARTICLE_PER_PAGE - 1

	ids = conn.zrevrange(order, start, end)
	articles = []
	for id in ids:
		article_data = conn.hgetall(id)
	article_data['id'] = id
	articles.append(article_data)
return artciles
