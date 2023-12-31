# -*- coding: utf-8 -*-
"""Louvain.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/163vZnGlxPfKH_unfIvd9a8HicaGbIxmz
"""

#Installing louvain
!pip install louvain

#Principal Component Analysis of the adata
sc.pp.pca(adata)
#compute the neighborhood graph of cells using the PCA representation of the adata matrix
sc.pp.neighbors(adata)
#embedding the graph in two dimensions using UMAP
sc.tl.umap(adata)
#Plot the clusters, Louvain clustering directly clusters the neighborhood graph of cells.
sc.tl.louvain(adata)

#Plotting the clusters of Louvain Algorithms
plt.rcParams["figure.figsize"] = (4, 4)
sc.pl.umap(adata, color=["total_counts", "n_genes_by_counts", "louvain"], wspace=0.4)

#With rc_context plotting the clustering of cells using Louvain
with rc_context({'figure.figsize': (5, 5)}):
    sc.pl.umap(adata, color='louvain', add_outline=True, legend_loc='on data',
               legend_fontsize=12, legend_fontoutline=2,frameon=False,
               title='clustering of cells', palette='Set1')

#Creating new adata with the louvain clustering for marker genes
adata3=adata

#Using the wilcoxon method and leiden finding out the marker genes from adata
sc.tl.rank_genes_groups(adata3, 'louvain', method='wilcoxon')

#Coverting the dataframe with matrices to find out the marker genes
resultsLO = adata.uns['rank_genes_groups']
('0', '1', '2', '3', '4')

outLO = np.array([[0,0,0,0,0]])
for group in resultsLO['names'].dtype.names:
    outLO = np.vstack((outLO, np.vstack((resultsLO['names'][group],
                                     resultsLO['scores'][group],
                                     resultsLO['pvals_adj'][group],
                                     resultsLO['logfoldchanges'][group],
                                     np.array([group] * len(resultsLO['names'][group])).astype('object'))).T))



markersLO = pd.DataFrame(outLO[1:], columns = ['Gene', 'scores', 'pval_adj', 'lfc', 'cluster'])

markersLO = markersLO[(markersLO.pval_adj < 0.05) & (abs(markersLO.lfc) > 1)]

#Printing the marker genes from louvain
markersLO

#Checking the total number of marker genes per group using Louvain
pd.DataFrame(adata3.uns['rank_genes_groups']['names']).head(20000)