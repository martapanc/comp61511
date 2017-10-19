
echo " * wc_argparse.py:"
python3 wc_argparse.py ${@:1}
echo
echo " * wc_unit.py:"
python3 wc_unit.py ${@:1}
echo
echo " * wc2:"
python wc2.py ${@:1}
echo
echo " * wc3:"
python wc3.py ${@:1}
echo
echo " * wc:"
wc ${@:1}
