简介：
希尔排序 看了好多遍还是没懂，真的是知识就是0跟1 的区别 知之为知之不知为不知。

伪代码：
函数 希尔排序 输入 数组arr
    n 为数组arr 长度
    step 初始化 为 (step|n/2)向下取整，直到 步长为1  | 或者用 斐波那切数列 1 1 2 3 5 8 13 .....
    // 用步长 为step 的划分成数组快 进行插入排序 这里纠结了很久
    i 从 step   到 n 增长步长 1
        j 从 step 到 0   减少步长 step
            swap(arr[j],arr[j-step])
        end
    end
end

function shellSort (arr)
    n = len(arr)
    for step = floor(n/2); step > 0; step = floor(step/2)
        for i = step; i < n; i++
            for j = i; (j - step) >= 0 && arr[j] < arr[j-step]; j -= step
                swap(arr[j],arr[j-step])
            end
        end
    end
注意事项：

有人 在第三个循环体这一步   用   j = j-step;j > 0; j -= step来做    我觉得  不太合思维方式

暂时没啥说的，这个现在具体性能上的差异还没搞懂 只是理解 会写 了

闲言碎语：
纸上得来终觉浅，须知此事要躬行

