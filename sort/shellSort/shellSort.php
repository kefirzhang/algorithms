<?php
/**
 * Created by IntelliJ IDEA.
 * User: kefirzhang
 * Date: 2019/3/15
 * Time: 13:19
 */


function shellSort($arr)
{
    $n = count($arr);
    for ($gap = floor($n / 2); $gap > 0; $gap = floor($gap / 2)) {
        //对指定步长的 划分区块 数组
        for ($i = $gap; $i < $n; $i++) {
            for ($j = $i; ($j - $gap) >= 0 && $arr[$j] < $arr[$j - $gap]; $j -= $gap) {
                $tmp = $arr[$j - $gap];
                $arr[$j - $gap] = $arr[$j];
                $arr[$j] = $tmp;
            }
        }
    }
    return $arr;
}
$arr = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5];
print_r(shellSort($arr));