from flask import Flask, request  # library to create API
from src.checks.token_check import checkToken  # Import function token validator
from src.functions.password import password_filter
import re

def registerr():  # route function
    token = request.args.get('token')  # GET token argument
    user = request.args.get('user')  # GET user argument
    senha = request.args.get('senha')  # GET senha argument
    csenha = request.args.get('csenha')  # GET csenha argument
    email = request.args.get('email')  # GET email argument
    nmatricula = request.args.get('nmatricula')  # GET matricula argument


    check_token = checkToken(token)  # token validator
    check_password = password_filter(senha, csenha)
    # -------------------------------------------------------------------
    # Check if token validator return False
    if False in check_token.keys():
        return check_token[False]

    elif "False" in check_password:
        return check_password

    # -------------------------------------------------------------------
    return "Conta criada com sucesso!"