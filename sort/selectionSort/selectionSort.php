<?php
/**
 * Created by IntelliJ IDEA.
 * User: kefirzhang
 * Date: 2019/3/8
 * Time: 15:48
 */

function selectionSort($arr)
{
    $len = count($arr);
    for ($i = 1; $i <= ($len - 1); $i++) {
        $maxIndex = 0;
        for ($j = 1; $j <= ($len - $i); $j++) {

            if ($arr[$maxIndex] < $arr[$j]) {
                $maxIndex = $j;
            }
        }
        //ps 要max 记录的是指针  不知值传递
        //根据指针 进行值交换 ps.脑子有点糊涂了 蛋疼 jcsn
        $tmp = $arr[$len - $i];
        $arr[$len - $i] = $arr[$maxIndex];
        $arr[$maxIndex] = $tmp;
    }
    return $arr;
}

$arr = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5];
print_r(selectionSort($arr));