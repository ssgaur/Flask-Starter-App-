COntact APP
=========================

How to build
------------
./flask-app-build <verion_minor> <version_major>

1. Above script will genrate a Debian file.  Now install debian file in any Ubuntu Machine with sudo dpkg -i <generatd_file>.deb



Current APIs
------------

Each API needs a header in Request ith field name as below

email: "String"

for API 1 and 2:  
Request Body: 
{
    "email" : string,
    "password" : string
}
1. http://localhost:700/api/vi/user/login  [POST]
2. http://localhost:700/api/vi/user/register [POST]


3. http://localhost:700/api/vi/contact/search?startIndex=1&limit=10&searchTerm=abcd  [GET]

for API 4 ,5 
Request Body: 
{
    "email" : string,
    "name" : string,
    "phone": string,
     ......
}

4. http://localhost:700/api/vi/contact   [POST]
5. http://localhost:700/api/vi/contact   [PUT]
6. http://localhost:700/api/vi/contact   [DELETE]


Integration testing (Testing for Contact APIs  CREATE, PUT and Delete)
------------


How run:

CD into Repo directory
Just Run

sudo python setup.py test
