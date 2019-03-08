<?php
/**
 * Created by IntelliJ IDEA.
 * User: kefirzhang
 * Date: 2019/3/8
 * Time: 10:43
 */

function bubbleSort($arr)
{
    $len = count($arr);
    for ($i = 1; $i <= ($len-1); $i++) {
        for ($j = 0; $j <= ($len - $i - 1); $j++) {
            if($arr[$j] > $arr[$j+1]) {
                $tmp = $arr[$j+1];
                $arr[$j+1] = $arr[$j];
                $arr[$j] = $tmp;
            }
        }
    }
    return $arr;
}


$arr = [10,1,9,2,8,3,7,4,6,5];
print_r(bubbleSort($arr));