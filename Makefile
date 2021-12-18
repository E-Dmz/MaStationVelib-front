APP_NAME = ma-station-velib

streamlit:
	@streamlit run app.py

heroku_login:
	-@heroku login

heroku_create_app:
	-@heroku create ${APP_NAME}

deploy_heroku:
	-@git push heroku main
	-@heroku ps:scale web=1
