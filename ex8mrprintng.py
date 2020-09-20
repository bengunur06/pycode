# - *- coding: utf- 8 - *-

formatter = "%r %r %r"

print formatter % (1,2,3)
print formatter % ("bir","iki", "uç" )
print formatter % (True,False,True)
print formatter % (formatter, formatter , formatter)
print formatter % (
    "bir kedi varmış",
    "2 ye kadar sayarmış ",
    " bir iki "
)

# with the %r strings like ü doesnt print well because it prints raw data