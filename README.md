# SageMaker models

    .
    ├── container       # Scripts to build the lstm docker image locally and/or publish it to AWS ECR.
    ├── data            # Input training data. Uploaded to S3 by run36.ipynb. SageMaker downloads it from S3 and mounts it to the running docker container at /opt/ml/input/data/training/* during the training job.
    ├── local           # Scripts to train and serve the model via the local docker engine.
    └── run36.ipynb     # Jypter notebook to train and serve the model via SageMaker. Written in Python 3.6.

The IAM role attached to the Jupyter instance must allow interaction with S3 and ECR.

Based on https://medium.com/@richardchen_81235/custom-keras-model-in-sagemaker-277a2831ac67
