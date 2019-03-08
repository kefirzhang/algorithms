简介：
选择排序SelectionSort
对于长度n的数组a来说，遍历n-1次，每次选出最大的放到当前选择域的最后（与最后一个交换）
这个跟冒泡前面有点类似，但是选择是用一个临时变量存储 比较 当前最大，而不是每次都交换

伪代码：
函数 选择排序 输入 一个数组名为arr
    获得数组长度 len
    i 从 1 到 len-1
        临时变量 tmpMaxIndex 0
        j 从 0 到 len-1-i
            如果 arr[j] < arr[j+1]
                tmpMaxIndex = j+1
            end
        end
    end

func selectionSort(arr)
{
    n = len(arr)
    for i from 1 to n-1 {
        maxIndex = 0 //指针
        for j from 0 to n-i
            if(arr[j] > arr[max])
                maxIndex = j
            end
        end
        swap(arr[maxIndex],arr[n-i])
    end
    return arr
}


符号
i∈[0,n-1]
    j∈[0,n-i]
        max(index,j)
    swap(index,n-i)



注意事项：
in place 排序 注意指针下标的交换  这个没有额外开辟内存

