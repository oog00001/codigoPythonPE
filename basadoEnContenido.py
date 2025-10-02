import cornac
from cornac.datasets import movielens
from cornac.data import Reader
from cornac.data import UserItemFeatureDataset
from cornac.models import CBMF
from cornac.eval_methods import RatioSplit

def filtro_basado_en_contenido(nombre_usuario):
    # Cargo MovieLens 1M
    data = movielens.load_feedback(fmt="UIR", variant="1M", reader=Reader())

