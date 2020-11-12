# Git学习笔记

本文本旨在记录Git的学习笔记，便于快速查找常用的Git的命令。

## Git的诞生

Git的创建者是Linus，也就Linux系统的开发者。是一个用C语言编写的分布式版本控制系统。

为开源项目提供Git存储，如JQuery、PHP、Ruby等。

> **集中式VS分布式**
>
> 引自 *[廖雪峰Git教程](https://www.liaoxuefeng.com/wiki/896043488029600/896202780297248 "Click")*
>
> **集中式版本控制系统：**
>
> - CVS
> - SVN，*目前应用最广泛的集中式开发系统*
> - IBM收购Rational公司的ClearCase
> - 微软的VSS，集成在Visual Studio
>
> **分布式版本控制系统：**
>
> - Git，最快、最简单、最流行
> - Mercurial
> - Bazaar

## Git安装

***在W indows上安装* **

Git官网[下载](https://git-scm.com/downloads),按提示步骤安装。

与账户绑定：

`用户名`

```nginx
$ git config --global user.name "Name"
```

`邮箱`

```nginx
$ git config --global user.email "email"
```

`密码`

```nginx
$ git config --global user.password "****"
```

`git config`:用于获得和设置配置变量；**配置文件**可存储在三个不同位置：

> 1. /etc/gitconfig 文件：包含了适用于系统所有用户和所有库的值。如果你传递参数选项’--system’ 给 git config，它将明确的读和写这个文件。
> 2. ~/.gitconfig 文件 ：具体到自己的用户。你可以通过传递--global 选项使Git 读或写这个特定的文件。
> 3. 位于git目录的config文件 (也就是 .git/config) ：无论你当前在用的库是什么，特定指向该单一的库。每个级别重写前一个级别的值。因此，在.git/config中的值覆盖了在/etc/gitconfig中的同一个值。

`检查配置`

```nginx
$ git config --list
```

`查看特定值`

```nginx
$ git config "key"
```

`查看文本内容`

```nginx
$ cat file.txt
```



## 创建本地仓库/存储库

1. ![Repository_Creation](F:\Github\Git_pictures\Repository_Creation.png '进入目录>创建仓库文件夹>进入仓库>`$ pwd`查询目录')
2. 通过`git init`命令将当前目录设置成Git可以管理的仓库

```nginx
$ git init
Initialized empty Git repository in F:/Github/BBT_Training_Repository/.git/
```

仓库中会多一个`.git`的隐藏目录，*用于Git跟踪管理仓库*

### 把文件放入Git（分两步）

- `git add`把文件添加到仓库(*暂存*

```nginx
$ git add readme.txt
```

- `git commit`把文件提交给仓库（可以将暂存的文件一次提交当前分支）

```nginx
$ git commit -m "说明（例：提交一个readme测试文件）"
```

- `git status`查看仓库状态

![效果图](F:\Github\Git_pictures\git_status.png)

```nginx
$ git status
```

## Git基本语句

- **管理修改**

在工作区修改文件 > `git add`暂存 > 第二次修改 > `git add` >`git commit`提交两次修改合并的结果。每次修改，如果不用`git add`到暂存区，那就不会加入到`commit`中。

`git status`查看状态

`git diff HEAD -- file`查看工作区与仓库最新版本的区别。

- **撤销修改**

```nginx
$ git checkout -- (文件名)
```

回到最近一次`git add`或`git commit`后的状态

- **删除文件**

(`rm`命令)把工作区文件删除

```nginx
$ rm file
```

之后会有两种结果及对应操作。

***确定从仓库删除***`git rm file`

***删错需要恢复***`git checkout -- file`

- **版本回退**

  `git log`（*提交历史*）查看最近到最远的提交日志，结束需要按`Q`退出。可以使用参数`--pretty=oneline`一条线输出。

  ![git_log](F:\Github\Git_pictures\git_log.png)

  输出的结果有很大的十六进制表示数`ocf0a...`，称作`commit id`（版本号）。

- **回退操作**

  当前版本HEAD，上个版本HEAD^，上上个版本HEAD^^,……,前第一百个版本HEAD~100

  `git reset`命令回退到指定版本,

  `--mixed`  **不删除工作空间改动代码，撤销**`commit`，**并且撤销**`git add` 。这个为默认参数,`git reset --mixed HEAD^`和`git reset   HEAD^`效果是一样的.

  `--soft`   **不删除工作空间改动代码，撤销**`commit`，**不撤销**`git add` . 

  `--hard`  **删除工作空间改动代码，撤销**commit，**撤销**`git add`. 例

  ```nginx
  $ git reset --hard HEAD^
  ```

  值得注意的是Git的HEAD指针指向之前的版本时，会隐藏最新的版本,不过仍可以通过版本号回退。

  `git reflog`（*命令历史*）记录了每次的命令。

## 远程仓库

托管在Github上

1. 创建SSH key。用户目录下无`.ssh`目录或其下无`id_rsa`私钥和`id_rsa.pub`公钥文件需要在Git Bush中手动添加。

   ```nginx
   ssh-keygen -t rsa -C "email"
   ```

2. 本地仓库与远程仓库建立联系。

```nginx
$git remote add origin git@github.com:仓库地址
$git remote add origin <远程库地址>
$git remote add <远程库名字：Git默认为origin> <远程库地址>
```

3. 将本地库的内容推到远程库上。

```nginx
$git push -u origin master
```

`-u`参数，Git不但会把本地的`master`分支内容推送到远程新的`master`的分支，还会将他们关联起来。之后简化为

```nginx
$ git push <地址> <分支>
```

4. 从远程库克隆

```nginx
$ git clone <远端地址:与`git remote add`命令相似>
$ git pull <地址> <分支>
```

支持多种协议地址`ssh`相比`https`更快，默认的`git://`实用ssh。

## 分支管理

分支有助于团队分工，同时进行，提高效率，最后只需将分支合并来达到任务完整的目的。

- *创建与合并*

```nginx
$ git checkout -b <branch> #创建并切换分支
$ git switch -c <branch> #同上，新版
$ git branch <branch> #创建分支
$ git checkout <branch> #切换分支
$ git switch <branch> #同上，新版
$ git branch #查看当前分支
$ git merge <other branchs> #将其他分支合并到当前分支
$ git branch -d <branch> #删除分支
```

- 解决冲突

同时修改不同分支的内容，版本之间可能会发生冲突。

`get log`搭配一些参数可以看到分支的合并情况

```nginx
$ git log --graph --pretty=oneline --abbrev-commit
```

- *[分支管理拓展](https://www.liaoxuefeng.com/wiki/896043488029600/896954848507552 ''进一步拓展学习分支管理")*

## 自定义Git

> - 忽略某些文件时，需要编写`.gitignore`；
> - `.gitignore`文件本身要放到版本库里，并且可以对`.gitignore`做版本管理

