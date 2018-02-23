# Collaborative Filtering

One of popular recommenation category is **`Collaborative Filtering`** which instead of imply user taste from other information, we can use other user/item ratings to predict how user love the item.

In reality, it's very hard to gather user personal attributes and it makes user feel threaten too much when very personal detail is used. So instead of asking personal question, we can instead use thier opinion toward the things or thier behaviour to imply thier taste. One quote I love from `Practical Recommender Systems` book to explain about collaborative filtering and people is:

```
Most people consider themselves unique and, therefore, don't like to be segmented into a particular type. But, that is exactly what using collaborative filtering to calculate recommendations is all about. In all its simplicity, collaborative filtering is recommending a list of items for you. The list being created based on people who like the same thing as you, but who also like something that you haven’t consumed yet.
```

## Data Source Analysis - Implicit Rating
The behaviour data can be both explicit one that use tell us how s/he like a products or implicit one that imply from they real behaviour such as viewing, buying, repeating-buying, etc. depend on recommendation purpose and availiblity of data.

I implied the rating from behaviour of people in twitter because I had very limited resource and this is just personal dirty-quick study of recommendation system.

**This is meaning of my rating matrix** 
1 = Follow one or more member fanpage in twitter
0 = Not-Follow any fanpage
