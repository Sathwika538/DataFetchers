from enum import auto
import imp
from operator import mod
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import io
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA

def std_data(df):
    df = df._get_numeric_data()
    return StandardScaler().fit_transform(df)

# def tsne(data, labels):
#     model = TSNE(n_components=2, random_state=0, perplexity=50)
#     tsne_data = model.fit_transform(data)
#     df = pd.DataFrame(tsne_data, columns=["feature 1", "feature 2"])
#     df["labels"] = labels
#     return df
def tsne(data, labels):
    model = TSNE(n_components=2, random_state=0, perplexity=50)
    tsne_data = model.fit_transform(data)
    dic = {"feature 1": tsne_data.T[0], "feature 2": tsne_data.T[1]}
    df = pd.DataFrame(dic)
    df["labels"] = labels
    return df

def do_plot(df, f1, f2, classes):
    f, ax = plt.subplots(figsize=(11, 9))

    sns.scatterplot(data=df, x=f1, y=f2, hue=classes, legend=auto)

    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image


def process(df, label):
  labels = df[label]
  df = df.drop(label, axis=1)
  df = df._get_numeric_data()
  cols = df.columns
  if 'Unnamed: 0' in cols:
    df =df.drop("Unnamed: 0",axis=1)
    
  columns = df.columns
  means = [df[column].mean() for column in columns]
  for column, mean in zip(columns, means):
    df[column] = df[column].fillna(mean)
  df["labels"] = labels 
  return df

def num_cols(df, label):
    
    df = df._get_numeric_data()
    
    cols = df.columns
    if 'Unnamed: 0' in cols:
        df =df.drop("Unnamed: 0",axis=1)
    
    
    columns = df.columns
    means = [df[column].mean() for column in columns]
    for column, mean in zip(columns, means):
        df[column] = df[column].fillna(mean)
    return [_ for _  in list(df.columns) if _ != label]

def do_hist(df, feature, classes):

    f, ax = plt.subplots(figsize=(11, 9))

    sns.histplot(data=df, x=feature, hue=classes)

    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image


def do_box(df, feature, classes):

    f, ax = plt.subplots(figsize=(11, 9))

    sns.boxplot(data=df, x=classes, y=feature)

    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image


def do_pdf(df, feature, classes):

    f, ax = plt.subplots(figsize=(11, 9))

    sns.kdeplot(data=df, x=feature, hue=classes)

    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image

def do_cdf(df, feature,  classes):


    f, ax = plt.subplots(figsize=(11, 9))


   
    sns.ecdfplot(data=df, x=feature, hue=classes)
 
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image

def do_violin(df, feature, classes):

    f, ax = plt.subplots(figsize=(11, 9))

    sns.violinplot(data=df, x=classes, y=feature)

    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image

def do_join(df, f1, f2, classes):
    f, ax = plt.subplots(figsize=(11, 9))

    sns.kdeplot(data=df, x=f1, y=f2, hue=classes)

    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image


def pca(data, labels):
    model = PCA()
    model.n_components = 2
    pca_data = model.fit_transform(data)
    dic = {"feature 1": pca_data.T[0], "feature 2": pca_data.T[1]}
    df = pd.DataFrame(dic)
    df["labels"] = labels
    return df