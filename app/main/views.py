from flask import render_template,request,redirect,url_for,abort
from .import main
from ..models import Blog,User,Comment
from .forms import UpdateProfile,BlogForm,CommentForm
from .. import db,photos
from flask_login import login_required,current_user
import datetime



# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home-BLOGmaster'
    #review by category
    blogs_fashion = Blog.get_blogs('fashion')
    blogs_food = Blog.get_blogs('food')
    blogs_travel = Blog.get_blogs('travel')
    blogs_music = Blog.get_blogs('music')
    blogs_movie = Blog.get_blogs('movie')
    blogs_personal = Blog.get_blogs('personal')
    blogs_sports = Blog.get_blogs('sports')  
    blogs_celebrity = Blog.get_blogs('celebrity')
    blogs_fitness = Blog.get_blogs('fitness')
    
    
    return render_template('index.html',title = title, fashion =blogs_fashion , food = blogs_food, travel = blogs_travel,music = blogs_music, movie = blogs_movie,personal = blogs_personal, sports= blogs_sports,celebrities =  blogs_celebrity,fitness = blogs_fitness)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    count_blogs =Blog.blogs_count(uname)
    user_joined = user.date_joined.strftime('%b %d, %Y')
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,blogs =count_blogs,date = user_joined)


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

    return render_template('profile/update.html',form = form)



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

@main.route('/blog/new', methods = ['GET','POST'])
@login_required
def new_blog():
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        title = blog_form.title.data
        blog = blog_form.text.data
        category = blog_form.category.data

        # Updated blog 
        new_blog = Blog(title_blog=title,content_blog=blog,category=category,user=current_user,likes=0,dislikes=0)

        # Save blog 
        new_blog.save_blog()
        return redirect(url_for('.index'))

    title = 'New Blog'
    return render_template('newpitch.html',title = title,blog_form=blog_form )


@main.route('/blogs/blogs_fashion')
def blog_fashion():

    blogs = Blog.get_blogs('fashion')

    return render_template("fashion.html", blogs = blogs)


@main.route('/blogs/blogs_food')
def blogs_food():

    blogs = Blog.get_blogs('food')

    return render_template("product.html", blogs = blogs)

@main.route('/blogs/blogs_travel')
def blogs_travel():

    blogs = Blog.get_blogs('travel')

    return render_template("travel.html", blogs = blogs)


@main.route('/blogs/blogs_music')
def blogs_music():

    blogs = Blog.get_blogs('music')

    return render_template("music.html", blogs = blogs)


@main.route('/blogs/blogs_movie')
def blogs_movie():

    blogs = Blog.get_blogs('movie')

    return render_template("movie.html", blogs = blogs)

@main.route('/blogs/blogs_personal')
def blogs_personal():

    blogs = Blog.get_blogs('personal')

    return render_template("personal.html", blogs = blogs)
@main.route('/blogs/blogs_sports')
def blogs_sports():

    blogs = Blog.get_blogs('sports')

    return render_template("sports.html", blogs = blogs)


@main.route('/blogs/blogs_celebrity')
def blogs_celebrity():

    blogs = Blog.get_blogs('celebrity')

    return render_template("celebrities.html", blogs = blogs)

@main.route('/blogs/blogs_fitness')
def blogs_fitness():

    blogs = Blog.get_blogs('fitness')

    return render_template("fitness.html", blogs = blogs)


@main.route('/blog/<int:id>', methods = ['GET','POST'])
def blog(id):
    blogs = Blog.get_blogs(id)
    posted_date = blog.posted.strftime('%b %d, %Y')

    if request.args.get("like"):
        blog.likes = blog.likes + 1

        db.session.add(blog)
        db.session.commit()

        return redirect("/blog/{blog_id}".format(blog_id=blog.id))

    elif request.args.get("dislike"):
        blog.dislikes = blog.dislikes + 1

        db.session.add(blog)
        db.session.commit()

        return redirect("/blog/{blog_id}".format(blog_id=blog.id))

    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment= comment_form.text.data

        new_comment = Comment(content_commit = comment,user = current_user,blog_id = blog)

        new_comment.save_comment()


    comments = Comment.get_comment(blog)

    return render_template("blog.html", blog = blog, comment_form = comment_form, comments = comments, date = posted_date)

@main.route('/user/<uname>/pitches')
def user_blogs(uname):
    user = User.query.filter_by(username=uname).first()
    blogs = Blog.query.filter_by(user_id = user.id).all()
    blogs_count = Blog.count_blogs(uname)
    user_joined = user.date_joined.strftime('%b %d, %Y')

    return render_template("profile/blog.html", user=user,blogs = blogs,blogs_count=blogs_count,date = user_joined)
