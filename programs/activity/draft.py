# echo 1 | sudo tee /proc/sys/vm/overcommit_memory

# import sklearn.neighbors
# N_NEIGHBORS = 10
# WEIGHTS = 'uniform'
# cknn = sklearn.neighbors.KNeighborsClassifier(n_neighbors=N_NEIGHBORS, weights=WEIGHTS)
# cknn.fit(X_train, Y_train)
# # Evaluate
# pred = cknn.predict(X_test)
# print('Test Set Performance: ' + str(sum(pred == Y_test)/len(Y_test)))