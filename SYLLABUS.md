# duq_ds3_2025

A repository of course materials for Duquesne University's Data Science 330 course, 2025.

In this class, we are a data science team with expectations to match. You are welcome to ask others for help, but at the same time are required to do your own work.

# Syllabus

Each day we will alternate theory with practice. Practice will involve both my coding in front of you, as well as taking turns coding in front of each other. Given that many job interviews require public coding, this is excellent, if occasionally challenging experience.

Note that we will adapt later weeks of the course to the interests of everyone in the course.

# Grading

It is easy to do well in this course. Seriously. Show up, engage, have fun, take notes, do the homework, and program occasionally on your own throughout the semester.

Because we are a data science team, treat this as you would a job. It matters that you show up and that you show interest. I'd much rather work with someone who is engaged than someone who plays on their phone.

Grades in this class are based on creating tools that are readable, runnable, and well-documented. 60% of the grade is code quality, 40% is documentation quality.

For the exceptionally few students who need external pressure to show up to class, attendance is essential. Grades will decrease exponentially based on the number of days missed (0, -1%, -2%, -4%... for 1-4 days respectively).

Ample time will be given for homeworks, and they should be viewed both as a chance to practice and a mechanism of expanding the documented code in your Github (which will help with future jobs). Collaboration is highly valued, but if overly similar code is submitted, I reserve the right to request independent explanations of how the code works and the thought behind its organization. Push commits to Github _before each class_. If code appears to be duplicated and is committed in a single entry after the commits of matching code, the history of the code becomes clear.

If you are concerned about the final exam, you are welcome to meet with me to do a practice prior to the exam. Whether you've completed the homework and documented it well is obvious. But, if you are concerned with whether or not you are sufficiently participating, you can schedule time to chat about it at any point during the semester, and we can talk about mechanisms of improvement if necessary. Given these open channels of communication, however, requests to change a grade at the end of the semester will not go well. Assume that I am giving you the benefit of the doubt.

## Final exam

The final exam will be a mock job interview. It will be comprised of the following portions:

- Evaluation of Github, all of which will be filled in the previous weeks (is there high-quality Python code with functions, documentation, and a cohesive project): 40% (If you cared about your work during the semester and have put substantial effort into your Github, the weight of the coding challenge will decrease and the weight of the Github will increase.)
- Description of previous work: 40%
- Coding challenge: 20%

# Code necessities

I highly recommend using a unix-based system for programming-- either dual-boot a windows machine with Ubuntu or use a Mac. The computer lab is fantastic and has computers that can boot into Ubuntu. If necessary, then the easiest way to use Python on a Windows machine is using a combination of Anaconda and Git Bash.

To install Git bash: https://git-scm.com/download/win

(Given that Anaconda was used in DS1, I am assuming that you have already installed Anaconda.)

To ensure that you can use Anaconda from within Git Bash, checkout the first answer to this Stack Overflow question: https://stackoverflow.com/questions/54501167/anaconda-and-git-bash-in-windows-conda-command-not-found

It may seem weird that a course syllabus links to Stack Overflow, but you will find that the professional experience of Data Science often involves using Google for solutions. Installing core Unix components is one of the most frustrating tasks in computing, regardless of operating system, but doing so provides excellent experience.

## SSH Issues

For Github, if you want to use ssh, there are a variety of ways to deal with this.

1. PyCharm: https://www.jetbrains.com/help/pycharm/create-ssh-configurations.html
1. Github more generally: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

## Slack

You may have noticed that you've been sent a slack invite. This is never required, but it's an easy way to contact me if you have questions. It's also a great place to ask other folks in the class questions that you might have. There's nothing worse than getting stuck programming, and having others around is key.

## Notes

1. Set up your own Github account
1. Github accounts should include at least one example of Python, with docstrings
1. I recommend using VSCode + poetry (historically venv) for installation
1. Let's use Python 3.8+

# Schedule

## Week 1

