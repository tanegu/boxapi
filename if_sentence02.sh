#!/bin/bash

SCR="python /Users/tanegu/Desktop/boxapi/boxapi6.py"
RESULT='<Box File - 460527349299 (data01)><Box File - 460527606671 (data02)><Box File - 460530323749 (data03)><Box File - 460540008243 (data04)><Box File - 460540113455 (data05)><Box File - 460543608143 (data06)><Box File - 460540106903 (data07)><Box File - 460540050257 (data08)><Box File - 460532181898 (data09)><Box File - 460532497156 (data10)><Box File - 460530438150 (data11)><Box File - 460540895469 (data12)><Box File - 460532207206 (data13)><Box File - 460532406254 (data14)><Box File - 460532685724 (data15)><Box File - 460541020572 (data16)><Box File - 460530755403 (data17)><Box File - 460532997968 (data18)><Box File - 460541050621 (data19)><Box File - 460541809829 (data20)><Box File - 460532528866 (data21)><Box File - 460531309396 (data22)><Box File - 460541373768 (data23)><Box File - 460532805886 (data24)><Box File - 460527897097 (data25)><Box File - 460541711713 (data26)><Box File - 460532900847 (data27)><Box File - 460541721843 (data28)><Box File - 460531422502 (data29)><Box File - 460542269472 (data30)>'

if $SCR | grep -sq "$RESULT"; then
    echo "OK"
    else 
    echo "NG"
    :
fi