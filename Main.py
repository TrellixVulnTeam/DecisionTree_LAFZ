import math

def readExel(exelname):
    import xlrd

    ExcelFileName= exelname
    workbook = xlrd.open_workbook(ExcelFileName)
    worksheet = workbook.sheet_by_name("Data")

    num_rows = worksheet.nrows  #Number of Rows
    num_cols = worksheet.ncols  #Number of Columns

    result_data =[]
    for curr_row in range(2,num_rows): # read except header
        row_data = []

        for curr_col in range(1, num_cols): # read except ID
            data = worksheet.cell_value(curr_row, curr_col) # Read the data in the current cell
            # print(data)
            row_data.append(data)

        result_data.append(row_data)
    print("read done")
    # print(result_data[0].__len__())
    return result_data

def I(n):
    n=list(n)
    info=0
    for i in n :
        if(i==0):
            info=0
            break
        pi=i/sum(n)
        info-=pi*math.log(pi,2)

    return info
data = readExel('data.xls')

min = list(map(min, zip(*data)))
max = list(map(max, zip(*data)))

print(max)
print(min)

ans = []
for i in data:
    ans.append(int(i.pop(i.__len__() - 1)))

infoE = I([ans.count(0),ans.count(1)])

sd=[]
for i in range(max.__len__()):
    tmp=(max[i]-min[i])/3
    sd.append(tmp)
print(sd)

infoN=[]
# sum(i > 0 for i in tmp)
for i in range(data[0].__len__()):
    tmp = []
    for j in range(data.__len__()):
        tmp.append(data[j][i])

    pn=[[0,0],[0,0],[0,0]]
    for j in range(tmp.__len__()):
        for k in range(pn.__len__()):
            if((min[i]+(k*sd[i]))<=tmp[j]<(min[i]+(k+1)*sd[i])):
                if(ans[j]==1):
                    pn[k][0]+=1
                elif(ans[j]==0):
                    pn[k][1]+=1
        if(tmp[j]==max[i]):
            if(ans[j]==1):
                pn[k][0]+=1
            elif(ans[j]==0):
                pn[k][1]+=1
    # print(pn)
    # print(i,sum(pn[0])+sum(pn[1])+sum(pn[2]))
    #
    # break
    attr=0
    for j in range(pn.__len__()):

        if(pn[j][0]+pn[j][1]>0):
            attr+= ((pn[j][0]+pn[j][1])/data.__len__())*I(pn[j])
    infoN.append(attr)

print(infoE)
print(infoN)
