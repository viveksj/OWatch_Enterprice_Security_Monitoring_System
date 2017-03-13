1) Make sure, xcode project has updated IP address of the webs server.
2) Go to tornado_bare-sklearn_example -> run "python tornado_scikit_learn.py"
3) Go to tornado_bare-sklearn_example -> mongodb -> bin -> run "sudo ./mongod --dbpath "data/db"
4) Go to parent folder -> run "python time1.py"
5) Go to parent folder -> run "python time2.py"
6) Go to parent folder -> project -> run "bundle" -> run "dashing start"
7) Go to browser -> type "0.0.0.0:3030" and hit enter. The dashboard will be online.

Note:
Make sure dependecy are installed for python and dashboard
Make sure the working directory is set correctly.