<?php
/**
 * Created by IntelliJ IDEA.
 * User: kefirzhang
 * Date: 2019/3/13
 * Time: 13:10
 */

function insertionSort($arr)
{
    $len = count($arr);
    for($i = 0; $i < $len;$i++){
        for($j = $i; $j > 0 && $arr[$j] < $arr[$j-1] ; $j--) {
            $tmp = $arr[$j-1];
            $arr[$j-1] = $arr[$j];
            $arr[$j] = $tmp;
        }
    }
    return $arr;
}

$arr = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5];
print_r(insertionSort($arr));
