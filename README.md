[![Tests](https://github.com/andrdpedro/forniture-classification/workflows/Tests/badge.svg)](https://github.com/andrdpedro/forniture-classification/actions?workflow=Tests)
<h1 align="center">Forniture Classification</h1>

<h2 align="center" href="#objective">This project has the objective to classificate fornitures images (Chair, Bed, Sofa), using Deep Learning alghoritm. Notice that its a inicial project and a lot of work need to be done.</h2>

<h1 href="#technologies">The technologies used in this project are:</h1>
<p>- Tensorflow</p>
<p>- Keras</p>
<p>- FastAPI</p>

<h1 href="userguide">To use this project, you will need to:</h1>
<ol>
  <li> Install Docker in your personal Computer</li>
  <li> Clone this repository using git clone</li>
  <li> After cloning this repository, navigate to it using the terminal and type the following commands</li>
  <li> Clone this repository using git clone</li>
  <li> docker build -t fornitureimage .</li>
  <li> docker run -d --name forniturecontainer -p 80:80 fornitureimage</li>
  <li> After the last command notice that you need to wait some time as it is training the model</li>
  <li> To see the logs of the progress of training, go to the dashboards in docker and access the container</li>
  <li> Now you can access the API on http://127.0.0.1/docs</li>
</ol>

<h1 href="#author">The author of this project is Pedro Andrade. Thanks for using it.</h1>
