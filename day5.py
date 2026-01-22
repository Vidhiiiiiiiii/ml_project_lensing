from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data=load_iris()

X=data.data
y=data.target

print("Dataset loaded")
print("Total samples:",len(X))
print("Feature names:",data.feature_names)
print("Target names:",data.target_names)
print("-"*40)

print("One data sample (numbers):",X[0])
print("Its correct label (number):",y[0])
print("Which means:",data.target_names[y[0]])
print("-"*40)

X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.2,random_state=42
)

print("Training samples:",len(X_train))
print("Testing samples:",len(X_test))
print("-"*40)

model=LogisticRegression(max_iter=200)

print("Model created (not trained yet)")
print("-"*40)


model.fit(X_train,y_train)

print("Model trained")
print("-"*40)

predictions=model.predict(X_test)

print("First 10 predictions:",predictions[:10])
print("First 10 actual labels:",y_test[:10])
print("-"*40)

accuracy=accuracy_score(y_test,predictions)
print("Accuracy:",accuracy)
print("-"*40 )

print("DONE: The model learned from data.")