[![Tests](https://github.com/andrdpedro/forniture-classification/workflows/Tests/badge.svg)](https://github.com/andrdpedro/forniture-classification/actions?workflow=Tests)
<h1 align="center">Forniture Classification</h1>

<h2 align="center" href="#objective">This project has the objective to classificate fornitures (Chair, Bed, Sofa), using Deep Learning</h2>

<h1 href="#technologies">The technologies used in this project are:</h1>
<p>- Tensorflow</p>
<p>- Keras</p>
<p>- FastAPI</p>

<h1 href="userguide">To use this project, you will need to:</h1>
<p> Install Docker in your personal Computer</p>
<p> Clone this repository using git clone</p>
<p> After cloning this repository, navigate to it using the terminal and type the following commands</p>
<p> Clone this repository using git clone</p>
<p> docker build -t fornitureimage .</p>
<p> docker run -d --name forniturecontainer -p 80:80 fornitureimage</p>
<p> After the last command notice that you need to wait some time as it is training the model</p>
<p> To see the logs of the progress of training, go to the dashboards in docker and access the container</p>
<p> Now you can access the API on http://127.0.0.1/docs</p>

<h1 href="#author">The author of this project is Pedro Andrade. Thanks for using it.</h1>
