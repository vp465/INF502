# Git/GitHub Assignment

* **INDIVIDUAL ASSIGNMENT**
* **Due date**: Sept-13th 11:59PM
* **Value**: 100 points counted towards Homework category.

## Description
This assignment is composed of two parts. 
- [Part 1](#Part-1-Dealing-with-git) consists of executing a sequence of commands and giving explanations about the commands you have to run. For each question, please provide appropriate explanation and/or the details requested.

- [Part 2](#Part-2-Using-GitHub) consists of creating a Markdown file on a fork of this course and creating a pull request towards this repo.

### Part 1: Dealing with git

To conduct this, you will have to download [handson.zip](handson.zip) and unzip it in your local machine. **Note:** handson folder is a git repository.

Then, follow these steps:

**On GitHub:**
1. Create a new repository under your GitHub account called *INF502*;
2. Create a file called *"Assignment1.md"*;
3. Copy the questions from this section and paste in your *"Assignment1.md"* file (tip: to copy the questions, click on *"Raw"* at the right-top of this file; this will show you the markdown source);
4. For each empty grey box, please provide an answer to the questions below.
5. Invite me to see your new repository. This will allow you to keep a private repository that only you and me will be able to see.

Your submission is complete when you complete the *Assigment1.md* file with your answers and invite me to your repo.

**On your local machine:** Using the command line, find and access the "handson/" directory (if you didn't download and unzip the file, go back to the beginning of Part 1's instructions). Then, answer the following questions (on your *Assigment1.md* file):

1. List all the branches in this repository and, for each branch, list the commits.

    - Use `git branch` to list the branches in this repository.
    - Use `git checkout` to explore each branch.
    - Use `git log --decorate` to explore the structure of commits.

```
- Use `git branch` to list the branches in this repository.
   There are 2 branch:
   Master 
   Math 
   
- Use `git checkout` to explore each branch.
1.)PS C:\Users\Vaishnavi\Downloads\handson\handson> git checkout math
   Switched to branch 'math'
2.)PS C:\Users\Vaishnavi\Downloads\handson\handson> git checkout master
   Switched to branch 'master'
   
Use `git log --decorate` to explore the structure of commits.
1.)PS C:\Users\Vaishnavi\Downloads\handson\handson> git log --decorate
  commit 18931d12a8be7cac049b73c6bc8136e9482f3371 (HEAD -> master)
  Author: Igor Steinmacher <igorsteinmacher@gmail.com>
  Date:   Wed Aug 14 23:15:28 2019 -0700

    Making a small change here

  commit 654b490a181dedf82dd6deda5f9848d6cca05918
  Author: Igor Steinmacher <igorsteinmacher@gmail.com>
  Date:   Wed Aug 14 23:12:14 2019 -0700

    Added a draft of A.py

  commit 2dfb02c3f9383d6c3b2695c99e175d8b85f594a1
  Author: Igor Steinmacher <igorsteinmacher@gmail.com>
  Date:   Wed Aug 14 23:08:47 2019 -0700

     Creating all files (all empty)
 2.) Commits will similar for math 


```

2. Try `git log --graph --all` to see the commit tree. Paste the result here and write a paragraph to provide an interpretation of what you found.
```
For git log --graph --all:
PS C:\Users\Vaishnavi\Downloads\handson\handson> git log --graph --all
* commit 18931d12a8be7cac049b73c6bc8136e9482f3371 (HEAD -> master)
| Author: Igor Steinmacher <igorsteinmacher@gmail.com>
| Date:   Wed Aug 14 23:15:28 2019 -0700
|
|     Making a small change here
|
| * commit e3c629dd524712aedea96d7dbaad1c50d12b5b5e (math)
|/  Author: Igor Steinmacher <igorsteinmacher@gmail.com>
|   Date:   Wed Aug 14 23:13:48 2019 -0700
|
|       Adding some more knowledge to the function
|
* commit 654b490a181dedf82dd6deda5f9848d6cca05918
| Author: Igor Steinmacher <igorsteinmacher@gmail.com>
| Date:   Wed Aug 14 23:12:14 2019 -0700
|
|     Added a draft of A.py
|
* commit 2dfb02c3f9383d6c3b2695c99e175d8b85f594a1
  Author: Igor Steinmacher <igorsteinmacher@gmail.com>
  Date:   Wed Aug 14 23:08:47 2019 -0700

       Creating all files (all empty)
       
       Interpretation:->
       1.) In the first commit it is observed that all files are created which are empty appartently.
       2.)In the second commit it is observed that some draft is added to file A.py.
       3.)In the third commit it is observed that some more knowledge is added to the function in the math branch.
       4.)In the fourth commit it is observed that some small changes are made .

```

3. Use `git diff BRANCH_NAME` to view the differences from a branch and the current branch. Summarize the difference from master to the other branch.

```
After using git diff result found are :
diff --git a/A.py b/A.py
index 0afa98c..dc1e9bd 100644
--- a/A.py
+++ b/A.py
@@ -1,11 +1,3 @@
 #this is just an example, do not freak out
 def calculate_this(operator, num1, num2):
-   if operator == 'sum':
-      print num1 + num2
-      print 'That was easy buddy'
-   else:
-      if operator == 'subtraction':
-         print num1 - num2
-         print 'I could handle that...'
-      else:
-         print 'my knowledge is limited'
+   print 'my knowledge is limited'
diff --git a/B.py b/B.py
index e69de29..c63f94c 100644
--- a/B.py
+++ b/B.py
@@ -0,0 +1 @@
+# Another file that will receive a line of code... at least.

Interpretation :
1.) A.py file in math branch has If else loops, but A.py file in master branch has no If Else loops 
2.) B.py file in master branch has comment and the B.py in math branch is empty


```

4. Write a command sequence to merge the non-master branch into `master`.

```
git merge BRANCH_NAME
for example :if we wan to merge the branch math then -> git merge math .

```


5. Write a command (or sequence) to (i) create a new branch called `math` (from the `master`) and (ii) change to this branch.

```
1.)To create a new branch called math:-> git branch math
2.)To change to this branch:-> git checkout math

```
   
6. Edit B.py adding the following source code below the content you have there.
```
print 'I know math, look:'
print 2+2
 
 PS C:\Users\Vaishnavi\Downloads\handson\handson> git commit -a -m "Added few lines in the B.py"
[master d5087cf] Added few lines in the B.py
 1 file changed, 1 insertion(+)
```

7. Write a command (or sequence) to commit your changes.
```
git commit -a -m "Added few lines in the B.py"


```

8. Change back to the `master` branch and change B.py adding the following source code (commit your change to `master`):
```
print 'hello world!'
```

9. Write a command sequence to merge the `math` branch into `master` and describe what happened.
```
git merge math
below conflict occured while merging 
Auto-merging B.py
CONFLICT (content): Merge conflict in B.py
Automatic merge failed; fix conflicts and then commit the result.
PS C:\Users\Vaishnavi\Downloads\handson\handson>
Description:
The conflict occured because the data in same line numbers for both file is different  .
```
   
10. Write a set of commands to abort the merge.
```
git merge --abort

```
   
11. Now repeat item 9, but proceed with the manual merge (editing B.py). All implemented methods are needed. Explain your procedure.
```
since in the 9 question we faced the conflict. To resolved that i have done a manual merge by removing line codes such as >>head,===, << math and then saved it . And then again commited in the terminal using git commit -a -m "edited B.py" which says it is already up to date .


```

12. Write a command (or set of commands) to proceed with the merge and make `master` branch up-to-date.
```
git merge math 
after this merge automatical master branch will be up to date 

```

13. Complete Part 2. Then, come back here and answer the following:
Report your experience of submitting the Part 2. Please, include the steps you followed, the commands you used, and the hurdles you faced (within the file you created for the **Part 1**).
```
As of for Part2 
I have edited my repository in the github itself, i haven't used any local editor .
In the Part1 we have used commands as such as git log -- decorate , git branch , git merge , etc  but along with that i have used commands such as git commit -a -m , git abort ,etc.Also there was apoint were i tried to merge the branches but the conflicts occured .And just to do some observation i used command git merge --abort . but later when i was trying to solve the conflict i was excepting some diferent source code for <<< HEAD ,======, <<<<<math meanwhile i forgot that that i already entered abort merge command . A soons as i realized my mistakes i made the changes .

```

### Part 2: Using GitHub

The goal of this assignment is to put you in touch with the fork-pull request process, with an extra of dealing a little bit with Markdown. To learn more about Markdown [click here](https://guides.github.com/features/mastering-markdown/).

To complete this submission, follow these steps:

1. Fork the course repository (available [here](https://github.com/chavesana/INF502-Fall22)).

2. Into the students folder, create a markdown file called LASTNAME_FIRSTNAME.md (please change LASTNAME_FIRSTNAME for your actual last and first names). 

3. Use markdown to write a report of the last paper you've read. You can structure your markdown the way you want, but the following information must be there:
- Title
- Venue (journal name/conference)
- Number of pages
- Three outcomes of the paper
- Link to the paper online

4. Commit your file and push to your own GitHub repository (INF502).

5. Create a pull request to the course repository. Your pull request needs to appear [here](https://github.com/chavesana/INF502-Fall22/pulls).

6. Go back to Part 1 and answer the question 13 based on your experience in solving Part 2.

Your Part 2 submission is complete when your pull request is listed in the link above.
