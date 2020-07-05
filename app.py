from flask import Flask, render_template, request, redirect, url_for
from main import *

app = Flask("SMRT")


@app.route("/")
def my_home():
    return render_template("index.html", stations=stations)


@app.route("/link-nodes")
def link_nodes():
    return render_template("link-nodes.html", stations=stations)


@app.route("/add-link-to-adjacency-list", methods=['GET'])
def add_link_to_adjacency_list():
    station1 = request.args['station1']
    station2 = request.args['station2']
    add_route(station1, station2)
    return redirect(url_for('my_home'))


@app.route("/de-link", methods=['GET'])
def de_link():
    return render_template("delink.html", adjacency_list=get_adjacency_list(), stations=stations)


@app.route("/remove-from-adjacency-list", methods=['GET'])
def remove_from_adjacency_list():
    source = request.args['source']
    destination = request.args['destination']
    delink(source, destination)
    return redirect(url_for('adjacency_list'))


@app.route("/print-traversal", methods=['GET'])
def my_traversal():
    source = request.args['source']
    traversal_path = traversal(source)
    my_path_string = traversal_path[0]
    for node in traversal_path[1:]:
        my_path_string += ' >>> {}'.format(node)
    return render_template('print-path.html', paths=my_path_string, title='Graph Traversal from {}'.format(source))


@app.route("/adjacency-list")
def adjacency_list():
    return render_template("adjacency.html", adjacency_list=get_adjacency_list(), stations=stations)


@app.route("/shortest-path", methods=['GET'])
def my_shortest_path():
    return render_template("my-shortest-path.html", stations=stations)


@app.route("/print-shortest-path", methods=['GET'])
def print_shortest_path():
    station1 = request.args['station1']
    station2 = request.args['station2']
    paths = djikstra(station1, station2)
    return render_template('print-path.html', paths=paths, title='Shortest Paths from {} to {}'.format(station1, station2))


@app.route("/traversal", methods=['GET'])
def traverse():
    return render_template("traverse.html", stations=stations)


if __name__ == "__main__":
    app.run("localhost")