- Discuss everyone's backgrounds
- Discuss each student's desired outcomes from the course
- VSCode/local coding
  - Install VSCode
- Code documentation
  - Fuctions
  - Type hinting
  - Docstrings
  - Libraries versus scripts
  - Colab vs VSCode
- Github
  - Setup
  - READMEs
  - gitignore
  - cloning
  - adding
  - commiting
  - pushing
  - pulling
  - branching
  - diff
- Go over some cool models from industry
  - Spotify
  - ChatGPT, quickly
- Discuss features and labels

Evaluation:

- Set up Github account, add at least one repository with documentation
- Set up VSCode locally

## Week 2

Dataset: https://reporter.nih.gov/exporter

- Rules for ChatGPT and why
- CVs/Resumes
  - Focus on projects
  - Improve your Github
  - Match keywords from job descriptions
- Pandas
  - All Pandas, all the time
  - What is Pandas?
    - Numpy-based, which is C-based
  - Comfort and speed
  - Good habits such as apply
  - Bad habits such as for loops
  - Data merging
- Pandas is easy, efficiency is hard
- Numpy/Pandas translation
- Grants data reading function

Evaluation:

- How do you fill in the missing dates from the grants data?

## Week 3

- Classification introduction
  - Examples of classification in data science
- Create a reusable function for training a classifier
- Create a reusable function for saving a classifier
- Create a reusable function for loading and running a classifier
  - Scikit-learn

Evaluation:

- Move the classifier into a new project-specific repository

## Week 4

- Talk about the hackathon
- Talk about Semantle
- Decision trees slides
  - Random forest
  - XGBoost
- Download the wine quality dataset: https://archive.ics.uci.edu/dataset/186/wine+quality
  - Use it with an xgboost model
- Natural language processing
  - spacy
  - fasttext
  - nltk
- Download the weekly incremental NPI file: https://download.cms.gov/nppes/NPI_Files.html

Evaluation:

- Create a file reader to put the incremental NPI in a useful format for matching with the grants data

## Week 5

NOTE: Installing fasttext on python 3.12 or higher requires a workaround:

```
poetry add git+https://github.com/cfculhane/fastText
```

- Return to Semantle as an example of word2vec
- Compare on the screen the reader functions submitted by each person
- Use one to load data
- Talk about bias in data
  - Finance field, zip code
  - Amazon hiring
  - Judicial predictions
- Create a function together to produce entity resolution features
- How to create training data
  - Simulation
  - Hand-labeling
  - Recursive
- Recursive model training
  - Bias
  - Bootstrapping + class mislabels

Evaluation:

- We know that there are tools that can find similarity in vectors (hnsw) as well as tools that can create vectors out of anything (e.g. word2vec or fasttext ). How can we use these ideas to ensure that we don’t do all-to-all comparisons?
- We put together a tool that could pass test data through, but not training data. Can you create a small number of rows of training data-- 20 at least-- in a CSV.
- Pass the training data through the classifier. It’s key that you can return the probabilities here. Remember, we’ll use this to identify a range of difficulties of problem to feed back in

## Week 6

The day of code

- Talk through everyone's classifier
- Create training data together (20-100 entries only)
- Combine together the functions to be able to train data
- Create sequential training data

The "blocking" problem

- Blocking problem and nearest neighbor indices
- Combine together to create a tool to classify the two datasets

## Week 7

- How has each person addressed the blocking problem?
- How has each person created a training set?

  - We need more data. Let's use a database

- Why a database?
  - Keeps data in sync between people
  - Designed for fast reading
  - Consistency
- Short database types overview
  - No SQL (e.g. MongoDB)
  - SQL
  - ETL (Extract, Transform, Load)
  - Spark
    - Databricks
- SQL introduction
  - SQLite v MySQL v Postgres
  - CREATE
  - row types
- Data tables
- Bridge tables

  - Relationships between tables

- Create database for our two datasets
- Create bridge table

- Embed and Blocking

Evaluation:

