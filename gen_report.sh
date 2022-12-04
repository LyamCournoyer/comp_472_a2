dir=output_files/solution
for f in $dir/*; do
    f_name=`basename $f .txt`
    name=`echo $f_name | awk -F'-' '{ print $1 }'`
    puzzle_no=""
    h=""
    output=""
    search_name=${strarr[0]}
    if [[ "$name" == "ucs" ]]; then
        puzzle_no=`echo $f_name | awk -F'-' '{ print $3 }'`
        output="$puzzle_no,$name,NA"
    else
        h=`echo $f_name | awk -F'-' '{ print $2 }'`
        puzzle_no=`echo $f_name | awk -F'-' '{ print $4 }'`
        output="$puzzle_no,$name,$h"
    fi
    time_=`grep "Runtime:" $f | awk -F':' '{ print $2 }' | xargs | awk -F' ' '{ print $1 }'`
    if grep -q "No solution" $f; then
        output="$output,NA,NA,$time_"     
    else
        len_sol=`grep "Solution path length:" $f | awk -F':' '{ print $2 }' | xargs`
        len_search=`grep "Search path length:" $f | awk -F':' '{ print $2 }' | xargs`
        output="$output,$len_sol,$len_search,$time_" 
    fi
    echo $output
    IFS=' '
done


# Runtime: 0.024 seconds
# Search path length: 33
# Solution path length: 2