from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.cluster import AgglomerativeClustering
from sklearn.mixture import GaussianMixture
from sklearn.cluster import SpectralClustering
from sklearn.cluster import MeanShift


def run_kmeans(data, n_clusters):
    model = KMeans(n_clusters=n_clusters, random_state=42)
    labels = model.fit_predict(data)
    return labels


def run_dbscan(data, eps, min_samples):
    model = DBSCAN(eps=eps, min_samples=min_samples)
    labels = model.fit_predict(data)
    return labels


def run_agglomerative(data, n_clusters):
    model = AgglomerativeClustering(n_clusters=n_clusters)
    labels = model.fit_predict(data)
    return labels


def run_gmm(data, n_clusters):
    model = GaussianMixture(n_components=n_clusters, random_state=42)
    labels = model.fit_predict(data)
    return labels


def run_spectral(data, n_clusters):
    model = SpectralClustering(n_clusters=n_clusters)
    labels = model.fit_predict(data)
    return labels


def run_meanshift(data):
    model = MeanShift()
    labels = model.fit_predict(data)
    return labels
