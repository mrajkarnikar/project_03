##Project 03

Scope of this project is to build on top what we have learned in the class. In the class different  algorigthms, both supervised and unsupervised of type classification and regression were covered. 

In this project, we will excercise how models are built using modern MLOPS practices using modern cloud data platform - mainly AWS Sagemaker. 

Topics that will be covered are:

- Feature Store and Feature Engineering
- Model Monitoring
- Model Registry
- Experiments Management
- ML Pipelines
- Automl
- AI explainability
- Inference

#### Feature store
Features are  all the data that we use to create model. Feature engineering is the process of transforming the data from various source and making it ready build model on top. It is basically an ETL process . 
Feature storeis is where we store the feature data. Feature store and engineering encourages reuse of code and  data.  It also helps bring in  standarization on the ETL process. Feature store usually provide search and discovery(data catalog)

There are 2 types of features:online feature and offline feature. Online feature support faster lookup and are used for real time inference  whereas offline feature are slow but efficient for bulk batch training and batch inference 

#### Experiment Management

Experiment is where a datascientist tries different things eg different model, different transformation, different hyperparameters etc to come up with most effective model. Experiment management is a process of organizing and tracking experiment metadata like code version, data version, metrics, hyperparameters etc. It allows users  to compare different models via different metrics, charts/plot, logs. 

  
#### Model Registry
Model registry is where the models are stored. Every experiment produces a model. Each model has different metrics, different bias report etc
Models are usually versioned and only approved models are deployed . 

#### Pipeline
Once a model is created, there are set of things that should happen. Such as check the quality of the model. bias check, load testing, a/b testing, rollback if necessary, model approval for production deployment. We need to be able to do this in consistent and automated way. That is what pipeline does

This is an example of cicd pipeline used in this project

![Pipeline](./img/pipeline.jpg  =250x250)

#### Inference
In the real world, models need to wrapped around an API so that it can be easily invoked. There is a lot that goes into building production quality apis. Data scientist should not have to worry about any of that and  creating an api should be super simple: one click deployment. All ml cloud platform provide that. They also provide logging/metrics/monitoring/infrastucture/autoscaling/serverless deployment
  
#### Model Monitoring
Inference need to be monitored. if there is changes in data quality, or data itself changed, we might have to retrain the model.

#### Automl
All the ml platform normally provide some kind of auto ml functionality. 


### End to End model pipeline

To test these all these feature and capabilities, we are using abalone project. Abalone is a kind of shell fish . It has list of attributes like length, width, different kind of weight(like weight of meat, guts, weigth after they dry etc).  The goal here is to figure out the the age of the abalone. Age is reflected by the rings on their shell. But counting the ring is hard, it require cutting of shell in certain way, staining the shell for better visibility and then counting the ring.This whole process is time consuming whereas gathering all those dimension mention earlier is easier.

Approach we can here is use other dimension to predict the age of the shellfish

### Dataset for the  Abalone Pipeline

The dataset used is the [UCI Machine Learning Abalone Dataset](https://archive.ics.uci.edu/ml/datasets/abalone) [1]. The aim for this task is to determine the age of an abalone (a kind of shellfish) from its physical measurements. At the core, it's a regression problem. 
    
The dataset contains several features - length (longest shell measurement), diameter (diameter perpendicular to length), height (height with meat in the shell), whole_weight (weight of whole abalone), shucked_weight (weight of meat), viscera_weight (gut weight after bleeding), shell_weight (weight after being dried), sex ('M', 'F', 'I' where 'I' is Infant), as well as rings (integer).

### Layout of the SageMaker ModelBuild Project Template

The template provides a starting point for bringing your SageMaker Pipeline development to production.

```
|-- codebuild-buildspec.yml
|-- CONTRIBUTING.md
|-- pipelines
|   |-- abalone
|   |   |-- evaluate.py
|   |   |-- __init__.py
|   |   |-- pipeline.py
|   |   `-- preprocess.py
|   |-- get_pipeline_definition.py
|   |-- __init__.py
|   |-- run_pipeline.py
|   |-- _utils.py
|   `-- __version__.py
|-- README.md
|-- sagemaker-pipelines-project.ipynb
|-- setup.cfg
|-- setup.py
|-- tests
|   `-- test_pipelines.py
`-- tox.ini
```

## Start here
 `pipelines/pipelines.py` contains the core of the business logic for this problem. It has the code to express the ML steps involved in generating an ML model. You will also find the code for that supports preprocessing and evaluation steps in `preprocess.py` and `evaluate.py` files respectively.

Once you understand the code structure described below, you can inspect the code and you can start customizing it for your own business case. This is only sample code, and you own this repository for your business use case. Please go ahead, modify the files, commit them and see the changes kick off the SageMaker pipelines in the CICD system.

You can also use the `sagemaker-pipelines-project.ipynb` notebook to experiment from SageMaker Studio before you are ready to checkin your code.

A description of some of the artifacts is provided below:
<br/><br/>
Your codebuild execution instructions. This file contains the instructions needed to kick off an execution of the SageMaker Pipeline in the CICD system (via CodePipeline). You will see that this file has the fields definined for naming the Pipeline, ModelPackageGroup etc. You can customize them as required.

```
|-- codebuild-buildspec.yml
```

<br/><br/>
Your pipeline artifacts, which includes a pipeline module defining the required `get_pipeline` method that returns an instance of a SageMaker pipeline, a preprocessing script that is used in feature engineering, and a model evaluation script to measure the Mean Squared Error of the model that's trained by the pipeline. This is the core business logic, and if you want to create your own folder, you can do so, and implement the `get_pipeline` interface as illustrated here.

```
|-- pipelines
|   |-- abalone
|   |   |-- evaluate.py
|   |   |-- __init__.py
|   |   |-- pipeline.py
|   |   `-- preprocess.py

```
<br/><br/>
Utility modules for getting pipeline definition jsons and running pipelines (you do not typically need to modify these):

```
|-- pipelines
|   |-- get_pipeline_definition.py
|   |-- __init__.py
|   |-- run_pipeline.py
|   |-- _utils.py
|   `-- __version__.py
```
<br/><br/>
Python package artifacts:
```
|-- setup.cfg
|-- setup.py
```