- Create at least three tables-- one for npi data, one for grants data, and a bridge table. - Insert the data from the reader classes you’ve created into the table

## Week 8

- Each person explains their current state

- Continue with SQL

  - SELECT and INSERT
  - DELETE FROM
  - JOIN
  - WHERE

- NetworkX and connected components
- Store training data in database

Evaluation:
By next week, everyone should have (this is all from previous weeks)

1. a grants reader class
1. an npi/doctor reader class
1. training data for a model to map people from grants to doctors (npi). Can be short.
1. an XGB model that is a binary classifier to determine whether a grantee and doctor are the same person, trained from the data
1. code to insert the cleaned grants data from (a) into the database
1. code to insert the cleaned npi data from (b) into the database
1. a sqlite database with the data inserted
1. a bridge table as well in the sqlite database
1. The only new thing is can you have code that can pull from the database that we will be able to pass through the XGB classifier

- If you have everything and are pondering what to do-- take a moment to organize your code. It’s good to test it out in VSCode and you’ll be astounded by how much more you know about the problem and how much easier it is to organize it

## Week 9

- You know that prep-before-the-midterm thing? That's this week. You've been working hard to get your code organized. We're going to start from scratch and reproduce everything, covering whatever questions you have. We will end with a working implementation of the entire pipeline based on everything we've learned, beginning with a brand-new repository. It is essential that you use this chance to ask all of those burning questions.

Evaluation (skipped for this week):

# Week 10

- Finishing up the review from Week 9
- Focus on creating a dataset and training the model
  - Reiterate using edge cases to improve model performance
  - Cover the "blocking" process again
    - Embedding + nearest neighbors
    - By last name

Evaluation:

- Create the final file-- a file that loads in blocks of data from the database and runs the trained model on the output
- Who makes the coolest CNN? https://teachablemachine.withgoogle.com/

# Week 11

- Go through the final file-- pushed to week 13
- Autoencoder in tensorflow
- Create our own neural network library

Evaluation:
Optional: check out backpropagation at the "neuron" level here: https://github.com/asugden/nn_intro/tree/main/nn_intro/nn_by_scalar and https://www.youtube.com/watch?v=VMj-3S1tku0

# Week 12

- Finish the autoencoder in tensorflow, training it on the wine quality dataset
- Finish the neural network library
- Apply tensortango (the NN library) to the wine quality dataset
- Consider how CNNs are a minor variant of what we've built

Evaluation:

- Compare the predictions of wine quality from the XGBoost classifier we made back in week 4 with the outcomes of an XGBoost classifier trained on data that has been dimensionality reduced using an autoencoder?
- We created the autoencoder in class with tensorflow, but for those folks who’ve been having problems running it, I will upload data with different numbers of dimensions
- Then, can you state approximately what the underlying dimensionality of the data is and why?

# Week 13

- Go over the last file in the model

  1. Get the "blocks" or set of last names from one of the datasets in the database
  1. Iterate through the blocks, pulling data from the database
  1. Create features from the two datasets
  1. Predict whether the lines match
  1. Add the matched lines to the bridge table in the database

- Graph theory

  - Download the MBTA data: https://mbta-massdot.opendata.arcgis.com/datasets/MassDOT::mbta-rapid-transit-stop-distances/explore
  - If need be, consult the map: https://www.mbta.com/schedules/subway
  - Create a graph in class that allows you to answer "what is the fastest way from Copley to Airport"
  - Can consider adding penalties for switching lines
  - Use `add_weighted_edges_from` and `shortest_path`

- Are we training for false positives or false negatives?
  - It is very important, for each problem, to consider what is the more problematic error case
  - Compare opioid cravings to entity resolution

# Week 14

This week is a grab-bag based on requests.

- Flask
- AWS
  - EC2
  - RDS
- Google cloud
  - Firebase
- Feature engineering
- TF-IDF
- Tokenization
- Image augmentation
- Standardizing pixels

## Final Exam

A job interview in which we evaluate your entire Github, as well as ask questions on topics covered throughout the course
