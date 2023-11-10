# reg_wine_quality
Regression of wine quality

# What the Project is about ?
The Project is mainly prepared and executed to learn
1. How to write modular coding for end to end MLOPS
2. How the MLOPS is executed using dvc.yaml
3. How to use MLFLOW to track experiments and runs ( I have provided the link for this project exp)

# Big Thanks to.....
A heartful thanks to KRISH NAIK for his sharing of knowledge and also thanks to BOKTIAR AHMED BAPPY for shaing the knowledge of MLOPS

# How to use the rep
1. Clone the repository
```bash
https://github.com/vikramviky123/reg_wine_quality
```
2. Create environment using
```bash
conda create -p myenv python==3.10.9 -y
```
3. Install all dependancies from requirements.tx
```bash
pip install -r requirements.txt
```
4. runpython file( attached same output at the bottom)
```bash
python main.py
```

# How the Project flows
The project has

1. src folder:This folder is the heart of the project where modular coding just flows from file to file
2. I has subfolders constants, entity, configuration manager, components, pipeline, utils each serve there purpose.

The flow is as follows
* config file: (its yaml file holds data of folder paths)
* entity: (its a class to create instances for paths)
* configuration manager: (its a class, stores paths from config.yaml to entity instances)
* components: (it has several files starting from creation of config instances, using the instances to create directories and ingest data, develop model trainer, develop evaluation file, develop predict file(for url use))
* pipeline: (it runs all required files of in components as line by line with one file)
* utils: (it has misc code, example to create yaml file, save pickle file, load files etc anything which is common to use in all the folders)

The flow is summarized to give the effect as below

* DATA INGESTION
* DATA TRANSFORMATION
* MODEL TRAINING
* MODEL EVALUATION
* PREDICT

The pipeline runs the above one by one with just one file, the use of dvc is it tracks all the runs.
lets say you change parameters the change is only in training so, the dvc runs only from MODEL TRAINING....which saves lot of time and resources

# Reign of mlflow
It is very hard to track the results of each and every ml algo on training and testing.
mlflow can track parameters, metric and loss results etc


# Dagshub
This the website, which helps to track experiments remotely
https://dagshub.com/vikramviky123/reg_wine_quality

# Experiment tracking data from dagshub.com (from the connected repository)
MLFLOW_TRACKING_URI=https://dagshub.com/vikramviky123/reg_wine_quality.mlflow \
MLFLOW_TRACKING_USERNAME=vikramviky123 \
MLFLOW_TRACKING_PASSWORD=5a2f68ea5e0aec2c756d6c161922b40f4e682d32 \
python script.py

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/vikramviky123/reg_wine_quality.mlflow
export MLFLOW_TRACKING_USERNAME=vikramviky123
export MLFLOW_TRACKING_PASSWORD=5a2f68ea5e0aec2c756d6c161922b40f4e682d32
```

# Find my experiments here
https://dagshub.com/vikramviky123/reg_wine_quality/experiments/#/

# main.py output

```cmd
(base) C:\Users\91981\Desktop\GREAT LEARNING\FROM SCRATCH LEARNING\Krish Naik Projects\WIP\reg_wine_quality>python main.py
[2023-11-10 20:26:33,462] 148 numexpr.utils - INFO - Note: NumExpr detected 12 cores but "NUMEXPR_MAX_THREADS" not set, so enforcing safe limit of 8.
[2023-11-10 20:26:33,462] 160 numexpr.utils - INFO - NumExpr defaulting to 8 threads.
[2023-11-10 20:26:39,302] 31 root - INFO - yaml file: globalparams.yaml loaded successfully
[2023-11-10 20:26:41,455] 11 root - INFO - 

x==========x

>>>>>> stage DATA -- INGESTION -- STAGE started <<<<<<


