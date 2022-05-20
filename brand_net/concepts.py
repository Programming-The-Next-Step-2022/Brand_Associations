# IMPORT PACKAGES

# pip install --upgrade gensim
# pip install igraph
# pip install pycairo

import gensim.downloader as api
import igraph as ig


def find_concepts():
    """
    This definition takes brand name as an input (string) and returns a list of 10 most semantically
    similar concepts together with their cosine similarity score.
    (tuples in list format)

    For details of the pre-trained word embedding models, see:
    https://github.com/RaRe-Technologies/gensim-data
    """
    # Ask for brand
    global brand
    brand = input("Enter brand name: ")

    # Show all available pre-trained models in gensim library
    print('Choose a word embedding model from the following list: ')
    print(list(api.info()['models'].keys()))
    # Ask for model
    model_name = input("Enter model name: ")
    # Load pre-trained model from gensim library
    print('Loading...this may take up to few minutes')
    model = api.load(model_name)

    # Ask for amount of concepts
    n = int(input('Enter amount of related concepts: '))

    # Find concepts + cosine similarity
    global words
    print('Finding concepts...this may take a moment')
    words = model.most_similar(positive=[brand], topn=n)
    print(words)
    


def draw_net(words, brand):
    """
    This definition takes two inputs:
    1) a list of associations + edge weight (list of tuples)
    2) brand name

    As an output it creates an associative network
    where the brand is in the middle and the associations
    are linked to it with an edge (edge weights are still
    to be added + more details)
    """
    edge_list = []
    vertex_list = [brand]

    # Get edges
    for index in range(len(words)):
        vertex = (0, index+1)
        edge_list.append(vertex)
    g = ig.Graph(edge_list)

    # Get vertices
    for item in words:
        concept = item[0]
        vertex_list.append(concept)
    g.vs['name'] = vertex_list

    # Plot network
    ig.plot(g,
            vertex_label=g.vs['name'],
            vertex_color='yellow',
            vertex_size=40)
