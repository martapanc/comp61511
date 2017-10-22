
#echo " * wc_argparse.py:"
#python3 wc_argparse.py -wcmlL ${@:1}
#echo
echo " * wc_unit.py:"
#python3 final_wc.py -wcmlL ${@:1}
python3 final_wc.py  ${@:1}
echo
# echo " * wc2:"
# python wc2.py ${@:1}
# echo
# echo " * wc3:"
# python wc3.py ${@:1}
# echo
echo " * wc:"
#wc -wcmlL ${@:1}
wc ${@:1}
