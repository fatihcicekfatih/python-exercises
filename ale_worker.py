#!/bin/bash
# read -p "Input a number: " number

# if [[ $number -gt 50 ]] #true
# then
#   echo "The number is big."
# elif [[ $number -lt 50 ]]
# then
#     echo "The number is small."
# else
# fi

# #!/bin/bash
# read -p "Input a number: " number

# if (( $number > 50 )) #true
# then
#     if ((50< $number<60))
#     then
#         echo "The number is big."
#     elif (($number < 70))
#     then
#     echo "The number is bigger."
#     else
#     echo "The number is bigger more."
#     fi
# elif (($number <50))
# then
#     echo "The number is equal."
# fi


###yaþ-emeklilik
read -p "Enter Name:" NAME
read -p "Enter Age:" AGE
read -p "Enter Ale:" ALE
if (($AGE<18)) #true
then
    echo "Student" 
    echo "At least $((X=18-$AGE)) years to become a worker"
elif  (($AGE<65))
then
    echo "Worker"
    echo "$((X=65-$AGE)) years to retire"
else
    if (($AGE < $ALE))
    then
        echo "Retired"
        echo "$((X=$ALE-$AGE)) years to die"
    else
        echo -ne '\007'
        echo "!!!Already died!!!"
        sleep 1
        echo "!!!Already died!!!"
        sleep 2
        echo "!!!Already died!!!"
    fi
fi