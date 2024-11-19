# 初始题库数据库获取

## 程序入口

- main.py

  -  请手动配置账号密码，防止同一账号请求过多导致的问题
    - username : Anorak	password : 123456
    - username : test          password : 135246
  - 可手动配置循环体内knowsid的range，以获取目标题库

- run_with_args.py

  - 此程序用于获取单个knowsid的题库
  - 使用方式：

  ```shell
  git clone https://github.com/Anorak2004/GetQuestionsDataset.git
  cd GetQuestionsDataset
  python ./run_with_args.py 200 #获取knowsid=200的所有题目
  ```

## 数据存储

- 相关数据将存储至data文件夹

## 团队开发

- 程序的开发请使用develop分支

```shell
git clone https://github.com/Anorak2004/GetQuestionsDataset.git -b develop
git push origin develop
```

