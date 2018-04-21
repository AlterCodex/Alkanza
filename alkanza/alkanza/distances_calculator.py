import numpy
import math



class Distance_Calculator():

    def calculate_distances(self,origin_position,positions):
        return list(self.calculate_distance(origin_position,x)for x in positions)
        
    def calculate_distance(self,origin,dest):
        lat1, lon1 = origin['lat'],origin['lon']
        lat2, lon2 = dest['lat'],dest['lon']
        radius = 6371  # km
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = (math.sin(dlat / 2) * math.sin(dlat / 2) +math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2))
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return radius * c

    def unbalanced_distance(self,distances):
        print(distances)
        B=list(set(range(1,len(distances)+1))-set(distances))
        result= sum(abs(x-y) for x in B for y in  distances)
        return result

