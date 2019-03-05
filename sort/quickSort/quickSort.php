<?php
/**
 * Created by PhpStorm.
 * User: kefirzhang
 * Date: 2019/3/5
 * Time: 16:30
 */

$unSortedData = range(1,10);
shuffle($unSortedData);
function quickSort($array)
{
    //基线条件 数组少于等于1
    if (count($array) <= 1) {
        return $array;
    }
    //递归条件 进行分割  小于数组 + 当前元素 + 大于数组
    // 随机获取一个元素
    $pickKey = array_rand($array);
    $pickValue = $array[$pickKey];
    // 获取比这个元素小的元素
    $smallerData = [];
    $biggerData = [];
    foreach ($array as $key => $value) {
        if ($key != $pickKey) {
            if ($value >= $pickValue) {
                $biggerData[] = $value;
            } else {
                $smallerData[] = $value;
            }
        }
    }
    return array_merge(quickSort($smallerData), [$pickValue], quickSort($biggerData));

}
$sortedData = quickSort($unSortedData);
print_r($sortedData);