#!/bin/bash

#抓取使用的显存
echo xiancun
xiancun=$(nvidia-smi | grep -w localization | awk -F ' ' '{print $8}' | grep -oE '[0-9]+')
echo $xiancun"m"

#抓取占用的gpu百分比
echo gpu
gpu=$(python3 ./nvit.py | grep point_localization | awk -F ' ' '{print $7}')
echo $gpu"%"

#抓取单核cpu的占用量
echo cpu
cpu_in_one_core=$(top -b -n 1  | grep -w localization | awk -F ' ' '{print $9}')
#echo $cpu_in_one_core"%"
#电脑核心总数
cores_in_computor=$(grep "processor" /proc/cpuinfo | wc -l)
cpu_in_all_cores=$(echo "scale=3;$cpu_in_one_core/$cores_in_computor" | bc | grep -oE '[0-9]+\.[0-9]+')
echo cpu_in_one_core"="$cpu_in_one_core"%   "$cores_in_computor" ge he xin"
echo "in all cores="$cpu_in_all_cores"%"
#cpu_in_all_cores=$(($cpu_in_one_core-$cores_in_computor))
#cpu_in_all_cores=`expr $cpu_in_one_core-$cores_in_computor`
#echo $cpu_in_all_cores
#echo $cpu_in_one_core":"$cores_in_computor

#抓取host mem的占用量
echo mem
mem=$(top -b -n 1  | grep -w localization | awk -F ' ' '{print $10}')
echo $mem"%"
echo "-----"

#时间
time=$(date "+%Y-%m-%d %H:%M:%S")

#时间，显存占用百分比，gpu占用百分比，cpu在单核中的占用量，本机cpu的总核心数量，内存占用百分比
#echo $time,$xiancun,$gpu,$cpu_in_all_cores,$mem >> ./resource.csv
echo $time,$xiancun,$gpu,$cpu_in_one_core,$cores_in_computor,$mem >> ./resource.csv


#echo $cpu_in_one_core" "$cores_in_computor
#echo "scale=3;$cpu_in_one_core/$cores_in_computor" | bc




