# DSBench

## Overview
DSBench is a benchmark for evaluating data science agents with 
realistic data analysis and data modeling tasks collected from 
modeloff and kaggle. 
Given a *task instruction (may contain image and table)* and
*data files*, a data science agent is tasked with generating 
a *solution* that resolves the described task.

<p align="center">
<img src="figures/overview_new.png">
</p>

## Set Up
For evaluation, you should install the Python packages in the requirment.txt file.

## Usage

1. Clone this repo.
2. Install all the requirments in Set Up.
3. For evaluation on data analysis task, refer to [./data_analysis/readme.md](https://github.com/LiqiangJing/DSBench/blob/main/data_analysis/readme.md).
4. For evaluation on data modeling task, refer to [./data_modeling/readme.md](https://github.com/LiqiangJing/DSBench/blob/main/data_modeling/readme.md).

## Results
| Framework      | Model        | Task-level Accuracy /% | Cost / $ | Inference Time / min | Competition-level Accuracy /% |
| -------------- | ------------ | ---------------------- | -------- | -------------------- | ----------------------------- |
| Model-only     | LLAVA        | 11.59                  | -        | 106.0                | 7.01                          |
|                | LLaMA-8b     | 16.95                  | -        | 130.3                | 10.60                         |
|                | LLaMA-70b    | 23.33                  | -        | 422.6                | 14.95                         |
|                | GPT-3.5      | 20.39                  | 1.95     | 27.6                 | 11.85                         |
|                | GPT-4        | 25.97                  | 117.90   | 162.7                | 17.21                         |
|                | GPT-4o       | 28.11                  | 67.56    | 115.5                | 19.26                         |
|                | GPT-4o mini  | 23.82                  | 2.21     | 87.1                 | 14.95                         |
|                | Claude       | 6.01                   | 64.98    | 5188.8               | 3.83                          |
|                | Gemini       | 31.55                  | 18.26    | 5331.7               | 24.81                         |
| AutoGen        | LLaMA-8b     | 10.73                  | -        | 221.7                | 6.05                          |
|                | LLaMA-70B    | 21.89                  | -        | 762.9                | 13.64                         |
|                | GPT-3.5      | 20.82                  | 5.60     | 184.8                | 12.80                         |
|                | GPT-4        | 30.69                  | 105.89   | 529.5                | 22.68                         |
|                | GPT-4o       | 34.12                  | 114.05   | 286.0                | 26.72                         |
|                | GPT-4o mini  | 28.11                  | 2.95     | 379.6                | 21.01                         |
| Code Interpreter | GPT-3.5    | 11.16                  | 21.39    | 197.2                | 8.23                          |
|                | GPT-4        | 23.82                  | 128.83   | 334.5                | 22.65                         |
|                | GPT-4o       | 23.82                  | 87.04    | 236.1                | 22.65                         |
|                | GPT-4o mini  | 17.81                  | 16.54    | 233.2                | 14.65                         |

<p align="center">
<img src="figures/result1.png">
</p>

<p align="center">
<img src="figures/result2.png">
</p>

##  Disclaimer
The dataset provided is intended solely for educational and research purposes, with the goal of fostering research in related areas. Users of this dataset are required to adhere to the following guidelines:

- Data Source and Accuracy: While efforts have been made to curate and organize the data, we make no guarantees regarding the accuracy, completeness, or timeliness of the dataset. Users are encouraged to independently verify the data's accuracy and assume full responsibility for any conclusions drawn from it.

- Usage Restrictions: This dataset is strictly for non-commercial use. Any commercial development or profit-driven activity requires explicit written permission from the dataset providers.

- Privacy and Compliance: Users must ensure that their use of the dataset complies with all applicable laws and regulations, particularly those related to privacy and data security. The dataset providers are not responsible for any legal consequences arising from improper use of the data.

- Non-Infringement: The pre-processed data provided by us is intended solely for educational and research purposes. We do not claim ownership of the original data, and any use of this data should respect the rights of the original creators. Users are responsible for ensuring that their use of the data does not infringe on any copyrights or other intellectual property rights.

- Disclaimer of Liability: The dataset providers shall not be held liable for any direct or indirect consequences resulting from the use of this dataset, including but not limited to losses, damages, or liabilities arising from reliance on the information contained within the dataset.

##  Citation
If you find our work helpful, please use the following citations.
```
@inproceedings{
}
```



