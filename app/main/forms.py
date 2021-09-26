from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField

class BlogForm(FlaskForm):

    title = StringField('Blog title')
    category= SelectField('Blog Category', choices=[('Select a category', 'Select a category'),('Music', 'Music'),('celebrites', 'celebriries'),('movie', 'movie'),('Fashion', 'Fashion'),('Travel', 'Travel'),('Food', 'Food'),('Personal', 'Personal'),('Fitness', 'Fitness'),('sports', 'sports')])
    content = TextAreaField('The Blog...')
    submit = SubmitField('Post')


class CommentForm(FlaskForm):

    comment = TextAreaField(' Comment blog')
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('want to know you more..')
    submit = SubmitField('Submit')