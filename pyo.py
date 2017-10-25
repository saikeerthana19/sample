from sklearn import tree
a=[[100,110],[260,20],[100,100],[250,10]]
b=[0,1,0,1]
clf=tree.DecisionTreeClassifier()
clf=clf.fit(a,b)
print clf.predict([[100,120]])

