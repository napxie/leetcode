from typing import List
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        citiesA = {path[0] for path in paths}
        return next(path[1] for path in paths if path[1] not in citiesA)
    def destCity(self, paths: List[List[str]]) -> str:
        return (set((city:=list(zip(*paths)))[1]) - set(city[0])).pop()


