import requests

# https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_name=guishudi&query=1391381+%E6%89%8B%E6%9C%BA%E5%8F%B7%E6%AE%B5
res = requests.get("http://www.baidu.com")
savefile = open("baidu.html","w")
savefile.write(res.content)
savefile.close()
