import facebook

token = ""

graph = facebook.GraphAPI(token)
# goto here to get ids https://lookup-id.com/
profile = graph.get_object("")
posts = graph.get_connections(profile['id'],"posts")

for post in posts['data']:
	try:
		graph.put_object(post['id'],"likes")
		print "Liking the Post : " +post['message']
	except:
		continue