[2023-11-10 20:26:41,471] 31 root - INFO - yaml file: config\config.yaml loaded successfully
[2023-11-10 20:26:41,471] 50 root - INFO - created directory at: artifacts
[2023-11-10 20:26:41,471] 50 root - INFO - created directory at: artifacts/data_ingestion
[2023-11-10 20:26:41,471] 50 root - INFO - created directory at: artifacts/data_ingestion/downloaded
[2023-11-10 20:26:41,471] 50 root - INFO - created directory at: artifacts/data_ingestion/extracted
[2023-11-10 20:26:42,287] 23 root - INFO - artifacts/data_ingestion/downloaded/wine_data.zip download! with following info: 
Connection: close
Content-Length: 23329
Cache-Control: max-age=300
Content-Security-Policy: default-src 'none'; style-src 'unsafe-inline'; sandbox
Content-Type: application/zip
ETag: "c69888a4ae59bc5a893392785a938ccd4937981c06ba8a9d6a21aa52b4ab5b6e"
Strict-Transport-Security: max-age=31536000
X-Content-Type-Options: nosniff
X-Frame-Options: deny
X-XSS-Protection: 1; mode=block
X-GitHub-Request-Id: 1CA8:2CB714:AEE6E:11EDCE:654E307D
Accept-Ranges: bytes
Date: Fri, 10 Nov 2023 14:56:38 GMT
Via: 1.1 varnish
X-Served-By: cache-hyd1100031-HYD
X-Cache: HIT
X-Cache-Hits: 1
X-Timer: S1699628198.969195,VS0,VE255
Vary: Authorization,Accept-Encoding,Origin
Access-Control-Allow-Origin: *
Cross-Origin-Resource-Policy: cross-origin
X-Fastly-Request-ID: 9f22d05f0529684880727c21a549324d8ccd6b00
Expires: Fri, 10 Nov 2023 15:01:38 GMT
Source-Age: 0


[2023-11-10 20:26:42,305] 15 root - INFO - 

>>>>>> stage DATA -- INGESTION -- STAGE completed <<<<<<

x==========x


[2023-11-10 20:26:42,306] 25 root - INFO -

x==========x

>>>>>> stage DATA -- TRANSFORMATION -- STAGE started <<<<<<


[2023-11-10 20:26:42,311] 31 root - INFO - yaml file: config\config.yaml loaded successfully
[2023-11-10 20:26:42,313] 50 root - INFO - created directory at: artifacts
[2023-11-10 20:26:42,313] 50 root - INFO - created directory at: artifacts/data_transformation
[2023-11-10 20:26:42,356] 31 root - INFO - Splited data into training and test sets
[2023-11-10 20:26:42,356] 32 root - INFO -  Train Shape ==> (1199, 12) | test Shape ==> (400, 12)
[2023-11-10 20:26:42,356] 29 root - INFO -

>>>>>> stage DATA -- TRANSFORMATION -- STAGE completed <<<<<<

x==========x


[2023-11-10 20:26:42,356] 39 root - INFO -

x==========x

>>>>>> stage MODEL -- TRAINING -- STAGE started <<<<<<


