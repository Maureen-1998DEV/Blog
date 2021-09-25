from flask import Flask
from . import main
import datetime
from flask import render_template, request, redirect, url_for, abort, flash
from flask_login import login_required
from ..models import User, Blog, Comment
from .forms import UpdateProfile, blogForm , CommentForm
from .. import db, photos
app = Flask(__name__)


# views
@main.route("/")
def index():
   '''
   the mainpage
   '''
   title = 'Blog master'
   blogs = Blog.query.all()

   return render_template('index.html', title= title, blogs = blogs)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
    
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/post/new', methods=['GET','POST'])
@login_required
def new_blog():
    form = blogForm()

    if form.validate_on_submit():

        title=form.title.data
        content=form.content.data
        category=form.category.data
        blog = Blog(title=title, content=content,category=category)
        # post.save_blog(blog)
        db.session.add(blog)
        db.session.commit()

        flash('Your post has been created!', 'success')
        return redirect(url_for('main.index', id=blog.id))

    return render_template('new_post.html', title='New Post', post_form=form, post ='New Post')


@main.route('/comment/new/<int:id>', methods=['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()

    if form.validate_on_submit():
        
        comment_content = form.comment.data

        comment = Comment(comment_content= comment_content, post_id=id)

        # post.save_blog(blog)
        db.session.add(comment)
        db.session.commit()
        
    comment = Comment.query.filter_by(post_id=id).all()
    return render_template('new_comment.html', title='New Post', comment=comment,comment_form=form, post ='New Post')

@main.route('/music/new', methods=['GET','POST'])
@login_required
def music(category = "Music"):

    music = Blog.query.filter_by(category = "Music")
    
    title = "Music Blogs"
    return render_template('music.html', music= music, title=title, post ='New Post')


@main.route('/movies/new', methods=['GET','POST'])
@login_required
def movie(category = "movies"):

    movie = Blog.query.filter_by(category = "movies")
    
    title = "latest Movie Blogs"
    return render_template('movie.html', movie=movie, title=title, post ='New Post')


@main.route('/celebrities/new', methods=['GET','POST'])
@login_required
def celebrities(category = "celebrities"):

    celebrities = Blog.query.filter_by(category = "celebrities")
    
    title = "celebrities Blogs"
    return render_template('celebrities.html', celebrities = celebrities, title=title, post ='New Post')


@main.route('/fashion/new', methods=['GET','POST'])
@login_required
def fashion(category = "fashion"):

    fashion = Blog.query.filter_by(category = "fashion")
    
    title = "Fashion Blogs"
    return render_template('fashion.html', fashion= fashion, title=title, post ='New Post')


@main.route('/travel/new', methods=['GET','POST'])
@login_required
def travel(category = "travel"):

    natures = Blog.query.filter_by(category = "travel")
    
    title = "Travel Blogs"
    return render_template('travel.html', natures= natures, title=title, post ='New Post')

@main.route('/food/new', methods=['GET','POST'])
@login_required
def food(category = "Food"):

    food = Blog.query.filter_by(category = "food")
    
    title = "Food Blogs"
    
    return render_template('food.html', food= food, title=title, post ='New Post')

@main.route('/personal/new', methods=['GET','POST'])
@login_required
def personal(category = "personal"):

    personal = Blog.query.filter_by(category = "personal")
    
    title = "Personal Blogs"
        
    return render_template('personal.html', personal= personal, title=title, post ='New Post')



@main.route('/fitness/new', methods=['GET','POST'])
@login_required
def fitness(category = "Fitness"):

    fitness = Blog.query.filter_by(category = "Fitness")
    
    title = "Fitness Blogs"
    
    return render_template('fitness.html', fitness= fitness, title=title, post ='New Post')



@main.route('/sports/new', methods=['GET','POST'])
@login_required
def Sports(category = "sports"):

    sports = Blog.query.filter_by(category = "sports")
    
    title = "Sports Blog"
    
    return render_template('sports.html', sports= sports, title=title, post ='New Post')

@main.route('/delete/<int:id>',methods=['GET','POST'])
@login_required
def delete(id):
   del_blog = Blog.query.filter_by(id=id).first()
   db.session.delete(del_blog)
   db.session.commit()
   
   return redirect(url_for('main.index'))
