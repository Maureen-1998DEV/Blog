from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required
class BlogForm(FlaskForm):

    title = StringField('BLOGmaster title',validators=[Required()])
    text = TextAreaField('write your Blog',validators=[Required()])
    category= SelectField('Blog Category', choices=[('Select a category', 'Select a category'),('Music', 'Music'),('celebrites', 'celebrities'),('movie', 'movie'),('Fashion', 'Fashion'),('Travel', 'Travel'),('Food', 'Food'),('Personal', 'Personal'),('Fitness', 'Fitness'),('sports', 'sports')])
    submit = SubmitField('Blog')


class CommentForm(FlaskForm):

    text = TextAreaField(' Comment blog')
    submit = SubmitField('Comment')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('want to know you more..')
    submit = SubmitField('Submit')