from flask_wtf import FlaskForm, Form
from wtforms import SelectField, SubmitField, StringField
from wtforms.validators import DataRequired


class Estacionamento(FlaskForm):
    # cidades = open("app\process\cidades.txt", 'r').readlines()
    # choices = []
    # for i in cidades:
    #     city = (i.rstrip('\n'),i)
    #     choices.append(city)
    
    # cidade = SelectField(u'cidade', choices=choices)
    submit = SubmitField('Sign In')

class EscolhaCep(FlaskForm):
    cep = StringField(u'cep')
    submit = SubmitField('Pesquisar')