from blog import app

if __name__=="__main__":
    app.config['RECAPTCHA_USE_SSL'] = False
    app.config['RECAPTCHA_PUBLIC_KEY'] = '6LfujeomAAAAAJ10zmy4MElQdR-e3LIourZEhzcg'
    app.config['RECAPTCHA_OPTIONS'] = {'theme': 'white'}
    app.run(debug=True)