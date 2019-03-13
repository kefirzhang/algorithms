简介：
打牌中炒常用的就是这种排序，把一个元素放到已经排序好的序列中，后面的整体右移一位
伪代码：
函数 插入排序 输入 一个数组名为arr
    获得数组长度 len
    i 从 1 到 len-1
    j 从 i 到 0
        如果 arr[j] < arr[j-1]
            swap(arr[j],arr[j-1])
        end
     end



func insertionSort(arr) {
    len = len(arr)
    for i from 0 to len-1
        for j from i to 0
            if (arr[j] < arr[j-1])
                swap(arr[j],arr[j-1])
            end
        end
    end
    return
}


注意事项：

