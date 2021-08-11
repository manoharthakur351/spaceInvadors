echo STATUS.............
git status


echo ADDING FILES.......
git add .


echo GIT STATUS.........
git status

echo WRITE YOUR COMMIT MSG......: 
read u
echo $u


echo COMMITING CHANGES........
git commit -m " msg $u "


echo PUSHING CHANGES.........
git push


echo PUSHING TO HEROKU.....
git push heroku main

echo LOGS ..........
git log

clear
# done
