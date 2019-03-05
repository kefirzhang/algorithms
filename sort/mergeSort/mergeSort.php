<?php
/**
 * Created by PhpStorm.
 * User: kefirzhang
 * Date: 2019/3/5
 * Time: 16:30
 */
$unSortedData = range(1, 10);
shuffle($unSortedData);
function mergeSort($array)
{

    //基线条件 数组少于等于1
    if (count($array) <= 1) {
        return $array;
    }
    //递归条件
    // 拆分两部分
    $num = ceil(count($array) / 2);
    $chunkData = array_chunk($array, $num);
    $left = mergeSort($chunkData[0]);
    $right = mergeSort($chunkData[1]);
    // 并 重新对排好序的左半部分和排好序的右半部分排序
    $sortedData = [];
    while (count($left) > 0 && count($right) > 0) {
        if ($left[0] <= $right[0]) {
            $sortedData[] = array_shift($left);
        } else {
            $sortedData[] = array_shift($right);
        }
    }
    //追加 剩下的
    if (count($left) > 0) {
        $sortedData = array_merge($sortedData, $left);
    }
    if (count($right) > 0) {
        $sortedData = array_merge($sortedData, $right);
    }
    return $sortedData;
}

$sortedData = mergeSort($unSortedData);
print_r($sortedData);
