#!/usr/bin/env python3

"""
Script to compare the frequency distributions of one query result in two partitions.
"""

# ========================
# Imports
# ========================

import os
import glob
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import pygal
from os.path import join
from pygal.style import BlueStyle


# ========================
# Files and folders
# ========================

AbsFreqsFiles = join("patterns_all-titles", "*.csv") # results for each query across all titles
LabelListFile = join("label-list.csv")
TokenCountsFile = "idnos-tokens.csv" # text length for each title (by identifier)
Partition1 = ["tc0649", "tc0651", "tc0653", "tc0654", "tc0655", "tc0656", "tc0657", "tc0658", "tc0659", "tc0661", "tc0664"]  # Racine
Partition2 = ["tc0093", "tc0094", "tc0096", "tc0098", "tc0101", "tc0113", "tc0114", "tc0115", "tc0116", "tc0117", "tc0118", "tc0163", "tc0165", "tc0183", "tc0189", "tc0190", "tc0193", "tc0196", "tc0200", "tc0203", "tc0204", "tc0206", "tc0207", "tc0219", "tc0221", "tc0222", "tc0224", "tc0225", "tc0226", "tc0227", "tc0628", "tc0629", "tc0630", "tc0632", "tc0636", "tc0637", "tc0645", "tc0648"]  # contemporaries / proches
Resultsfile = join("racine-vs-contemporaries_statistics.tsv")


# ========================
# Functions
# ========================


def get_TokenCounts(TokenCountsFile): 
    with open(TokenCountsFile, "r", encoding="UTF-8") as infile: 
        TokenCounts = pd.read_csv(TokenCountsFile, sep=",")
        TokenCounts = TokenCounts.iloc[:,1:]
        return TokenCounts


def prepare_data(AbsFreqsFile, TokenCounts, patternID):
    with open(AbsFreqsFile, "r", encoding="UTF-8") as infile: 
        AbsFreqs = pd.read_csv(infile, sep="\t")
        AbsFreqs = AbsFreqs.iloc[:,2:].sum(axis=0)
        RelFreqs = AbsFreqs / TokenCounts * 10000
        return RelFreqs


def split_data(RelFreqs, Partition1, Partition2): 
    RelFreqsP1 = RelFreqs[Partition1]
    RelFreqsP2 = RelFreqs[Partition2] 
    P1 = RelFreqsP1.iloc[0].values.tolist()
    P2 = RelFreqsP2.iloc[0].values.tolist()
    return P1, P2


def get_stats(P1, P2): 
    MeanP1, MeanP2 = np.mean(P1), np.mean(P2)
    MedianP1, MedianP2 = np.median(P1), np.median(P2)
    MeanRatio12 = (MeanP1+0.00000000001)/(MeanP2+0.00000000001)
    MedianRatio12 = (MedianP1+0.00000000001)/(MedianP2+0.00000000001)
    MeanRatioAbs = abs(MeanRatio12-1)
    #print(MeanRatio12, MedianRatio12, MeanRatioAbs)
    return MeanP1, MeanP2, MedianP1, MedianP2, MeanRatio12, MedianRatio12, MeanRatioAbs


def get_significance(P1, P2): 
    """
    # Welch t-test: http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.ttest_ind.html
    # Wilcoxon's rank sum test: http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.ranksums.html
    # Kolmogorov-Smirnov test: http://docs.scipy.org/doc/scipy-0.16.1/reference/generated/scipy.stats.ks_2samp.html
    """
    Welch = stats.ttest_ind(P1, P2, equal_var=False)[1]
    Wilcoxon = stats.ranksums(P1, P2)[1]
    Kolmogorov = stats.ks_2samp(P1, P2)[1]
    return Welch, Wilcoxon, Kolmogorov


def save_results(AllResults, Resultsfile): 
    Headers = ["patternID", "MeanP1", "MeanP2", "MeanRatio12", "MeanRatioAbs", "MedianP1", "MedianP2", "MedianRatio12", "Welch", "Wilcoxon", "Kolmogorov"]
    AllResults = pd.DataFrame(AllResults).T
    AllResults.columns = Headers
    print(AllResults.head())
    with open(Resultsfile, "w", encoding="UTF-8") as outfile: 
        AllResults.to_csv(outfile, sep="\t")
    return AllResults


def get_labels(LabelListFile): 
    with open(LabelListFile, "r", encoding="UTF-8") as infile: 
        LabelList = infile.read().split("\n")
        LabelDict = {}
        for item in LabelList:
            if len(item.split(",")) == 2: 
                LabelDict[item.split(",")[0]] = item.split(",")[1]            
        #print(LabelDict)
        return LabelDict


def make_barchart(AllResults, LabelDict):
    GraphFileName = "racine-vs-contemporaries_overview"
    DataTable = AllResults.sort_values("MeanRatio12", ascending=False)
    #print(DataTable)
    Items = DataTable.loc[:,"patternID"].values.tolist()
    Ratio12 = DataTable.loc[:,"MeanRatio12"].values.tolist()
    Wilcoxon = DataTable.loc[:,"Wilcoxon"].values.tolist()
    #print(Items)
    #print(Wilcoxon[0])
    bar = pygal.Bar(show_legend=False, x_label_rotation=295, show_labels=True, style = BlueStyle)
    
    bar.title = "Comparative prevalence of stylistic devices"
    bar.x_title = "Stylistic devices"
    bar.y_title = "Ratio of means (Racine / Contemporaries)"
    #bar.x_labels = Items
    #bar.add("Ratio", Ratio12, rounded_bars=2)
    for i in range(0,len(Items)):
        #print(Ratio12[i])
        #print(Labels[i])
        if Wilcoxon[i] < 0.05: 
            color = "DarkGreen"
        else:
            color = "PowderBlue"
        Ratio12display = float("{:01.4f}".format(Ratio12[i]))
        LabelDisplay = LabelDict[Items[i]]
        print(LabelDisplay) 
        #print(Ratio12display)
        bar.add(Items[i], [{"value" : Ratio12display, "color" : color, "label" : LabelDisplay}], rounded_bars=3)
        bar.render_to_file(GraphFileName+"-MeanRatio.svg")



# ========================
# Main
# ========================

def main(AbsFreqsFiles, TokenCountsFile, Partition1, Partition2, Resultsfile): 
    print("Starting!")
    AllResults = {}
    TokenCounts = get_TokenCounts(TokenCountsFile)
    for AbsFreqsFile in glob.glob(AbsFreqsFiles):
        patternID,ext = os.path.basename(AbsFreqsFile).split(".")
        RelFreqs = prepare_data(AbsFreqsFile, TokenCounts, patternID)
        P1,P2 = split_data(RelFreqs, Partition1, Partition2)
        MeanP1, MeanP2, MedianP1, MedianP2, MeanRatio12, MedianRatio12, MeanRatioAbs = get_stats(P1, P2)
        Welch, Wilcoxon, Kolmogorov = get_significance(P1, P2)
        AllResults[patternID] = [patternID, MeanP1, MeanP2, MeanRatio12, MeanRatioAbs, MedianP1, MedianP2, MedianRatio12, Welch, Wilcoxon, Kolmogorov]
    AllResults = save_results(AllResults, Resultsfile)
    LabelDict = get_labels(LabelListFile)
    make_barchart(AllResults, LabelDict)        

main(AbsFreqsFiles, TokenCountsFile, Partition1, Partition2, Resultsfile)    


