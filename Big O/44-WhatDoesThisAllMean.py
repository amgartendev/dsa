"""
Scalable means we worry about large inputs.

So if our function is only worried about really small inputs, or we know that our inputs are only going to be an array
of 5 items, Big O won't matter as much. Because if we look at the graph (BigOChart.png), if the elements are small, all
those lines in the start of the graph will kind of bunched up together, they will be all the same.

But is that real life? No.
As humans, we tend to think in here and now, we tend to think that if our website is only going to have 100 users,
that's it. But what if our user base / input grows?

When we write code, we want to write code that can scale so that we don't have to constantly go back and fix things. Or
when things get out of hand, the code breaks. And that's why Big O is so important. To write scalable code menas
thinking outside of that small little section of the beginning of the graph (where all the lines bunched up). It means
thinking long term, thinking big about your code and what could happen in the future.

With this newfound knowledge, you're going to look at code differently now.
"""
