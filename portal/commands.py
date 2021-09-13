
user1 = User.objects.create(username='Babaika', first_name='Mike')
Author.objects.create(authorUser=user1)

user2 = User.objects.create(username='Babaika', first_name='Mike')
Author.objects.create(authorUser=user2)

Category.objects.create(name_cat='Business')
Category.objects.create(name_cat='Movies')
Category.objects.create(name_cat='Cricket')
Category.objects.create(name_cat='Tech')


Post.objects.create(author=Author.objects.get(author_user=User.objects.get(username='Babaika')),
                    category_choice='AR', title='some title', content='some text')
Post.objects.create(author=Author.objects.get(author_user=User.objects.get(username='Babaika')),
                    category_choice='NW', title='some title', content='some text')
Post.objects.create(author=Author.objects.get(author_user=User.objects.get(username='Kroki')),
                    category_choice='AR', title='some title', content='some text')

p1 = Post.objects.get(pk=1)
p2 = Post.objects.get(pk=2)
p3 = Post.objects.get(pk=3)

c1 = Category.objects.get(name_cat='Business')
c2 = Category.objects.get(name_cat='Tech')

p1.post_category.add(c1, c2)

Comment.objects.create(comment_user=User.objects.get(username='Kroki'), comment_posts=Post.objects.get(pk=1), text='comment text1')
Comment.objects.create(comment_user=User.objects.get(username='Babaika'), comment_posts=Post.objects.get(pk=2), text='comment text2')
Comment.objects.create(comment_user=User.objects.get(username='Babaika'),
                       comment_posts=Post.objects.get(pk=3), text='comment text3', rating=1)
Comment.objects.create(comment_user=User.objects.get(username='Kroki'), comment_posts=Post.objects.get(pk=4),
                       text='comment text4', rating=2)

Post.objects.get(pk=3).dislike()
Post.objects.get(pk=2).like()
Post.objects.get(pk=1).like()

Author.objects.get(author_user=User.objects.get(username='Babaika')).update_rating()
Author.objects.get(author_user=User.objects.get(username='Kroki')).update_rating()

a = Author.objects.get(author_user=User.objects.get(username='Babaika')).update_rating()
a.rating_author

best = Author.objects.all().order_by('-rating_author').values('author_user', 'rating_author')[0]
print(best)

