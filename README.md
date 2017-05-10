# restserver

docker build -t USERNAME/PROJECTNAME ./

# Deploy

docker run -v /PATH/TO/CODE:/code -ti -p 5000:5000 USERNAME/PROJECTNAME

I do not like put code in docker app, you must write code path here yourself!


# ENVIRONMENT you must set

MONGO_HOST

MONGO_PORT

MONGO_USERNAME

MONGO_PASSWORD

MONGO_DBNAME

# ENVIRONMENT you can choose to fill

SECRET_KEY

VIRTUAL_HOST

# HOW TO USE

* clone this source code
* docker build -t USERNAME/PROJECTNAME ./
* copy src code to dir that you point /PATH/TO/CODE, attention your container must have the privalige to src code
* set your environment with mongoDB infomation
* docker run -v /PATH/TO/CODE:/code -ti -p 5000:5000 USERNAME/PROJECTNAME
* visit your brower at http://VIRTUAL_HOST/v1/ it will alert an auth dialog.

# links

*  'accounts': accounts POST GET PATCH

    manage your user infomation.
    
    you must provide your token in  Headers -> Authorization  to get accounts be accessible except GET method.
    
*  'devices': devices    POST GET DELETE PATCH 

    manage your device infomation.
    
    you must provide your token in  Headers -> Authorization  to get accounts be accessible.
    
*  'gettoken': gettoken  GET 

    you must provide your username and password registered at accounts item point, in Headers -> Authorization.
    
# example

```javascript
var device_url = 'http://SERVER-URL/v1/devices/'
var login_url = 'http://SERVER-URL/v1/gettoken/';

mui.ajax(device_url + '?where={"username":"' + username + '"}', {
	headers: {
		'Content-Type': 'application/json',
		"authorization": token,
	},
	data: deviceInfo,
	dataType: 'json',
	type: 'post',
	async: false,
	timeout: 1000,
	success: function(data) {
		mui.toast("add device success！")
	},
	error: function(xhr, textStatus, errorThrown) {
		mui.toast("add device failed, please check it!");
		console.log("xhr code:" + xhr.status);
	}
});

function login(username, passwd) {
	var authed = false;
	mui.ajax(login_url + username, {
		headers: {
			'Content-Type': 'application/json',
			"authorization": "Basic " + btoa(username + ":" + passwd),
			"cache-control": "no-cache"
		},
		dataType: 'json',
		type: 'get',
		async: false,
		timeout: 1000,
		success: function(data) {
			authed = true;
			userInfo = JSON.stringify(data);
			plus.storage.setItem("userInfo", userInfo);
			userInfo = JSON.parse(userInfo);
		},
		error: function(xhr, textStatus, errorThrown) {
			authed = false;
		}
	});
	return authed;
}
```
