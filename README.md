# E-commerce/Auction with Django

This is my implementation of project 2 from [CS50’s Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/2020/), 2020 version.

It's an auction site where users can post auction listings, place bids on listings, comment on those listings, and add listings to a “watchlist.”

<br/>

## Requirements

In this project we should:
- Create three models, one for auction listings, one for bids and one for comments, I also created one for Categories.
- Users should be able to visit a page to create a new listing.
- Show the active listings in the default route.
- Create an individual page to display each listings and all its information
  - If the user is signed in, the user should be able to add the item to their “Watchlist”.
  - If the user is signed in, the user should be able to bid on the item. 
  - If the user is signed in and is the one who created the listing, the user should have the ability to “close” the auction.
  - If a user is signed in on a closed listing page, and the user has won that auction, the page should say so.
  - Users who are signed in should be able to add comments to the listing page. 
- Users who are signed in should be able to visit their Watchlist page.
- Users should be able to visit a page that displays a list of all listing categories.
- Via the Django admin interface, a site administrator should be able to view, add, edit, and delete any listings, comments, and bids made on the site.

You can see all the requirements on [this page](https://cs50.harvard.edu/web/2020/projects/2/commerce/).

<br/>

## How to run

You can clone the repo and type `python manage.py runserver`, you must have Django installed to run a Django application. By now I removed the database from the project, but I'll added some fake data in the future, this way it will be easier to anyone see it working.

<br/>

## Screen shots

<br/>

### Main page and individual page
<p>
<img src="https://user-images.githubusercontent.com/62313672/124426816-f439b480-dd40-11eb-9878-ce11808e011e.gif" width="60%">
</p>

<br/>

### User's listings
<p>
<img src="https://user-images.githubusercontent.com/62313672/124426880-09164800-dd41-11eb-9b70-81cb6965a99d.png" width="60%">
</p>

<br/>

### User's watchlist
<p>
<img src="https://user-images.githubusercontent.com/62313672/124426866-0582c100-dd41-11eb-9b97-690a58a434e8.png" width="60%">
</p>
