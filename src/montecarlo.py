import numpy as np
from typing import Literal
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


SIGMA_LEVEL:int=6

def validate_generate_variable(low:float, high:float, n_samples:int, distribution:str)->None:
    if low>high:
        raise ValueError("low should be equal or lower than high")
    
    if type(n_samples)!=int:
        raise TypeError("n samples must be an integer >0")
    
    if distribution not in ["uniform","normal","triangular"]:
        raise ValueError(f"{distribution} is not a valid distribution")


def generate_variable(low:float,
                      high:float,
                      n_samples:int,
                      distribution:str) -> np.ndarray:

    validate_generate_variable(low,high,n_samples, distribution)
    
    if distribution=="uniform":
        return np.random.uniform(low,high,n_samples)
    elif distribution=="normal":
        avg = (high+low)/2
        stdv = (high-low)/SIGMA_LEVEL
        return np.random.normal(loc=avg,scale=stdv,size=n_samples)
    else:
        return np.random.triangular(left=low, mode=(high+low)/2, right=high, size=n_samples)




def generate_histogram(data:np.ndarray, title:str, bins:int=16, save:bool=False) ->Figure:
    fig, ax = plt.subplots()
    ax.hist(data, bins=bins, edgecolor='black')
    ax.set_title(title)
    ax.set_xlabel("valor")
    ax.set_ylabel("frecuencia")
    # plt.close(fig)  # Prevents automatic display in some environments
    print(type(fig))
    print(type(ax))
    if save:
        fig.savefig(f"img/{title}_hist.png")
    return fig


if __name__=="__main__":
    n:int = 100
    var_1 = generate_variable(-1,1,n,"uniform")
    var_2 = generate_variable(-10,10,n,"uniform")

    res = var_1 * var_2
    fig = generate_histogram(res,"holi")
    fig.savefig("img/histogram.png")
    