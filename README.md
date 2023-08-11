# XGBoost Course - Youtube

## How to take the course - Self Study

To make the best use of the material my recommendation is to do the following for each section
Watch all the videos of the section and follow along the provided python code
Re-Watch the videos of the section but this time typing everything on your end on your local environment.

I'd strongly recommend you install Anaconda and jupyter notebooks on your local machine.
Learning how to configure an Anaconda environment is a very useful skill to deploy models in production.
If you find this too hard, you can try google colab to follow the course.
In any case, you can watch the videos first and then work on setting the environment.


## Environment Set-Up

If you are familiar with anaconda check out the setup_conda_env.sh file.

These are the commands I used to create the conda environment. There are many ways to do this, use the one you are most familiar with.
Open the terminal (linux or mac) or the Anaconda Shell in windows and run these commands:

1) Install Python 3.9 in a new environment
`conda create --name xgb python=3.9`

2) Activate conda environment

`conda activate xgb`

Some older versions of conda worked with source activate instead of conda activate

`source activate xgb`

3) Install libraries

```conda install ipykernel
conda install -c conda-forge xgboost pandas scikit-learn plotnine seaborn

# pyarrow is optional
conda install -c conda-forge pyarrow

pip install optuna
# libraries only used to make optuna plots
pip install plotly
pip install nbformat
```

### Alternative Method:

After steps 1) and 2).
3) Download the environment.yml file from this link and run this command in the terminal:

`conda env create -f environment.yml -n xgb`

After this you should be able to run:

`conda activate xgb`
`jupyter notebook`

If you get stuck installing one library ask a question in the videos or look for some tutorials on setting up an anaconda environment.
