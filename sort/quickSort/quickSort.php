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
    //�������� �������ڵ���1
    if (count($array) <= 1) {
        return $array;
    }
    //�ݹ����� ���зָ�  С������ + ��ǰԪ�� + ��������
    // �����ȡһ��Ԫ��
    $pickKey = array_rand($array);
    $pickValue = $array[$pickKey];
    // ��ȡ�����Ԫ��С��Ԫ��
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