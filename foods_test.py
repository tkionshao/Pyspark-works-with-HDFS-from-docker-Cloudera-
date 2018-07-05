from pyspark import SparkContext
from math import cos
def latAndLon_to_int(x):
    x[0][6] = float(x[0][6])
    x[0][7] = float(x[0][7])
    return x

# Latitude: 1 deg = 110.574 km
# Longitude: 1 deg = 111.320*cos(latitude) km

def stat_code_compute(x):
    scale_km = 0.5
    lat = x[0][6]
    lon = x[0][7]
    lat_to_km = lat*110.574
    lon_to_km = lon*(111.320*cos(lat))

    state_code_x = int(lat_to_km//scale_km)
    state_code_y = int(lon_to_km//scale_km)
    state_code = str(state_code_x)+str(state_code_y)
    return (x[0],state_code)

def printByGroup(x):
    for i in x:
        count = 0
        for j in i:
            count += 1
        print(count)

if __name__ == "__main__":
    sc = SparkContext()
    RDD = sc.textFile("hdfs://localhost:8020/user/cloudera/foods/input")
    # RDD.take(10)
    header = RDD.first()

    header_list = RDD.first().split(',')
    lon_index = header_list.index('lon')
    lat_index = header_list.index('lat')

    noHeaderRDD = RDD.filter(lambda line: line != header)

    row = noHeaderRDD.map(lambda x: x.split(','))
    # row.take(10)

    col_count = row.map(lambda x:len(x))
    # col_count.take(100)

    add_count = row.map(lambda x: (x,str(len(x))))
    # add_count.collect()

    filter_missing_row = add_count.filter(lambda x: int(x[1]) == 8)
    # filter_missing_row.first()
    # filter_missing_row.collect()
    # filter_missing_row.count()

    latAndLon_is_int = filter_missing_row.map(latAndLon_to_int)
    # latAndLon_is_int.first()
    # latAndLon_is_int.collect()

    # Trying
    tmp1 = latAndLon_is_int.map(stat_code_compute)
    tmp1.take(10)
    tmp2 = tmp1.groupBy(lambda x:x[1])

    result = latAndLon_is_int.map(stat_code_compute)
    # result.first()
    # result.groupBy(lambda x:x[1]).take(10)
    res_g = result.groupBy(lambda x:x[1])
    result.saveAsTextFile("hdfs://localhost:8020/user/cloudera/foods/output")

    # Read Ouput
    # f = sc.textFile('hdfs://localhost:8020/user/cloudera/foods/output')
    # f.take(10)

    # linesRCPheader = linesRCP.first() 
    # noHeaderRDD = linesRCP.subtract(linesRCPheader)
    # noHeaderRDD = linesRCP.zipWithIndex().filter(lambda (row,index): index > 1).keys()
