# restserver

docker build -t USERNAME/PROJECTNAME ./

# Deploy

docker run -v /PATH/TO/CODE:/code -ti -p 5000:5000 USERNAME/PROJECTNAME

I do not like put code in docker app, you must write code path here yourself!


# ENVIRONMENT you must set

SECRET_KEY

MONGO_HOST

MONGO_PORT

MONGO_USERNAME

MONGO_PASSWORD

MONGO_DBNAME
