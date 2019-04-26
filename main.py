data = [1, 10, 3, 4, 5, 15, 7,123123,12,-2]
current_clusterr = {}
for i in data:
    current_clusterr[str(i)] = (i, i)


def compute_pairwise_distances(data):
    result = []
    done = []
    for i in data.keys():
        for j in data.keys():
            if i != j:
                if [i, j] not in done:
                    dist = min(abs(data[i][0] - data[j][0]), abs(data[i][0] - data[j][1]), abs(data[i][1] - data[j][0]),
                               abs(data[i][1] - data[j][1]))
                    result.append((dist, [i, j]))
                    done.append([j, i])
    result.sort()
    return result


def clustering(current_cluster, k):
    while len(current_cluster) > k:
        new_cluster = []
        distances = compute_pairwise_distances(current_cluster)
        minim = distances[0][0]
        for i in range(len(distances)):
            if distances[i][0] == minim:
                for j in distances[i][1]:
                    if j not in new_cluster:
                        new_cluster.append(j)
                        del current_cluster[str(j)]
            else:
                break

        print("Merged in same cluster =", new_cluster)
        new_key = ','.join(new_cluster)

        t = []
        for p in new_key.split(','):
            t.append(int(p))


        current_cluster[new_key] = (min(t), max(t))
    return current_cluster;


done = clustering(current_clusterr, 1)
print(done)
