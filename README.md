---
date: 2024-08-06 10:45:54
created: 2024-08-06 10:36:46
categories:
- PV / プログラミング / python
---

## anaconda手順

  

  

  

  

## anacondaの環境を0から構築する場合

  

  

  

### 1\. 特定のPythonバージョンを指定して仮想環境を作成

Anaconda Promptを開き、以下のコマンドを実行して仮想環境を作成します。ここでは、Python 3.8を例にしていますが、必要に応じて他のバージョンに変更できます。

```
conda create --name myenv python=3.12.4
```

  

  

### 2\. 仮想環境をアクティブにする

仮想環境をアクティブにするには、以下のコマンドを実行します。

※プロジェクト名部分はプロジェクトごとに代わる

```
conda activate MathProject
```

  

### 3\. 必要なパッケージをインストール

仮想環境をアクティブにした状態で、必要なパッケージをインストールします。例えば、SymPy、NumPy、SciPyをインストールする場合：

```
conda install sympy numpy scipy
```

  

  

### 5\. 環境の共有

`environment.yml`ファイルを他の人と共有します。メール、クラウドストレージ、GitHubなど、好きな方法で共有できます。

### 6\. 共有された環境をインポート

他の人が共有された`environment.yml`ファイルを使って仮想環境をインポートする手順です。

1. 共有された`environment.yml`ファイルを取得します。
2. Anaconda Promptを開き、以下のコマンドを実行して環境をインポートします。

  

```
conda env create -f environment.yml
```

  

このコマンドにより、`environment.yml`ファイルに基づいて新しい環境が作成されます。

  

  

githubからの場合、以下以降のみでOK！

  

### 6\. 共有された環境をインポート

他の人が共有された`environment.yml`ファイルを使って仮想環境をインポートする手順です。

1. 共有された`environment.yml`ファイルを取得します。
2. Anaconda Promptを開き、以下のコマンドを実行して環境をインポートします。

```
conda env create -f environment.yml
```

このコマンドにより、`environment.yml`ファイルに基づいて新しい環境が作成されます。

  

  

  

  

### 7\. 仮想環境をアクティブにする

インポートした仮想環境をアクティブにするには、以下のコマンドを実行します。

  

```
conda activate MathProject
```

  

ここで、`myenv`は`environment.yml`ファイルに記載されている環境の名前です。

### まとめ

Anacondaを使用して特定のPythonバージョンを指定した仮想環境を作成し、それを他の人と共有する手順は以下の通りです：

1. 特定のPythonバージョンを指定して仮想環境を作成する。
2. 必要なパッケージをインストールする。
3. 環境をエクスポートして`environment.yml`ファイルを作成する。
4. `environment.yml`ファイルを共有する。
5. 他の人がそのファイルを使って環境をインポートする。

この手順により、複数のユーザーが同じ環境を簡単に再現できるようになります。


### 数式のつかいかた及びjupiternote


Jupyter Notebookを使用する場合、以下のコマンドを実行して必要なパッケージをインストールします。



```
pip install jupyter sympy
```


その後、以下のコマンドでJupyter Notebookを起動します。

```
jupyter notebook
```


  

1. `question1` の計算:
   $$
   3^{(-6 + 3 + 4)} = 3^1 = 3
   $$