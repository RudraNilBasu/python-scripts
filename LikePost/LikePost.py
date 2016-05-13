import facebook

token = "EAACEdEose0cBAMKZAvpyhaUO1T0rF5ohzDpdvqLTrpJZAEQeabtso8sXheP97gcWiUs1UotDZCfPF1ZChcW44LD2WmjsGd0x04o6krdYjl5FIlrGNjvTvEZA6pYriVcXSsMkBZCYnwqBasyYShWHBu9WA9ZC1shWXW6eiZBYQ4zQHQZDZD"

graph = facebook.GraphAPI(token)
# goto here to get ids https://lookup-id.com/
profile = graph.get_object("prizm.r.a.d")
posts = graph.get_connections(profile['id'],"posts")
print posts['data']
for post in posts['data']:
	try:
		graph.put_object(post['id'],"likes")
		print "Liking the Post : " +post['message']
		# commenting
		# graph.put_comment(post['id'],message="Test : auto comment : Success!")
	except:
		continue

