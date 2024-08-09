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
conda env export > environment.yml
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
以下を自分の仮想環境上にインストールして、jupiterに取り込む
```
python -m ipykernel install --user --name=Mathproject --display-name "Python (Mathproject)"
```



1. `question1` の計算:
   $$
   3^{(-6 + 3 + 4)} = 3^1 = 3
   $$



# 数式一覧

## expand (展開)

```
expr = (x + y) ** 2
expanded_expr = expand(expr)
```

### 結果

>$$
x^2 + 2xy + y^2
$$

## factor(因数分解)
```
expr = (x + y) ** 2
expanded_expr = expand(expr)
factored_expr = factor(expanded_expr)
```

### 結果
>$$
(x+y)^2 
$$


## Eq(方程式が等しい場合に利用する)
第一引数に式、第二引数に答え

```
equation = Eq(x ** 2 + 2 * x + 1, 0)

```

### 結果
>$$
x^2 +2xy+y^2 =0
$$

## solve(方程式の解を求める)
```
# 方程式の解法
equation = Eq(x ** 2 + 2 * x + 1, 0)
solutions = solve(equation, x)
```
### 結果
>$$
[-1]
$$

## diff(微分)
```
f = x ** 2 + x
derivative = diff(f, x)
```
### 結果

>$$
2x + 1
$$

## integrate(積分)

```
f = x ** 2 + x
integral = integrate(f, (x, 0, 1))
# 積分計算
integral_result = integrate(expression, x)
```
### 結果
>$$
6/5
$$

## 積分備考 

### $$ 関数 𝑓(x) = x^2+x を xの範囲[0,1]の範囲で積分する。$$

1-1.関数の定義 

>$$f(x) = x^2 +x  $$


1-2不定積分(原始関数)を求める
→各項の次数を関数に入れ込む今回の式ではC＝０なので考えなくてよい。
>$$
∫x^ndx= \frac{x^{n+1}}{n+1}+C
$$

各項の不定積分を考える。

>$$x^2 $$
↓↓
>$$
∫x^2dx = \frac{x^3}{3}
$$

>$$x $$
↓↓
>$$∫xdx = \frac{x^2}{2} $$


1-3定積分の計算

上記の不定積分を用いて、指定された範囲 [0,1] で積分を計算します。
積分範囲内での面積を求めるために、上限と下限に不定積分を代入し、
その差を計算する。

>$$
= \left(\frac{x^3}{3} + \frac{x^2}{2}\right) \Bigg|_0^1
$$
単純に、[0,1]を代入して、合成するだけ。