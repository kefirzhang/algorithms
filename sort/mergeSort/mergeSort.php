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

    //�������� �������ڵ���1
    if (count($array) <= 1) {
        return $array;
    }
    //�ݹ�����
    // ���������
    $num = ceil(count($array) / 2);
    $chunkData = array_chunk($array, $num);
    $left = mergeSort($chunkData[0]);
    $right = mergeSort($chunkData[1]);
    // �� ���¶��ź������벿�ֺ��ź�����Ұ벿������
    $sortedData = [];
    while (count($left) > 0 && count($right) > 0) {
        if ($left[0] <= $right[0]) {
            $sortedData[] = array_shift($left);
        } else {
            $sortedData[] = array_shift($right);
        }
    }
    //׷�� ʣ�µ�
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
