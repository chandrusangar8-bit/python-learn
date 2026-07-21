a={"name":"chand"}
print(a)
print(a["name"])


#keys and values print
b={
    "name":"chand",
    "age":"21",
    "dpt":"IT",
    "service":["backend developer","fullstack developer","senior software developer","ceo"]
    }
print(b.keys())
print(b.values())


#update dictionary
c={
    "name":"chand",
    "age":"21",
    "dpt":"IT",
    "service":["backend developer","fullstack developer","senior software developer","ceo"]
    }
c.update({"rollno":13})
c["age"]=20
c["color"]="blue"
print(c)


#dlt dict
d={
    "name":"chand",
    "age":"21",
    "dpt":"IT",
    "domain":["backend developer","fullstack developer"]
    }
d.pop("domain")
del d["age"]
print(d)


#clear term
f={
    "name":"chand",
    "age":"21",
    "dpt":"IT",
    "domain":["backend developer","fullstack developer"]
    }
f.clear()
print(f)

#whole term dlt
e={
    "name":"chand",
    "age":"21",
    "dpt":"IT",
    "domain":["backend developer","fullstack developer"]
    }
del e
print(e)





