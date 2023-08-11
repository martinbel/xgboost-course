### Set up conda environment

conda create -n xgb python=3.9
conda activate xgb
conda install ipykernel
conda install -c conda-forge xgboost pandas scikit-learn plotnine seaborn

# pyarrow is optional
conda install -c conda-forge pyarrow

pip install optuna
pip install plotly
pip install nbformat

conda install ipykernel
conda install -c conda-forge xgboost pandas scikit-learn plotnine seaborn