[2023-11-10 20:26:42,373] 31 root - INFO - yaml file: config\config.yaml loaded successfully
[2023-11-10 20:26:42,373] 50 root - INFO - created directory at: artifacts
[2023-11-10 20:26:42,373] 50 root - INFO - created directory at: artifacts/model_trainer
[2023-11-10 20:26:42,373] 31 root - INFO - yaml file: globalparams.yaml loaded successfully
[2023-11-10 20:26:42,390] 31 root - INFO - yaml file: params.yaml loaded successfully
[2023-11-10 20:26:42,441] 76 root - INFO - tuning parameters for model: random_forest
[2023-11-10 20:27:49,366] 87 root - INFO - tuning done for == random_forest== DONE
[2023-11-10 20:27:49,366] 88 root - INFO - --------------------------------------------------------------------------------
[2023-11-10 20:27:49,366] 76 root - INFO - tuning parameters for model: histgradient_boost
[2023-11-10 20:28:59,262] 87 root - INFO - tuning done for == histgradient_boost== DONE
[2023-11-10 20:28:59,262] 88 root - INFO - --------------------------------------------------------------------------------
[2023-11-10 20:28:59,262] 76 root - INFO - tuning parameters for model: xgb_regressor
[2023-11-10 20:29:14,457] 87 root - INFO - tuning done for == xgb_regressor== DONE
[2023-11-10 20:29:14,457] 88 root - INFO - --------------------------------------------------------------------------------
[2023-11-10 20:29:14,457] 76 root - INFO - tuning parameters for model: lgbm_regressor
[2023-11-10 20:29:49,853] 87 root - INFO - tuning done for == lgbm_regressor== DONE
[2023-11-10 20:29:49,853] 88 root - INFO - --------------------------------------------------------------------------------
[2023-11-10 20:29:49,853] 91 root - INFO - Initiating model : random_forest
[2023-11-10 20:30:12,077] 102 root - INFO - Model ==random_forest== trained with best params == DONE
[2023-11-10 20:30:12,077] 104 root - INFO - --------------------------------------------------------------------------------
[2023-11-10 20:30:12,077] 91 root - INFO - Initiating model : histgradient_boost
[2023-11-10 20:30:41,433] 102 root - INFO - Model ==histgradient_boost== trained with best params == DONE
[2023-11-10 20:30:41,433] 104 root - INFO - --------------------------------------------------------------------------------
[2023-11-10 20:30:41,433] 91 root - INFO - Initiating model : xgb_regressor
[2023-11-10 20:30:51,415] 102 root - INFO - Model ==xgb_regressor== trained with best params == DONE
[2023-11-10 20:30:51,415] 104 root - INFO - --------------------------------------------------------------------------------
[2023-11-10 20:30:51,415] 91 root - INFO - Initiating model : lgbm_regressor
[2023-11-10 20:31:01,791] 102 root - INFO - Model ==lgbm_regressor== trained with best params == DONE
[2023-11-10 20:31:01,791] 104 root - INFO - --------------------------------------------------------------------------------
[2023-11-10 20:31:01,807] 119 root - INFO - best parameters SAVED as bestparams.yaml
[2023-11-10 20:31:05,355] 101 root - INFO - binary file saved into: artifacts\model_trainer\trained_models.joblib
[2023-11-10 20:31:05,355] 122 root - INFO - trained models are SAVED in artifacts\model_trainer\trained_models.joblib
[2023-11-10 20:31:05,355] 101 root - INFO - binary file saved into: artifacts\model_trainer\best_params.joblib
[2023-11-10 20:31:05,355] 124 root - INFO - best params dict SAVED in artifacts\model_trainer\best_params.joblib
[2023-11-10 20:31:05,355] 101 root - INFO - binary file saved into: artifacts\model_trainer\eval_results.joblib
[2023-11-10 20:31:05,355] 126 root - INFO - evaluation metrics of valid and test SAVED in artifacts\model_trainer\eval_results.joblib 
[2023-11-10 20:31:05,442] 43 root - INFO - 

>>>>>> stage MODEL -- TRAINING -- STAGE completed <<<<<<

x==========x


[2023-11-10 20:31:05,444] 53 root - INFO -

x==========x

>>>>>> stage MODEL -- EVALUATION -- STAGE started <<<<<<


[2023-11-10 20:31:05,449] 31 root - INFO - yaml file: config\config.yaml loaded successfully
[2023-11-10 20:31:05,450] 50 root - INFO - created directory at: artifacts
[2023-11-10 20:31:05,452] 50 root - INFO - created directory at: artifacts/model_evaluation
[2023-11-10 20:31:05,474] 31 root - INFO - yaml file: bestparams.yaml loaded successfully
[2023-11-10 20:31:05,500] 115 root - INFO - binary file loaded from: artifacts\model_trainer\eval_results.joblib
2023/11/10 20:31:06 WARNING mlflow.sklearn: Model was missing function: predict. Not logging python_function flavor!
C:\Users\91981\anaconda3\lib\site-packages\_distutils_hack\__init__.py:33: UserWarning: Setuptools is replacing distutils.
  warnings.warn("Setuptools is replacing distutils.")
2023/11/10 20:31:12 WARNING mlflow.sklearn: Model was missing function: predict. Not logging python_function flavor!
2023/11/10 20:31:16 WARNING mlflow.sklearn: Model was missing function: predict. Not logging python_function flavor!
2023/11/10 20:31:20 WARNING mlflow.sklearn: Model was missing function: predict. Not logging python_function flavor!
[2023-11-10 20:31:24,331] 57 root - INFO - 

>>>>>> stage MODEL -- EVALUATION -- STAGE completed <<<<<<

x==========x
```

